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


class CreateShowcaseItemMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Showcase):
        FUNCTION = "CreateShowcaseItemMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateShowcaseItemMasterRequest, self).__init__(params)
        if params is None:
            self.__showcase_name = None
        else:
            self.set_showcase_name(params['showcaseName'] if 'showcaseName' in params.keys() else None)
        if params is None:
            self.__category = None
        else:
            self.set_category(params['category'] if 'category' in params.keys() else None)
        if params is None:
            self.__item_name = None
        else:
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)
        if params is None:
            self.__item_group_name = None
        else:
            self.set_item_group_name(params['itemGroupName'] if 'itemGroupName' in params.keys() else None)
        if params is None:
            self.__release_condition_type = None
        else:
            self.set_release_condition_type(params['releaseConditionType'] if 'releaseConditionType' in params.keys() else None)
        if params is None:
            self.__release_condition_schedule_name = None
        else:
            self.set_release_condition_schedule_name(params['releaseConditionScheduleName'] if 'releaseConditionScheduleName' in params.keys() else None)
        if params is None:
            self.__release_condition_schedule_event_name = None
        else:
            self.set_release_condition_schedule_event_name(params['releaseConditionScheduleEventName'] if 'releaseConditionScheduleEventName' in params.keys() else None)
        if params is None:
            self.__priority = None
        else:
            self.set_priority(params['priority'] if 'priority' in params.keys() else None)

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
        :rtype: CreateShowcaseItemMasterRequest
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
        :rtype: CreateShowcaseItemMasterRequest
        """
        self.set_category(category)
        return self

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
        if item_name and not (isinstance(item_name, str) or isinstance(item_name, unicode)):
            raise TypeError(type(item_name))
        self.__item_name = item_name

    def with_item_name(self, item_name):
        """
        商品名を設定
        :param item_name: 商品名
        :type item_name: unicode
        :return: this
        :rtype: CreateShowcaseItemMasterRequest
        """
        self.set_item_name(item_name)
        return self

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
        if item_group_name and not (isinstance(item_group_name, str) or isinstance(item_group_name, unicode)):
            raise TypeError(type(item_group_name))
        self.__item_group_name = item_group_name

    def with_item_group_name(self, item_group_name):
        """
        グループ名を設定
        :param item_group_name: グループ名
        :type item_group_name: unicode
        :return: this
        :rtype: CreateShowcaseItemMasterRequest
        """
        self.set_item_group_name(item_group_name)
        return self

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
        if release_condition_type and not (isinstance(release_condition_type, str) or isinstance(release_condition_type, unicode)):
            raise TypeError(type(release_condition_type))
        self.__release_condition_type = release_condition_type

    def with_release_condition_type(self, release_condition_type):
        """
        公開判定の種類を設定
        :param release_condition_type: 公開判定の種類
        :type release_condition_type: unicode
        :return: this
        :rtype: CreateShowcaseItemMasterRequest
        """
        self.set_release_condition_type(release_condition_type)
        return self

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
        if release_condition_schedule_name and not (isinstance(release_condition_schedule_name, str) or isinstance(release_condition_schedule_name, unicode)):
            raise TypeError(type(release_condition_schedule_name))
        self.__release_condition_schedule_name = release_condition_schedule_name

    def with_release_condition_schedule_name(self, release_condition_schedule_name):
        """
        公開許可判定 に実行されるGS2-Scheduleを設定
        :param release_condition_schedule_name: 公開許可判定 に実行されるGS2-Schedule
        :type release_condition_schedule_name: unicode
        :return: this
        :rtype: CreateShowcaseItemMasterRequest
        """
        self.set_release_condition_schedule_name(release_condition_schedule_name)
        return self

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
        if release_condition_schedule_event_name and not (isinstance(release_condition_schedule_event_name, str) or isinstance(release_condition_schedule_event_name, unicode)):
            raise TypeError(type(release_condition_schedule_event_name))
        self.__release_condition_schedule_event_name = release_condition_schedule_event_name

    def with_release_condition_schedule_event_name(self, release_condition_schedule_event_name):
        """
        公開許可判定 に実行されるGS2-Schedule のイベント名を設定
        :param release_condition_schedule_event_name: 公開許可判定 に実行されるGS2-Schedule のイベント名
        :type release_condition_schedule_event_name: unicode
        :return: this
        :rtype: CreateShowcaseItemMasterRequest
        """
        self.set_release_condition_schedule_event_name(release_condition_schedule_event_name)
        return self

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
        if priority and not isinstance(priority, int):
            raise TypeError(type(priority))
        self.__priority = priority

    def with_priority(self, priority):
        """
        応答順序優先度を設定
        :param priority: 応答順序優先度
        :type priority: int
        :return: this
        :rtype: CreateShowcaseItemMasterRequest
        """
        self.set_priority(priority)
        return self
