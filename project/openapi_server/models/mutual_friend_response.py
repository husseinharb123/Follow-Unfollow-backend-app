# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.user_info import UserInfo
from openapi_server import util

from openapi_server.models.user_info import UserInfo  # noqa: E501

class MutualFriendResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, users=None):  # noqa: E501
        """MutualFriendResponse - a model defined in OpenAPI

        :param message: The message of this MutualFriendResponse.  # noqa: E501
        :type message: str
        :param users: The users of this MutualFriendResponse.  # noqa: E501
        :type users: List[UserInfo]
        """
        self.openapi_types = {
            'message': str,
            'users': List[UserInfo]
        }

        self.attribute_map = {
            'message': 'message',
            'users': 'users'
        }

        self._message = message
        self._users = users

    @classmethod
    def from_dict(cls, dikt) -> 'MutualFriendResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MutualFriendResponse of this MutualFriendResponse.  # noqa: E501
        :rtype: MutualFriendResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this MutualFriendResponse.


        :return: The message of this MutualFriendResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this MutualFriendResponse.


        :param message: The message of this MutualFriendResponse.
        :type message: str
        """

        self._message = message

    @property
    def users(self):
        """Gets the users of this MutualFriendResponse.


        :return: The users of this MutualFriendResponse.
        :rtype: List[UserInfo]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this MutualFriendResponse.


        :param users: The users of this MutualFriendResponse.
        :type users: List[UserInfo]
        """

        self._users = users