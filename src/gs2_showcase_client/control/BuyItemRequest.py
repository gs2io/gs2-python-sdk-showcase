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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_showcase_client.Gs2Showcase import Gs2Showcase


class BuyItemRequest(Gs2UserRequest):

    class Constant(Gs2Showcase):
        FUNCTION = "BuyItem"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(BuyItemRequest, self).__init__(params)
        if params is None:
            self.__showcase_name = None
            self.__showcase_item_id = None
            self.__key_name = None
        else:
            self.set_showcase_name(params['showcaseName'] if 'showcaseName' in params.keys() else None)
            self.set_showcase_item_id(params['showcaseItemId'] if 'showcaseItemId' in params.keys() else None)
            self.set_key_name(params['keyName'] if 'keyName' in params.keys() else None)

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
        :rtype: BuyItemRequest
        """
        self.set_showcase_name(showcase_name)
        return self

    def get_showcase_item_id(self):
        """
        陳列商品のIDを取得
        :return: 陳列商品のID
        :rtype: unicode
        """
        return self.__showcase_item_id

    def set_showcase_item_id(self, showcase_item_id):
        """
        陳列商品のIDを設定
        :param showcase_item_id: 陳列商品のID
        :type showcase_item_id: unicode
        """
        if showcase_item_id is not None and not (isinstance(showcase_item_id, str) or isinstance(showcase_item_id, unicode)):
            raise TypeError(type(showcase_item_id))
        self.__showcase_item_id = showcase_item_id

    def with_showcase_item_id(self, showcase_item_id):
        """
        陳列商品のIDを設定
        :param showcase_item_id: 陳列商品のID
        :type showcase_item_id: unicode
        :return: this
        :rtype: BuyItemRequest
        """
        self.set_showcase_item_id(showcase_item_id)
        return self

    def get_key_name(self):
        """
        スタンプシートの暗号化に使う GS2-Key 暗号鍵名を取得
        :return: スタンプシートの暗号化に使う GS2-Key 暗号鍵名
        :rtype: unicode
        """
        return self.__key_name

    def set_key_name(self, key_name):
        """
        スタンプシートの暗号化に使う GS2-Key 暗号鍵名を設定
        :param key_name: スタンプシートの暗号化に使う GS2-Key 暗号鍵名
        :type key_name: unicode
        """
        if key_name is not None and not (isinstance(key_name, str) or isinstance(key_name, unicode)):
            raise TypeError(type(key_name))
        self.__key_name = key_name

    def with_key_name(self, key_name):
        """
        スタンプシートの暗号化に使う GS2-Key 暗号鍵名を設定
        :param key_name: スタンプシートの暗号化に使う GS2-Key 暗号鍵名
        :type key_name: unicode
        :return: this
        :rtype: BuyItemRequest
        """
        self.set_key_name(key_name)
        return self
