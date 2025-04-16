import re
from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('https://www.youtube.com')
        tem_val = dict(value).get(self.field)
        if not bool(reg.match(tem_val)):
            raise ValidationError('можно добавлять только ролики с youtube.com')