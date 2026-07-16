import numpy as np

from speech.recognizer import SpeechRecognizer

recognizer = SpeechRecognizer()

recognizer.load_model()

recognizer.transcribe(
    np.array([], dtype=np.float32)
)