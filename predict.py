# predict.py
class Predictor:
    def setup(self):
        pass  # Инициализация модели (если нужно)

    def predict(self, text: str) -> str:
        return f"Ты написал: {text}"
