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


class UpdateShowcaseRequest(Gs2BasicRequest):

    class Constant(Gs2Showcase):
        FUNCTION = "UpdateShowcase"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateShowcaseRequest, self).__init__(params)
        if params is None:
            self.__showcase_name = None
        else:
            self.set_showcase_name(params['showcaseName'] if 'showcaseName' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__release_condition_trigger_script = None
        else:
            self.set_release_condition_trigger_script(params['releaseConditionTriggerScript'] if 'releaseConditionTriggerScript' in params.keys() else None)
        if params is None:
            self.__buy_trigger_script = None
        else:
            self.set_buy_trigger_script(params['buyTriggerScript'] if 'buyTriggerScript' in params.keys() else None)

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
        :rtype: UpdateShowcaseRequest
        """
        self.set_showcase_name(showcase_name)
        return self

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        if description is not None and not (isinstance(description, str) or isinstance(description, unicode)):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: UpdateShowcaseRequest
        """
        self.set_description(description)
        return self

    def get_release_condition_trigger_script(self):
        """
        公開許可判定 に実行されるGS2-Scriptを取得
        :return: 公開許可判定 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__release_condition_trigger_script

    def set_release_condition_trigger_script(self, release_condition_trigger_script):
        """
        公開許可判定 に実行されるGS2-Scriptを設定
        :param release_condition_trigger_script: 公開許可判定 に実行されるGS2-Script
        :type release_condition_trigger_script: unicode
        """
        if release_condition_trigger_script is not None and not (isinstance(release_condition_trigger_script, str) or isinstance(release_condition_trigger_script, unicode)):
            raise TypeError(type(release_condition_trigger_script))
        self.__release_condition_trigger_script = release_condition_trigger_script

    def with_release_condition_trigger_script(self, release_condition_trigger_script):
        """
        公開許可判定 に実行されるGS2-Scriptを設定
        :param release_condition_trigger_script: 公開許可判定 に実行されるGS2-Script
        :type release_condition_trigger_script: unicode
        :return: this
        :rtype: UpdateShowcaseRequest
        """
        self.set_release_condition_trigger_script(release_condition_trigger_script)
        return self

    def get_buy_trigger_script(self):
        """
        購入直前 に実行されるGS2-Scriptを取得
        :return: 購入直前 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__buy_trigger_script

    def set_buy_trigger_script(self, buy_trigger_script):
        """
        購入直前 に実行されるGS2-Scriptを設定
        :param buy_trigger_script: 購入直前 に実行されるGS2-Script
        :type buy_trigger_script: unicode
        """
        if buy_trigger_script is not None and not (isinstance(buy_trigger_script, str) or isinstance(buy_trigger_script, unicode)):
            raise TypeError(type(buy_trigger_script))
        self.__buy_trigger_script = buy_trigger_script

    def with_buy_trigger_script(self, buy_trigger_script):
        """
        購入直前 に実行されるGS2-Scriptを設定
        :param buy_trigger_script: 購入直前 に実行されるGS2-Script
        :type buy_trigger_script: unicode
        :return: this
        :rtype: UpdateShowcaseRequest
        """
        self.set_buy_trigger_script(buy_trigger_script)
        return self
