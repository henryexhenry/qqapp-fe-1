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

class Composition(object):
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
        'name': 'str',
        'composer': 'str',
        'level': 'int',
        'remark': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'composer': 'composer',
        'level': 'level',
        'remark': 'remark',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, composer=None, level=None, remark=None, create_time=None, update_time=None):  # noqa: E501
        """Composition - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._composer = None
        self._level = None
        self._remark = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.composer = composer
        self.level = level
        if remark is not None:
            self.remark = remark
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this Composition.  # noqa: E501


        :return: The id of this Composition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Composition.


        :param id: The id of this Composition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Composition.  # noqa: E501


        :return: The name of this Composition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Composition.


        :param name: The name of this Composition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def composer(self):
        """Gets the composer of this Composition.  # noqa: E501


        :return: The composer of this Composition.  # noqa: E501
        :rtype: str
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this Composition.


        :param composer: The composer of this Composition.  # noqa: E501
        :type: str
        """
        if composer is None:
            raise ValueError("Invalid value for `composer`, must not be `None`")  # noqa: E501

        self._composer = composer

    @property
    def level(self):
        """Gets the level of this Composition.  # noqa: E501


        :return: The level of this Composition.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Composition.


        :param level: The level of this Composition.  # noqa: E501
        :type: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def remark(self):
        """Gets the remark of this Composition.  # noqa: E501


        :return: The remark of this Composition.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this Composition.


        :param remark: The remark of this Composition.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def create_time(self):
        """Gets the create_time of this Composition.  # noqa: E501


        :return: The create_time of this Composition.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Composition.


        :param create_time: The create_time of this Composition.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Composition.  # noqa: E501


        :return: The update_time of this Composition.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Composition.


        :param update_time: The update_time of this Composition.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

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
        if issubclass(Composition, dict):
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
        if not isinstance(other, Composition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
