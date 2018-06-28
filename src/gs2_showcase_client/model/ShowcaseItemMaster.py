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


class ShowcaseItemMaster(object):

    def __init__(self, params=None):
        if params is None:
            self.__showcase_item_id = None
            self.__category = None
            self.__item_name = None
            self.__item_group_name = None
            self.__release_condition_type = None
            self.__release_condition_schedule_name = None
            self.__release_condition_schedule_event_name = None
            self.__priority = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_showcase_item_id(params['showcaseItemId'] if 'showcaseItemId' in params.keys() else None)
            self.set_category(params['category'] if 'category' in params.keys() else None)
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)
            self.set_item_group_name(params['itemGroupName'] if 'itemGroupName' in params.keys() else None)
            self.set_release_condition_type(params['releaseConditionType'] if 'releaseConditionType' in params.keys() else None)
            self.set_release_condition_schedule_name(params['releaseConditionScheduleName'] if 'releaseConditionScheduleName' in params.keys() else None)
            self.set_release_condition_schedule_event_name(params['releaseConditionScheduleEventName'] if 'releaseConditionScheduleEventName' in params.keys() else None)
            self.set_priority(params['priority'] if 'priority' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_showcase_item_id(self):
        """
        陳列商品GRNを取得
        :return: 陳列商品GRN
        :rtype: unicode
        """
        return self.__showcase_item_id

    def set_showcase_item_id(self, showcase_item_id):
        """
        陳列商品GRNを設定
        :param showcase_item_id: 陳列商品GRN
        :type showcase_item_id: unicode
        """
        self.__showcase_item_id = showcase_item_id

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
        self.__category = category

    def get_item_name(self):
        """
        商品名を取得
        :return: 商品名
        :rtype: unicode
        """
        return self.__item_name

    def set_item_name(self, item_name):
        """
        商品名を設定
        :param item_name: 商品名
        :type item_name: unicode
        """
        self.__item_name = item_name

    def get_item_group_name(self):
        """
        グループ名を取得
        :return: グループ名
        :rtype: unicode
        """
        return self.__item_group_name

    def set_item_group_name(self, item_group_name):
        """
        グループ名を設定
        :param item_group_name: グループ名
        :type item_group_name: unicode
        """
        self.__item_group_name = item_group_name

    def get_release_condition_type(self):
        """
        公開判定の種類を取得
        :return: 公開判定の種類
        :rtype: unicode
        """
        return self.__release_condition_type

    def set_release_condition_type(self, release_condition_type):
        """
        公開判定の種類を設定
        :param release_condition_type: 公開判定の種類
        :type release_condition_type: unicode
        """
        self.__release_condition_type = release_condition_type

    def get_release_condition_schedule_name(self):
        """
        公開許可判定 に実行されるGS2-Scheduleを取得
        :return: 公開許可判定 に実行されるGS2-Schedule
        :rtype: unicode
        """
        return self.__release_condition_schedule_name

    def set_release_condition_schedule_name(self, release_condition_schedule_name):
        """
        公開許可判定 に実行されるGS2-Scheduleを設定
        :param release_condition_schedule_name: 公開許可判定 に実行されるGS2-Schedule
        :type release_condition_schedule_name: unicode
        """
        self.__release_condition_schedule_name = release_condition_schedule_name

    def get_release_condition_schedule_event_name(self):
        """
        公開許可判定 に実行されるGS2-Schedule のイベント名を取得
        :return: 公開許可判定 に実行されるGS2-Schedule のイベント名
        :rtype: unicode
        """
        return self.__release_condition_schedule_event_name

    def set_release_condition_schedule_event_name(self, release_condition_schedule_event_name):
        """
        公開許可判定 に実行されるGS2-Schedule のイベント名を設定
        :param release_condition_schedule_event_name: 公開許可判定 に実行されるGS2-Schedule のイベント名
        :type release_condition_schedule_event_name: unicode
        """
        self.__release_condition_schedule_event_name = release_condition_schedule_event_name

    def get_priority(self):
        """
        応答順序優先度を取得
        :return: 応答順序優先度
        :rtype: int
        """
        return self.__priority

    def set_priority(self, priority):
        """
        応答順序優先度を設定
        :param priority: 応答順序優先度
        :type priority: int
        """
        self.__priority = priority

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
        return super(ShowcaseItemMaster, self).__getitem__(key)

    def to_dict(self):
        return {
            "showcaseItemId": self.__showcase_item_id,
            "category": self.__category,
            "itemName": self.__item_name,
            "itemGroupName": self.__item_group_name,
            "releaseConditionType": self.__release_condition_type,
            "releaseConditionScheduleName": self.__release_condition_schedule_name,
            "releaseConditionScheduleEventName": self.__release_condition_schedule_event_name,
            "priority": self.__priority,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
