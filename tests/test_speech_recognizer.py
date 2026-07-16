from speech.recognizer import SpeechRecognizer


def main():

    recognizer = SpeechRecognizer()

    print(f"Loaded: {recognizer.model_loaded}")

    recognizer.load_model()

    print(f"Loaded: {recognizer.model_loaded}")


if __name__ == "__main__":
    main()