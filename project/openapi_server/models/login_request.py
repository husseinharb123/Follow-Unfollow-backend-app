# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class LoginRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email=None, password=None):  # noqa: E501
        """LoginRequest - a model defined in OpenAPI

        :param email: The email of this LoginRequest.  # noqa: E501
        :type email: str
        :param password: The password of this LoginRequest.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'email': str,
            'password': str
        }

        self.attribute_map = {
            'email': 'Email',
            'password': 'Password'
        }

        self._email = email
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'LoginRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The login_request of this LoginRequest.  # noqa: E501
        :rtype: LoginRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self):
        """Gets the email of this LoginRequest.


        :return: The email of this LoginRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this LoginRequest.


        :param email: The email of this LoginRequest.
        :type email: str
        """
        if email is not None and len(email) > 50:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `50`")  # noqa: E501
        if email is not None and not re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):  # noqa: E501
            raise ValueError("Invalid value for `email`, must be a follow pattern or equal to `/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this LoginRequest.


        :return: The password of this LoginRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LoginRequest.


        :param password: The password of this LoginRequest.
        :type password: str
        """

        self._password = password