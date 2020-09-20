# from PIL import Image
# from yolo_inference import YoloExecutor
from stream_processor import StreamProcessor


class FrontCameraRuntime:

    def __init__(self):

        # self.yolo = YoloExecutor()
        self.stream_processor = StreamProcessor(operation='add')

    def run_camera(self) -> None:
        self.stream_processor.process_stream()

    # def execute_yolo_inference(self) -> None:
    #     self.stream_processor.process_stream()
    #     input_frame = Image.open('add_image.jpg')
    #     self.yolo.get_labels(input_frame)
    #
    #     print('What about garbage?')
    #     return self.yolo.post_process_stream()
