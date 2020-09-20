import numpy as np
from detection_utilities import detect
from inventory_state_utils import update_inventory_state


class YoloExecutor:

    def __init__(self):
        print('doin tings')
        self.labels = None
        self.detections = []

    def get_labels(self, input_frame: np.ndarray) -> dict:

        print(f'Length of detections: {len(self.detections)}')

        self.detections = detect(input_frame=input_frame, operation='add')   #   Array of tuples (x1, y1, x2, y2, conf, cls_conf, cls_pred) per image

    def post_process_stream(self) -> dict:

        print(self.detections)
        instance_inventory_dict = {}

        for item in self.detections:

            item_name = item[-1]
            instance_inventory_dict = update_inventory_state(input_items={item_name: 1},
                                                             state_inventory_dict=instance_inventory_dict,
                                                             operation='add')

        return instance_inventory_dict
