from models import *
from utils.utils import *
from utils.datasets import *

import numpy as np
import time
import datetime
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms import transforms
from torch.autograd import Variable
from matplotlib.ticker import NullLocator


class FrameImage(Dataset):

    # Wrapper class for loading into DataLoader
    def __init__(self, frame_image):
        self.image_size = 416
        self.frame_image = frame_image

    def __getitem__(self, _):

        return resize(transforms.ToTensor()(self.frame_image), self.image_size)

    def __len__(self):
        return 1


def plot_detections(img_size: int, detections, classes, operation) -> None:

    # Bounding-box colors
    cmap = plt.get_cmap("tab20b")
    colors = [cmap(i) for i in np.linspace(0, 1, 20)]

    print('showing some detections boi')
    # Iterate through images and save plot of detections

    # Create plot
    img = np.array(Image.open(f'{operation}_image.jpg'))
    plt.figure()
    fig, ax = plt.subplots(1)
    ax.imshow(img)

    print(detections)

    # Draw bounding boxes and labels of detections
    if detections is not None:
        # Rescale boxes to original image
        detections = rescale_boxes(detections, img_size, img.shape[:2])
        unique_labels = detections[:, -1].cpu().unique()
        n_cls_preds = len(unique_labels)
        bbox_colors = random.sample(colors, n_cls_preds)
        for x1, y1, x2, y2, conf, cls_conf, cls_pred in detections:
            print("\t+ Label: %s, Conf: %.5f" % (classes[int(cls_pred)], cls_conf.item()))

            box_w = x2 - x1
            box_h = y2 - y1

            color = bbox_colors[int(np.where(unique_labels == int(cls_pred))[0])]
            # Create a Rectangle patch
            bbox = patches.Rectangle((x1, y1), box_w, box_h, linewidth=2, edgecolor=color, facecolor="none")
            # Add the bbox to the plot
            ax.add_patch(bbox)
            # Add label
            plt.text(
                x1,
                y1,
                s=classes[int(cls_pred)],
                color="white",
                verticalalignment="top",
                bbox={"color": color, "pad": 0},
            )

        # Save generated image with detections
        plt.axis("off")
        plt.gca().xaxis.set_major_locator(NullLocator())
        plt.gca().yaxis.set_major_locator(NullLocator())
        plt.savefig(f"seefood_output.png", bbox_inches="tight", pad_inches=0.0)
        plt.close()


def resize(image, size):
    image = F.interpolate(image.unsqueeze(0), size=size, mode="nearest").squeeze(0)
    return image


def detect(input_frame, operation) -> list:

    #   Initialize constants
    model_def = "config/yolov3.cfg"
    weights_path = "weights/yolov3.weights"
    class_path = "data/coco.names"
    conf_thres = 0.8
    nms_thres = 0.4
    batch_size = 1
    n_cpu = 0
    img_size = 416

    #   Wrap the input image into a Dataset
    input_frame_wrapper = FrameImage(input_frame)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Set up model
    model = Darknet(model_def, img_size=img_size).to(device)

    if weights_path.endswith(".weights"):
        # Load darknet weights
        model.load_darknet_weights(weights_path)
    else:
        # Load checkpoint weights
        model.load_state_dict(torch.load(weights_path))

    model.eval()  # Set in evaluation mode

    dataloader = DataLoader(
        input_frame_wrapper,
        batch_size=batch_size,
        shuffle=False,
        num_workers=n_cpu,
    )

    classes = load_classes(class_path)  # Extracts class labels from file

    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

    imgs = []  # Stores image paths
    img_detections = []  # Stores detections for each image index
    tensor_detections = []

    print("\nPerforming object detection:")
    prev_time = time.time()

    for batch_i, input_imgs in enumerate(dataloader):
        # Configure input
        input_imgs = Variable(input_imgs.type(Tensor))

        # Get detections
        with torch.no_grad():
            detections = model(input_imgs)
            detections = non_max_suppression(detections, conf_thres, nms_thres)

            print(detections)
            print(detections[0].tolist())
            detection_list = detections[0].tolist()[0]

            for item in detections[0].tolist():

                detection_list = item
                print('SeeFood found: ')
                print(classes[int(item[6])])

                detection_list[-1] = classes[int(item[6])]
                img_detections.append(detection_list)

            print(img_detections)
            tensor_detections.extend(detections)

            # pred_name = classes[int(detections[0].tolist()[0][6])]

        # Log progress
        current_time = time.time()
        inference_time = datetime.timedelta(seconds=current_time - prev_time)
        prev_time = current_time
        print("\t+ Batch %d, Inference Time: %s" % (batch_i, inference_time))

        #img_detections.extend(detection_list)

    print(tensor_detections)

    for detection in tensor_detections:
        plot_detections(img_size, detection, classes, operation)

    return img_detections
