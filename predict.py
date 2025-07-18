from cog import BasePredictor, Input, Path, BaseModel
import whisperx
import requests
import gc
from datetime import datetime
import os
import time


class Predictor(BasePredictor):
    def setup(self):
        device = "cuda"
        batch_size = 16  # reduce if low on GPU mem
        compute_type = "float16"
        start_time_whisper = datetime.now()
        self.whisper_model = whisperx.load_model("large-v2", device, compute_type=compute_type)
        print(f'Время загрузки модели транскрибации: {datetime.now() - start_time_whisper}')

        start_time_diarize = datetime.now()

    def predict(self, text: str) -> str:
        return f"Ты написал: {text}"
