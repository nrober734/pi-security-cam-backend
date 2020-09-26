import numpy as np
from detection_utilities import detect


class YoloExecutor:

    def __init__(self):
        self.detections = []

    def get_labels(self, input_frame: np.ndarray) -> dict:

        print(f'Length of detections: {len(self.detections)}')

        self.detections = detect(input_frame=input_frame, operation='add')   #   Array of tuples (x1, y1, x2, y2, conf, cls_conf, cls_pred) per image

    def post_process_stream(self) -> dict:

        print(self.detections)
        instance_inventory_dict = {}

        for faces in self.detections:

            item_name = faces[-1]

        return instance_inventory_dict
