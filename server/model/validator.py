from schematics.models import Model
from schematics.types import EmailType, StringType, IntType


class SignupValidator(Model):
    email = EmailType(serialized_name='email', required=True)
    password = StringType(serialized_name='password', required=True, min_length=5, max_length=20)
    name = StringType(serialized_name='name', required=True)
    major = StringType(serialized_name='major', required=True)


class SendEmailCodeValidator(Model):
    email = EmailType(serialized_name='email', required=True)


class CheckEmailCodeValidator(Model):
    email = EmailType(serialized_name='email', required=True)
    code = IntType(serialized_name='code', required=True, min_value=111111, max_value=999999)


class SigninValidator(Model):
    email = EmailType(serialized_name='email', required=True)
    password = StringType(serialized_name='password', required=True, min_length=5, max_length=20)


class CreateNoticeValidator(Model):
    title = StringType(serialized_name='title', required=True, max_length=50)
    content = StringType(serialized_name='content', required=True, max_length=1000)
