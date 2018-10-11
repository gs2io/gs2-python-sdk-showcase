# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_showcase_client.Gs2Showcase import Gs2Showcase


class DeleteItemGroupMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Showcase):
        FUNCTION = "DeleteItemGroupMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteItemGroupMasterRequest, self).__init__(params)
        if params is None:
            self.__showcase_name = None
        else:
            self.set_showcase_name(params['showcaseName'] if 'showcaseName' in params.keys() else None)
        if params is None:
            self.__item_group_name = None
        else:
            self.set_item_group_name(params['itemGroupName'] if 'itemGroupName' in params.keys() else None)

    def get_showcase_name(self):
        """
        ショーケースの名前を取得
        :return: ショーケースの名前
        :rtype: unicode
        """
        return self.__showcase_name

    def set_showcase_name(self, showcase_name):
        """
        ショーケースの名前を設定
        :param showcase_name: ショーケースの名前
        :type showcase_name: unicode
        """
        if showcase_name is not None and not (isinstance(showcase_name, str) or isinstance(showcase_name, unicode)):
            raise TypeError(type(showcase_name))
        self.__showcase_name = showcase_name

    def with_showcase_name(self, showcase_name):
        """
        ショーケースの名前を設定
        :param showcase_name: ショーケースの名前
        :type showcase_name: unicode
        :return: this
        :rtype: DeleteItemGroupMasterRequest
        """
        self.set_showcase_name(showcase_name)
        return self

    def get_item_group_name(self):
        """
        商品グループの名前を取得
        :return: 商品グループの名前
        :rtype: unicode
        """
        return self.__item_group_name

    def set_item_group_name(self, item_group_name):
        """
        商品グループの名前を設定
        :param item_group_name: 商品グループの名前
        :type item_group_name: unicode
        """
        if item_group_name is not None and not (isinstance(item_group_name, str) or isinstance(item_group_name, unicode)):
            raise TypeError(type(item_group_name))
        self.__item_group_name = item_group_name

    def with_item_group_name(self, item_group_name):
        """
        商品グループの名前を設定
        :param item_group_name: 商品グループの名前
        :type item_group_name: unicode
        :return: this
        :rtype: DeleteItemGroupMasterRequest
        """
        self.set_item_group_name(item_group_name)
        return self
