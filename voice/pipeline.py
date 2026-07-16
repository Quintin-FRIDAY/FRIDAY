"""
Project F.R.I.D.A.Y.
Voice Pipeline
"""
from __future__ import annotations

import time

from speech.models import TranscriptionResult

from voice.exceptions import (EmptyRecordingError, NoSpeechDetectedError, SpeechRecognitionFailedError)

from audio.audio_manager import AudioManager

from audio.player import AudioPlayer
from audio.recorder import AudioRecorder

from speech.recognizer import SpeechRecognizer


class VoicePipeline:
    """
    Coordinates the voice subsystem.

    The pipeline orchestrates recording and speech recognition
    but does not perform either itself.
    """

    def __init__(
        self,
        audio_manager: AudioManager,
    ) -> None:

        self._audio_manager = audio_manager

        self._recorder: AudioRecorder = (
            audio_manager.get_recorder()
        )

        self._player: AudioPlayer = (
            audio_manager.get_player()
        )

        self._recognizer: SpeechRecognizer = (
            audio_manager.get_speech_recognizer()
        )

    def listen(self, duration: float = 5.0) -> TranscriptionResult:
        """
        Record audio and convert it into text.
        """

        self._recorder.clear()

        self._recorder.start()

        time.sleep(duration)

        self._recorder.stop()

        recording = self._recorder.get_audio()

        # Step 2 - Validate the recording
        if recording.size == 0:
            raise EmptyRecordingError(
                "No audio was recorded."
            )

        # Step 4 - Wrap speech recognition errors
        try:

            result = self._recognizer.transcribe(
                recording
            )

        except Exception as exc:
            raise SpeechRecognitionFailedError(
                str(exc)
            ) from exc

        # Step 3 - Validate the transcription
        if not result.text.strip():
            raise NoSpeechDetectedError(
                "No speech detected."
            )

        return result