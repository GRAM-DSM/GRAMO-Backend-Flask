from schematics.models import Model
from schematics.types import EmailType, StringType


class SignupValidator(Model):
    email = EmailType(serialized_name='email', required=True)
    password = StringType(serialized_name='password', required=True, min_length=5, max_length=20)
    name = StringType(serialized_name='name', required=True)
    major = StringType(serialized_name='major', required=True)
