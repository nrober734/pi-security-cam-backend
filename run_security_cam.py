from camera_runtime import CameraProcessingModule


def camera_detection_runtime() -> None:

    inventory_state_dict = {}
    camera_runtime = CameraProcessingModule()

    while True:
        add_objects = camera_runtime.get_detections()


if __name__ == '__main__':
    camera_detection_runtime()
