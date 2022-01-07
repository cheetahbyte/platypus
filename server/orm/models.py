from uuid import uuid4
from tortoise.models import Model
from tortoise import fields

class Upload(Model):
    id = fields.CharField(pk=True, default=str(uuid4()), max_length=255)
    filename = fields.CharField(max_length=255)
    mimetype = fields.CharField(max_length=255)
    downloads = fields.IntField(default=0)
    owner = fields.ForeignKeyField('models.User', related_name='uploads')
    key = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)



class User(Model):
    id = fields.CharField(pk=True, default=str(uuid4()), max_length=255)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255, null=True)
    email = fields.CharField(max_length=255, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    # oauth2 - google
    google_id = fields.CharField(max_length=255, null=True)
    google_token = fields.CharField(max_length=255, null=True)
    google_refresh_token = fields.CharField(max_length=255, null=True)
    google_expires_at = fields.DatetimeField(null=True)
    google_email = fields.CharField(max_length=255, null=True)
    google_name = fields.CharField(max_length=255, null=True)
    # oauth2 - github
    github_id = fields.CharField(max_length=255, null=True)
    github_token = fields.CharField(max_length=255, null=True)
    github_refresh_token = fields.CharField(max_length=255, null=True)
    github_expires_at = fields.DatetimeField(null=True)
    github_email = fields.CharField(max_length=255, null=True)
    github_name = fields.CharField(max_length=255, null=True)