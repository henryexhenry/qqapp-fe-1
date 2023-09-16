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

class Performance(object):
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
        'comment': 'str',
        'piece_ext_high': 'float',
        'piece_ext_low': 'float',
        'note_img': 'str',
        'suite': 'str',
        'composition': 'str'
    }

    attribute_map = {
        'id': 'id',
        'comment': 'comment',
        'piece_ext_high': 'piece_ext_high',
        'piece_ext_low': 'piece_ext_low',
        'note_img': 'note_img',
        'suite': 'suite',
        'composition': 'composition'
    }

    def __init__(self, id=None, comment=None, piece_ext_high=None, piece_ext_low=None, note_img=None, suite=None, composition=None):  # noqa: E501
        """Performance - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._comment = None
        self._piece_ext_high = None
        self._piece_ext_low = None
        self._note_img = None
        self._suite = None
        self._composition = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if comment is not None:
            self.comment = comment
        if piece_ext_high is not None:
            self.piece_ext_high = piece_ext_high
        if piece_ext_low is not None:
            self.piece_ext_low = piece_ext_low
        if note_img is not None:
            self.note_img = note_img
        self.suite = suite
        if composition is not None:
            self.composition = composition

    @property
    def id(self):
        """Gets the id of this Performance.  # noqa: E501


        :return: The id of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Performance.


        :param id: The id of this Performance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def comment(self):
        """Gets the comment of this Performance.  # noqa: E501


        :return: The comment of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Performance.


        :param comment: The comment of this Performance.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def piece_ext_high(self):
        """Gets the piece_ext_high of this Performance.  # noqa: E501


        :return: The piece_ext_high of this Performance.  # noqa: E501
        :rtype: float
        """
        return self._piece_ext_high

    @piece_ext_high.setter
    def piece_ext_high(self, piece_ext_high):
        """Sets the piece_ext_high of this Performance.


        :param piece_ext_high: The piece_ext_high of this Performance.  # noqa: E501
        :type: float
        """

        self._piece_ext_high = piece_ext_high

    @property
    def piece_ext_low(self):
        """Gets the piece_ext_low of this Performance.  # noqa: E501


        :return: The piece_ext_low of this Performance.  # noqa: E501
        :rtype: float
        """
        return self._piece_ext_low

    @piece_ext_low.setter
    def piece_ext_low(self, piece_ext_low):
        """Sets the piece_ext_low of this Performance.


        :param piece_ext_low: The piece_ext_low of this Performance.  # noqa: E501
        :type: float
        """

        self._piece_ext_low = piece_ext_low

    @property
    def note_img(self):
        """Gets the note_img of this Performance.  # noqa: E501


        :return: The note_img of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._note_img

    @note_img.setter
    def note_img(self, note_img):
        """Sets the note_img of this Performance.


        :param note_img: The note_img of this Performance.  # noqa: E501
        :type: str
        """

        self._note_img = note_img

    @property
    def suite(self):
        """Gets the suite of this Performance.  # noqa: E501


        :return: The suite of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._suite

    @suite.setter
    def suite(self, suite):
        """Sets the suite of this Performance.


        :param suite: The suite of this Performance.  # noqa: E501
        :type: str
        """
        if suite is None:
            raise ValueError("Invalid value for `suite`, must not be `None`")  # noqa: E501

        self._suite = suite

    @property
    def composition(self):
        """Gets the composition of this Performance.  # noqa: E501


        :return: The composition of this Performance.  # noqa: E501
        :rtype: str
        """
        return self._composition

    @composition.setter
    def composition(self, composition):
        """Sets the composition of this Performance.


        :param composition: The composition of this Performance.  # noqa: E501
        :type: str
        """

        self._composition = composition

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
        if issubclass(Performance, dict):
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
        if not isinstance(other, Performance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other