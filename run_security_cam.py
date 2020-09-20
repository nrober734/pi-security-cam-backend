from inventory_state_utils import update_inventory_state
from camera_runtime import CameraRuntime


def camera_detection_runtime() -> None:

    inventory_state_dict = {}
    camera_runtime = CameraRuntime()

    # TODO - add GUI

    while True:
        add_objects = camera_runtime.fetch_inventory()
        object_detection_state_dict = update_inventory_state(input_items=add_objects,
                                                             state_inventory_dict=inventory_state_dict,
                                                             operation='add')
        print(object_detection_state_dict)


if __name__ == '__main__':
    camera_detection_runtime()
