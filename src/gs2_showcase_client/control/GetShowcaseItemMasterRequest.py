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


class GetShowcaseItemMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Showcase):
        FUNCTION = "GetShowcaseItemMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetShowcaseItemMasterRequest, self).__init__(params)
        if params is None:
            self.__showcase_name = None
        else:
            self.set_showcase_name(params['showcaseName'] if 'showcaseName' in params.keys() else None)
        if params is None:
            self.__category = None
        else:
            self.set_category(params['category'] if 'category' in params.keys() else None)
        if params is None:
            self.__resource_id = None
        else:
            self.set_resource_id(params['resourceId'] if 'resourceId' in params.keys() else None)

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
        :rtype: GetShowcaseItemMasterRequest
        """
        self.set_showcase_name(showcase_name)
        return self

    def get_category(self):
        """
        商品の種類を取得
        :return: 商品の種類
        :rtype: unicode
        """
        return self.__category

    def set_category(self, category):
        """
        商品の種類を設定
        :param category: 商品の種類
        :type category: unicode
        """
        if category and not (isinstance(category, str) or isinstance(category, unicode)):
            raise TypeError(type(category))
        self.__category = category

    def with_category(self, category):
        """
        商品の種類を設定
        :param category: 商品の種類
        :type category: unicode
        :return: this
        :rtype: GetShowcaseItemMasterRequest
        """
        self.set_category(category)
        return self

    def get_resource_id(self):
        """
        商品/商品グループ名を取得
        :return: 商品/商品グループ名
        :rtype: unicode
        """
        return self.__resource_id

    def set_resource_id(self, resource_id):
        """
        商品/商品グループ名を設定
        :param resource_id: 商品/商品グループ名
        :type resource_id: unicode
        """
        if resource_id and not (isinstance(resource_id, str) or isinstance(resource_id, unicode)):
            raise TypeError(type(resource_id))
        self.__resource_id = resource_id

    def with_resource_id(self, resource_id):
        """
        商品/商品グループ名を設定
        :param resource_id: 商品/商品グループ名
        :type resource_id: unicode
        :return: this
        :rtype: GetShowcaseItemMasterRequest
        """
        self.set_resource_id(resource_id)
        return self
