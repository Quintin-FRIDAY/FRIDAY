"""
Project F.R.I.D.A.Y.
Voice Controller
"""

from __future__ import annotations

from core.brain import Brain

from voice.session import VoiceSession

from voice.exceptions import (NoSpeechDetectedError, EmptyRecordingError, SpeechRecognitionFailedError)

from core.logger import log


class VoiceController:
    """
    Coordinates voice interaction with the Brain.
    """

    def __init__(
        self,
        session: VoiceSession,
        brain: Brain,
    ) -> None:

        self._session = session
        self._brain = brain

    def process_once(self):

        try:

            result = self._session.listen()

            log("Listening for voice input...")

            response = self._brain.process(result.text)

            log("Brain processed voice command.")

            log(f'Recognized: "{result.text}"')
            
            return response

        except NoSpeechDetectedError:

            print("No speech detected.")

        except EmptyRecordingError:

            print("No audio was recorded.")

        except SpeechRecognitionFailedError as exc:

            print(f"Speech recognition failed: {exc}")