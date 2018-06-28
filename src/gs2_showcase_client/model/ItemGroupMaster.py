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


class ItemGroupMaster(object):

    def __init__(self, params=None):
        if params is None:
            self.__item_group_id = None
            self.__name = None
            self.__item_names = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_item_group_id(params['itemGroupId'] if 'itemGroupId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_item_names(params['itemNames'] if 'itemNames' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_item_group_id(self):
        """
        商品グループGRNを取得
        :return: 商品グループGRN
        :rtype: unicode
        """
        return self.__item_group_id

    def set_item_group_id(self, item_group_id):
        """
        商品グループGRNを設定
        :param item_group_id: 商品グループGRN
        :type item_group_id: unicode
        """
        self.__item_group_id = item_group_id

    def get_name(self):
        """
        商品グループ名を取得
        :return: 商品グループ名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        商品グループ名を設定
        :param name: 商品グループ名
        :type name: unicode
        """
        self.__name = name

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
        self.__item_names = item_names

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(ItemGroupMaster, self).__getitem__(key)

    def to_dict(self):
        return {
            "itemGroupId": self.__item_group_id,
            "name": self.__name,
            "itemNames": self.__item_names,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
