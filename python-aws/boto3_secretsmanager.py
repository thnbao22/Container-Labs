import typing
import boto3
from base import BaseAWSServiceProcessor

class SecretsManagerProcessor(BaseAWSServiceProcessor):
    def __init__(self, _session: boto3.Session):
        super().__init__(_session)

    def __service_name__(self) -> typing.AnyStr:
        return "secretsmanager"