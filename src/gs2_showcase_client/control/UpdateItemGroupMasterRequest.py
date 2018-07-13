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


class UpdateItemGroupMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Showcase):
        FUNCTION = "UpdateItemGroupMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateItemGroupMasterRequest, self).__init__(params)
        if params is None:
            self.__showcase_name = None
        else:
            self.set_showcase_name(params['showcaseName'] if 'showcaseName' in params.keys() else None)
        if params is None:
            self.__item_group_name = None
        else:
            self.set_item_group_name(params['itemGroupName'] if 'itemGroupName' in params.keys() else None)
        if params is None:
            self.__item_names = None
        else:
            self.set_item_names(params['itemNames'] if 'itemNames' in params.keys() else None)

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
        if showcase_name and not (isinstance(showcase_name, str) or isinstance(showcase_name, unicode)):
            raise TypeError(type(showcase_name))
        self.__showcase_name = showcase_name

    def with_showcase_name(self, showcase_name):
        """
        ショーケースの名前を設定
        :param showcase_name: ショーケースの名前
        :type showcase_name: unicode
        :return: this
        :rtype: UpdateItemGroupMasterRequest
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
        if item_group_name and not (isinstance(item_group_name, str) or isinstance(item_group_name, unicode)):
            raise TypeError(type(item_group_name))
        self.__item_group_name = item_group_name

    def with_item_group_name(self, item_group_name):
        """
        商品グループの名前を設定
        :param item_group_name: 商品グループの名前
        :type item_group_name: unicode
        :return: this
        :rtype: UpdateItemGroupMasterRequest
        """
        self.set_item_group_name(item_group_name)
        return self

    def get_item_names(self):
        """
        販売している商品名のリストを取得
        :return: 販売している商品名のリスト
        :rtype: list[unicode]
        """
        return self.__item_names

    def set_item_names(self, item_names):
        """
        販売している商品名のリストを設定
        :param item_names: 販売している商品名のリスト
        :type item_names: list[unicode]
        """
        if item_names and not isinstance(item_names, list):
            raise TypeError(type(item_names))
        self.__item_names = item_names

    def with_item_names(self, item_names):
        """
        販売している商品名のリストを設定
        :param item_names: 販売している商品名のリスト
        :type item_names: list[unicode]
        :return: this
        :rtype: UpdateItemGroupMasterRequest
        """
        self.set_item_names(item_names)
        return self
