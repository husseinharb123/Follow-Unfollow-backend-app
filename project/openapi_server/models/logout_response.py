# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.user_info import UserInfo
from openapi_server import util

from openapi_server.models.user_info import UserInfo  # noqa: E501

class LogoutResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, user_info=None):  # noqa: E501
        """LogoutResponse - a model defined in OpenAPI

        :param message: The message of this LogoutResponse.  # noqa: E501
        :type message: str
        :param user_info: The user_info of this LogoutResponse.  # noqa: E501
        :type user_info: UserInfo
        """
        self.openapi_types = {
            'message': str,
            'user_info': UserInfo
        }

        self.attribute_map = {
            'message': 'message',
            'user_info': 'user_info'
        }

        self._message = message
        self._user_info = user_info

    @classmethod
    def from_dict(cls, dikt) -> 'LogoutResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LogoutResponse of this LogoutResponse.  # noqa: E501
        :rtype: LogoutResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this LogoutResponse.


        :return: The message of this LogoutResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LogoutResponse.


        :param message: The message of this LogoutResponse.
        :type message: str
        """

        self._message = message

    @property
    def user_info(self):
        """Gets the user_info of this LogoutResponse.


        :return: The user_info of this LogoutResponse.
        :rtype: UserInfo
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info):
        """Sets the user_info of this LogoutResponse.


        :param user_info: The user_info of this LogoutResponse.
        :type user_info: UserInfo
        """

        self._user_info = user_info
