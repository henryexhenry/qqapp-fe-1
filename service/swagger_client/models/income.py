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

class Income(object):
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
        'amount': 'int',
        'status': 'int',
        'comment': 'str',
        'lesson_op_log': 'str',
        'order': 'str'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'status': 'status',
        'comment': 'comment',
        'lesson_op_log': 'lesson_op_log',
        'order': 'order'
    }

    def __init__(self, id=None, amount=None, status=None, comment=None, lesson_op_log=None, order=None):  # noqa: E501
        """Income - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._amount = None
        self._status = None
        self._comment = None
        self._lesson_op_log = None
        self._order = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.amount = amount
        if status is not None:
            self.status = status
        if comment is not None:
            self.comment = comment
        if lesson_op_log is not None:
            self.lesson_op_log = lesson_op_log
        if order is not None:
            self.order = order

    @property
    def id(self):
        """Gets the id of this Income.  # noqa: E501


        :return: The id of this Income.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Income.


        :param id: The id of this Income.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this Income.  # noqa: E501


        :return: The amount of this Income.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Income.


        :param amount: The amount of this Income.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def status(self):
        """Gets the status of this Income.  # noqa: E501


        :return: The status of this Income.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Income.


        :param status: The status of this Income.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def comment(self):
        """Gets the comment of this Income.  # noqa: E501


        :return: The comment of this Income.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Income.


        :param comment: The comment of this Income.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def lesson_op_log(self):
        """Gets the lesson_op_log of this Income.  # noqa: E501


        :return: The lesson_op_log of this Income.  # noqa: E501
        :rtype: str
        """
        return self._lesson_op_log

    @lesson_op_log.setter
    def lesson_op_log(self, lesson_op_log):
        """Sets the lesson_op_log of this Income.


        :param lesson_op_log: The lesson_op_log of this Income.  # noqa: E501
        :type: str
        """

        self._lesson_op_log = lesson_op_log

    @property
    def order(self):
        """Gets the order of this Income.  # noqa: E501


        :return: The order of this Income.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Income.


        :param order: The order of this Income.  # noqa: E501
        :type: str
        """

        self._order = order

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
        if issubclass(Income, dict):
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
        if not isinstance(other, Income):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other