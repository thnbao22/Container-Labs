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
        Parma_data = self.get_params_decryption("ssm_parameter_name")
        Parma_data_data = json.loads(Parma_data)
        return {
            'a': Parma_data_data.get("a"),
            'b': Parma_data_data.get("b"),
            'c': Parma_data_data.get("c"),
            'd': Parma_data_data.get("d"),
            "e": Parma_data_data.get("e")
        }