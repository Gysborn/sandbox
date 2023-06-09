from django.core.exceptions import ValidationError

import string


class LegalWordsValidator:
    """
    Проверка на недопустимые слова
    """

    def __init__(self, words):
        self.words = words

    def _clear_string(self, dirt_str: str) -> list:
        result = dirt_str.translate(str.maketrans('', '', string.punctuation))
        return result.split(' ')

    def __call__(self, title, *args, **kwargs):
        split_title = self._clear_string(title)
        for w in split_title:
            for _ in self.words:
                if w.lower() == _:
                    raise ValidationError(
                        "Недопустимые слова"
                    )
