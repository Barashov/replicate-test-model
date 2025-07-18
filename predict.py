from cog import BasePredictor, BaseModel, Input, Path
from faster_whisper import WhisperModel


class Predictor(BasePredictor):
    def setup(self):
        model_name = "large-v3-turbo"
        self.model = WhisperModel(
            model_name,
            device="cuda",
            compute_type="float16",
        )

    def predict(self, text: str) -> str:
        return f"Ты написал: {text}"
