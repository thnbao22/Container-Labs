import json
import typing
from abc import ABC, abstractmethod

import boto3


class BaseAWSServiceProcessor(ABC):

    def __init__(self, session: boto3.Session):
        self._session = session
        self._client = self._session.client(self.__service_name__())
        self._resource = None

    def resource(self):
        if not self._resource:
            self._resource = self.session().resource(self.__service_name__())
        return self._resource

    def session(self):
        return self._session

    def client(self):
        return self._client

    @staticmethod
    def pretty_res(_res):
        return json.dumps(_res, indent=4, default=str)

    @abstractmethod
    def __service_name__(self) -> typing.AnyStr:
        pass
