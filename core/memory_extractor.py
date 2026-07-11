from core.extractors.name import extract_name
from core.extractors.preferences import extract_preferences
from core.extractors.location import extract_location
from core.extractors.occupation import extract_occupation

class MemoryExtractor:
    """Coordinates all memory extractors."""

    def process(self, text: str):

        extractors = [
            extract_name,
            extract_preferences,
            extract_location,
            extract_occupation,
        ]

        for extractor in extractors:

            response = extractor(text)

            if response is not None:
                return response

        return None