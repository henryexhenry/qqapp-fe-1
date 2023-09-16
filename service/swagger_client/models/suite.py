# coding: utf-8

"""
    QQAPP API

    QQAPP API Description  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Suite(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'est_low': 'float',
        'est_high': 'float',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'exam': 'str'
    }

    attribute_map = {
        'id': 'id',
        'est_low': 'est_low',
        'est_high': 'est_high',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'exam': 'exam'
    }

    def __init__(self, id=None, est_low=None, est_high=None, create_time=None, update_time=None, exam=None):  # noqa: E501
        """Suite - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._est_low = None
        self._est_high = None
        self._create_time = None
        self._update_time = None
        self._exam = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.est_low = est_low
        self.est_high = est_high
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        self.exam = exam

    @property
    def id(self):
        """Gets the id of this Suite.  # noqa: E501


        :return: The id of this Suite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Suite.


        :param id: The id of this Suite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def est_low(self):
        """Gets the est_low of this Suite.  # noqa: E501


        :return: The est_low of this Suite.  # noqa: E501
        :rtype: float
        """
        return self._est_low

    @est_low.setter
    def est_low(self, est_low):
        """Sets the est_low of this Suite.


        :param est_low: The est_low of this Suite.  # noqa: E501
        :type: float
        """
        if est_low is None:
            raise ValueError("Invalid value for `est_low`, must not be `None`")  # noqa: E501

        self._est_low = est_low

    @property
    def est_high(self):
        """Gets the est_high of this Suite.  # noqa: E501


        :return: The est_high of this Suite.  # noqa: E501
        :rtype: float
        """
        return self._est_high

    @est_high.setter
    def est_high(self, est_high):
        """Sets the est_high of this Suite.


        :param est_high: The est_high of this Suite.  # noqa: E501
        :type: float
        """
        if est_high is None:
            raise ValueError("Invalid value for `est_high`, must not be `None`")  # noqa: E501

        self._est_high = est_high

    @property
    def create_time(self):
        """Gets the create_time of this Suite.  # noqa: E501


        :return: The create_time of this Suite.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Suite.


        :param create_time: The create_time of this Suite.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Suite.  # noqa: E501


        :return: The update_time of this Suite.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Suite.


        :param update_time: The update_time of this Suite.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def exam(self):
        """Gets the exam of this Suite.  # noqa: E501


        :return: The exam of this Suite.  # noqa: E501
        :rtype: str
        """
        return self._exam

    @exam.setter
    def exam(self, exam):
        """Sets the exam of this Suite.


        :param exam: The exam of this Suite.  # noqa: E501
        :type: str
        """
        if exam is None:
            raise ValueError("Invalid value for `exam`, must not be `None`")  # noqa: E501

        self._exam = exam

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Suite, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Suite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
