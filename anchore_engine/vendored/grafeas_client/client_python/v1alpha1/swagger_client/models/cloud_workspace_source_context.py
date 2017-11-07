# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class CloudWorkspaceSourceContext(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, workspace_id=None, snapshot_id=None):
        """
        CloudWorkspaceSourceContext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'workspace_id': 'CloudWorkspaceId',
            'snapshot_id': 'str'
        }

        self.attribute_map = {
            'workspace_id': 'workspaceId',
            'snapshot_id': 'snapshotId'
        }

        self._workspace_id = workspace_id
        self._snapshot_id = snapshot_id

    @property
    def workspace_id(self):
        """
        Gets the workspace_id of this CloudWorkspaceSourceContext.
        The ID of the workspace.

        :return: The workspace_id of this CloudWorkspaceSourceContext.
        :rtype: CloudWorkspaceId
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """
        Sets the workspace_id of this CloudWorkspaceSourceContext.
        The ID of the workspace.

        :param workspace_id: The workspace_id of this CloudWorkspaceSourceContext.
        :type: CloudWorkspaceId
        """

        self._workspace_id = workspace_id

    @property
    def snapshot_id(self):
        """
        Gets the snapshot_id of this CloudWorkspaceSourceContext.
        The ID of the snapshot. An empty snapshot_id refers to the most recent snapshot.

        :return: The snapshot_id of this CloudWorkspaceSourceContext.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """
        Sets the snapshot_id of this CloudWorkspaceSourceContext.
        The ID of the snapshot. An empty snapshot_id refers to the most recent snapshot.

        :param snapshot_id: The snapshot_id of this CloudWorkspaceSourceContext.
        :type: str
        """

        self._snapshot_id = snapshot_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other