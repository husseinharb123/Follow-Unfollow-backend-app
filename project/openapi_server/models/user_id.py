# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class UserId(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None):  # noqa: E501
        """UserId - a model defined in OpenAPI

        :param id: The id of this UserId.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': '_id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'UserId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user_id of this UserId.  # noqa: E501
        :rtype: UserId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this UserId.


        :return: The id of this UserId.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserId.


        :param id: The id of this UserId.
        :type id: str
        """
        if id is not None and not re.search(r'^[a-fA-F0-9]{24}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[a-fA-F0-9]{24}$/`")  # noqa: E501

        self._id = id
