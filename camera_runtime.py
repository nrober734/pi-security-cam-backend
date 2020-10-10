from PIL import Image
from yolo_inference import YoloExecutor
from stream_processor import StreamProcessor


class CameraProcessingModule:

    def __init__(self):
        self.yolo = YoloExecutor()
        self.stream_processor = StreamProcessor(operation='add')

    def get_detections(self) -> dict:
        #   Launches the intelligent inventory collection
        self.stream_processor.process_stream()
        input_frame = Image.open('add_image.jpg')
        self.yolo.get_labels(input_frame)

        return self.yolo.post_process_stream()
