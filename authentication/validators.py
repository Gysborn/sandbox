from django.core.exceptions import ValidationError


class MinimumLengthValidator:
    """
        Проверка на длинну
    """

    def __init__(self, min_length=8):
        self.min_length = min_length

    def __call__(self, password, *args, **kwargs):
        if len(password) < self.min_length:
            raise ValidationError(
                f"This password must contain at least {self.min_length} characters."
            )


class NumericInPasswordValidator:
    """
    Проверка на наличие цифр
    """

    def __init__(self):
        pass

    def __call__(self, password, *args, **kwargs):
        if not list(filter(lambda x: x.isdigit(), password)):
            raise ValidationError(
                "This password must be contain numeric."
            )


class EmailValidator:
    """
    Проверка на формат и домены (mail.ru, yandex.ru) почты
    """

    def __init__(self, domain1='mail.ru', domain2='yandex.ru'):
        self.domain1 = domain1
        self.domain2 = domain2

    def __call__(self, password, *args, **kwargs):
        pars = password.split('@')
        if pars[1] not in [self.domain1, self.domain2]:
            raise ValidationError(
                "Допустимые домены: mail.ru, yandex.ru."
            )
