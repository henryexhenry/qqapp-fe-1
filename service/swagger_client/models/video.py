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

class Video(object):
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
        'video_name': 'str',
        'created_time': 'datetime',
        'video_file': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'video_name': 'video_name',
        'created_time': 'created_time',
        'video_file': 'video_file',
        'remark': 'remark'
    }

    def __init__(self, id=None, video_name=None, created_time=None, video_file=None, remark=None):  # noqa: E501
        """Video - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._video_name = None
        self._created_time = None
        self._video_file = None
        self._remark = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.video_name = video_name
        if created_time is not None:
            self.created_time = created_time
        if video_file is not None:
            self.video_file = video_file
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this Video.  # noqa: E501


        :return: The id of this Video.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Video.


        :param id: The id of this Video.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def video_name(self):
        """Gets the video_name of this Video.  # noqa: E501


        :return: The video_name of this Video.  # noqa: E501
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this Video.


        :param video_name: The video_name of this Video.  # noqa: E501
        :type: str
        """
        if video_name is None:
            raise ValueError("Invalid value for `video_name`, must not be `None`")  # noqa: E501

        self._video_name = video_name

    @property
    def created_time(self):
        """Gets the created_time of this Video.  # noqa: E501


        :return: The created_time of this Video.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Video.


        :param created_time: The created_time of this Video.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def video_file(self):
        """Gets the video_file of this Video.  # noqa: E501


        :return: The video_file of this Video.  # noqa: E501
        :rtype: str
        """
        return self._video_file

    @video_file.setter
    def video_file(self, video_file):
        """Sets the video_file of this Video.


        :param video_file: The video_file of this Video.  # noqa: E501
        :type: str
        """

        self._video_file = video_file

    @property
    def remark(self):
        """Gets the remark of this Video.  # noqa: E501


        :return: The remark of this Video.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this Video.


        :param remark: The remark of this Video.  # noqa: E501
        :type: str
        """

        self._remark = remark

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
        if issubclass(Video, dict):
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
        if not isinstance(other, Video):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other