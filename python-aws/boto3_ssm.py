import typing
import boto3
import json

from base import BaseAWSServiceProcessor


class SsmProcessor(BaseAWSServiceProcessor):
    
    def __init__(self, session: boto3.Session):
        super().__init__(session)

    def __service_name__(self) -> typing.AnyStr:
        return "ssm"
    
    def get_params_decryption(self, parameter_name: str):
        _res = self.client().get_parameter(Name=parameter_name, WithDecryption=True)
        return _res['Parameter']['Value']

    def get_all_params_notification(self):
        rds_ops_user = self.get_params_decryption("ssm_parameter_name")
        rds_ops_user_data = json.loads(rds_ops_user)
        return {
            'a': rds_ops_user_data.get("a"),
            'b': rds_ops_user_data.get("b"),
            'c': rds_ops_user_data.get("c"),
            'd': rds_ops_user_data.get("d"),
            "e": rds_ops_user_data.get("e")
        }