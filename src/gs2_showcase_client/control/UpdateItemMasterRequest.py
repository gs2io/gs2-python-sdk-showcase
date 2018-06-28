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


class UpdateItemMasterRequest(Gs2BasicRequest):

    class Constant(Gs2Showcase):
        FUNCTION = "UpdateItemMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateItemMasterRequest, self).__init__(params)
        if params is None:
            self.__showcase_name = None
        else:
            self.set_showcase_name(params['showcaseName'] if 'showcaseName' in params.keys() else None)
        if params is None:
            self.__item_name = None
        else:
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)
        if params is None:
            self.__meta = None
        else:
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
        if params is None:
            self.__currency_type = None
        else:
            self.set_currency_type(params['currencyType'] if 'currencyType' in params.keys() else None)
        if params is None:
            self.__currency_money_name = None
        else:
            self.set_currency_money_name(params['currencyMoneyName'] if 'currencyMoneyName' in params.keys() else None)
        if params is None:
            self.__currency_gold_name = None
        else:
            self.set_currency_gold_name(params['currencyGoldName'] if 'currencyGoldName' in params.keys() else None)
        if params is None:
            self.__currency_option = None
        else:
            self.set_currency_option(params['currencyOption'] if 'currencyOption' in params.keys() else None)
        if params is None:
            self.__price = None
        else:
            self.set_price(params['price'] if 'price' in params.keys() else None)
        if params is None:
            self.__item_type = None
        else:
            self.set_item_type(params['itemType'] if 'itemType' in params.keys() else None)
        if params is None:
            self.__item_money_name = None
        else:
            self.set_item_money_name(params['itemMoneyName'] if 'itemMoneyName' in params.keys() else None)
        if params is None:
            self.__item_gold_name = None
        else:
            self.set_item_gold_name(params['itemGoldName'] if 'itemGoldName' in params.keys() else None)
        if params is None:
            self.__item_stamina_stamina_pool_name = None
        else:
            self.set_item_stamina_stamina_pool_name(params['itemStaminaStaminaPoolName'] if 'itemStaminaStaminaPoolName' in params.keys() else None)
        if params is None:
            self.__item_consumable_item_item_pool_name = None
        else:
            self.set_item_consumable_item_item_pool_name(params['itemConsumableItemItemPoolName'] if 'itemConsumableItemItemPoolName' in params.keys() else None)
        if params is None:
            self.__item_consumable_item_item_name = None
        else:
            self.set_item_consumable_item_item_name(params['itemConsumableItemItemName'] if 'itemConsumableItemItemName' in params.keys() else None)
        if params is None:
            self.__item_amount = None
        else:
            self.set_item_amount(params['itemAmount'] if 'itemAmount' in params.keys() else None)
        if params is None:
            self.__item_option = None
        else:
            self.set_item_option(params['itemOption'] if 'itemOption' in params.keys() else None)
        if params is None:
            self.__open_condition_type = None
        else:
            self.set_open_condition_type(params['openConditionType'] if 'openConditionType' in params.keys() else None)
        if params is None:
            self.__open_condition_limit_name = None
        else:
            self.set_open_condition_limit_name(params['openConditionLimitName'] if 'openConditionLimitName' in params.keys() else None)
        if params is None:
            self.__open_condition_limit_counter_name = None
        else:
            self.set_open_condition_limit_counter_name(params['openConditionLimitCounterName'] if 'openConditionLimitCounterName' in params.keys() else None)

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
        :rtype: UpdateItemMasterRequest
        """
        self.set_showcase_name(showcase_name)
        return self

    def get_item_name(self):
        """
        商品の名前を取得
        :return: 商品の名前
        :rtype: unicode
        """
        return self.__item_name

    def set_item_name(self, item_name):
        """
        商品の名前を設定
        :param item_name: 商品の名前
        :type item_name: unicode
        """
        if item_name and not (isinstance(item_name, str) or isinstance(item_name, unicode)):
            raise TypeError(type(item_name))
        self.__item_name = item_name

    def with_item_name(self, item_name):
        """
        商品の名前を設定
        :param item_name: 商品の名前
        :type item_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_name(item_name)
        return self

    def get_meta(self):
        """
        メタデータを取得
        :return: メタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        """
        if meta and not (isinstance(meta, str) or isinstance(meta, unicode)):
            raise TypeError(type(meta))
        self.__meta = meta

    def with_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_meta(meta)
        return self

    def get_currency_type(self):
        """
        販売通貨を取得
        :return: 販売通貨
        :rtype: unicode
        """
        return self.__currency_type

    def set_currency_type(self, currency_type):
        """
        販売通貨を設定
        :param currency_type: 販売通貨
        :type currency_type: unicode
        """
        if currency_type and not (isinstance(currency_type, str) or isinstance(currency_type, unicode)):
            raise TypeError(type(currency_type))
        self.__currency_type = currency_type

    def with_currency_type(self, currency_type):
        """
        販売通貨を設定
        :param currency_type: 販売通貨
        :type currency_type: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_currency_type(currency_type)
        return self

    def get_currency_money_name(self):
        """
        GS2-Money 課金通貨名を取得
        :return: GS2-Money 課金通貨名
        :rtype: unicode
        """
        return self.__currency_money_name

    def set_currency_money_name(self, currency_money_name):
        """
        GS2-Money 課金通貨名を設定
        :param currency_money_name: GS2-Money 課金通貨名
        :type currency_money_name: unicode
        """
        if currency_money_name and not (isinstance(currency_money_name, str) or isinstance(currency_money_name, unicode)):
            raise TypeError(type(currency_money_name))
        self.__currency_money_name = currency_money_name

    def with_currency_money_name(self, currency_money_name):
        """
        GS2-Money 課金通貨名を設定
        :param currency_money_name: GS2-Money 課金通貨名
        :type currency_money_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_currency_money_name(currency_money_name)
        return self

    def get_currency_gold_name(self):
        """
        GS2-Gold 通貨名を取得
        :return: GS2-Gold 通貨名
        :rtype: unicode
        """
        return self.__currency_gold_name

    def set_currency_gold_name(self, currency_gold_name):
        """
        GS2-Gold 通貨名を設定
        :param currency_gold_name: GS2-Gold 通貨名
        :type currency_gold_name: unicode
        """
        if currency_gold_name and not (isinstance(currency_gold_name, str) or isinstance(currency_gold_name, unicode)):
            raise TypeError(type(currency_gold_name))
        self.__currency_gold_name = currency_gold_name

    def with_currency_gold_name(self, currency_gold_name):
        """
        GS2-Gold 通貨名を設定
        :param currency_gold_name: GS2-Gold 通貨名
        :type currency_gold_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_currency_gold_name(currency_gold_name)
        return self

    def get_currency_option(self):
        """
        対価消費処理にまつわるオプション値を取得
        :return: 対価消費処理にまつわるオプション値
        :rtype: unicode
        """
        return self.__currency_option

    def set_currency_option(self, currency_option):
        """
        対価消費処理にまつわるオプション値を設定
        :param currency_option: 対価消費処理にまつわるオプション値
        :type currency_option: unicode
        """
        if currency_option and not (isinstance(currency_option, str) or isinstance(currency_option, unicode)):
            raise TypeError(type(currency_option))
        self.__currency_option = currency_option

    def with_currency_option(self, currency_option):
        """
        対価消費処理にまつわるオプション値を設定
        :param currency_option: 対価消費処理にまつわるオプション値
        :type currency_option: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_currency_option(currency_option)
        return self

    def get_price(self):
        """
        販売価格を取得
        :return: 販売価格
        :rtype: float
        """
        return self.__price

    def set_price(self, price):
        """
        販売価格を設定
        :param price: 販売価格
        :type price: float
        """
        if price and not isinstance(price, float):
            raise TypeError(type(price))
        self.__price = price

    def with_price(self, price):
        """
        販売価格を設定
        :param price: 販売価格
        :type price: float
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_price(price)
        return self

    def get_item_type(self):
        """
        入手アイテムの種類を取得
        :return: 入手アイテムの種類
        :rtype: unicode
        """
        return self.__item_type

    def set_item_type(self, item_type):
        """
        入手アイテムの種類を設定
        :param item_type: 入手アイテムの種類
        :type item_type: unicode
        """
        if item_type and not (isinstance(item_type, str) or isinstance(item_type, unicode)):
            raise TypeError(type(item_type))
        self.__item_type = item_type

    def with_item_type(self, item_type):
        """
        入手アイテムの種類を設定
        :param item_type: 入手アイテムの種類
        :type item_type: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_type(item_type)
        return self

    def get_item_money_name(self):
        """
        GS2-Money 課金通貨名を取得
        :return: GS2-Money 課金通貨名
        :rtype: unicode
        """
        return self.__item_money_name

    def set_item_money_name(self, item_money_name):
        """
        GS2-Money 課金通貨名を設定
        :param item_money_name: GS2-Money 課金通貨名
        :type item_money_name: unicode
        """
        if item_money_name and not (isinstance(item_money_name, str) or isinstance(item_money_name, unicode)):
            raise TypeError(type(item_money_name))
        self.__item_money_name = item_money_name

    def with_item_money_name(self, item_money_name):
        """
        GS2-Money 課金通貨名を設定
        :param item_money_name: GS2-Money 課金通貨名
        :type item_money_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_money_name(item_money_name)
        return self

    def get_item_gold_name(self):
        """
        GS2-Gold 通貨名を取得
        :return: GS2-Gold 通貨名
        :rtype: unicode
        """
        return self.__item_gold_name

    def set_item_gold_name(self, item_gold_name):
        """
        GS2-Gold 通貨名を設定
        :param item_gold_name: GS2-Gold 通貨名
        :type item_gold_name: unicode
        """
        if item_gold_name and not (isinstance(item_gold_name, str) or isinstance(item_gold_name, unicode)):
            raise TypeError(type(item_gold_name))
        self.__item_gold_name = item_gold_name

    def with_item_gold_name(self, item_gold_name):
        """
        GS2-Gold 通貨名を設定
        :param item_gold_name: GS2-Gold 通貨名
        :type item_gold_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_gold_name(item_gold_name)
        return self

    def get_item_stamina_stamina_pool_name(self):
        """
        GS2-Stamina スタミナプール名を取得
        :return: GS2-Stamina スタミナプール名
        :rtype: unicode
        """
        return self.__item_stamina_stamina_pool_name

    def set_item_stamina_stamina_pool_name(self, item_stamina_stamina_pool_name):
        """
        GS2-Stamina スタミナプール名を設定
        :param item_stamina_stamina_pool_name: GS2-Stamina スタミナプール名
        :type item_stamina_stamina_pool_name: unicode
        """
        if item_stamina_stamina_pool_name and not (isinstance(item_stamina_stamina_pool_name, str) or isinstance(item_stamina_stamina_pool_name, unicode)):
            raise TypeError(type(item_stamina_stamina_pool_name))
        self.__item_stamina_stamina_pool_name = item_stamina_stamina_pool_name

    def with_item_stamina_stamina_pool_name(self, item_stamina_stamina_pool_name):
        """
        GS2-Stamina スタミナプール名を設定
        :param item_stamina_stamina_pool_name: GS2-Stamina スタミナプール名
        :type item_stamina_stamina_pool_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_stamina_stamina_pool_name(item_stamina_stamina_pool_name)
        return self

    def get_item_consumable_item_item_pool_name(self):
        """
        GS2-ConsumableItem アイテムプール名を取得
        :return: GS2-ConsumableItem アイテムプール名
        :rtype: unicode
        """
        return self.__item_consumable_item_item_pool_name

    def set_item_consumable_item_item_pool_name(self, item_consumable_item_item_pool_name):
        """
        GS2-ConsumableItem アイテムプール名を設定
        :param item_consumable_item_item_pool_name: GS2-ConsumableItem アイテムプール名
        :type item_consumable_item_item_pool_name: unicode
        """
        if item_consumable_item_item_pool_name and not (isinstance(item_consumable_item_item_pool_name, str) or isinstance(item_consumable_item_item_pool_name, unicode)):
            raise TypeError(type(item_consumable_item_item_pool_name))
        self.__item_consumable_item_item_pool_name = item_consumable_item_item_pool_name

    def with_item_consumable_item_item_pool_name(self, item_consumable_item_item_pool_name):
        """
        GS2-ConsumableItem アイテムプール名を設定
        :param item_consumable_item_item_pool_name: GS2-ConsumableItem アイテムプール名
        :type item_consumable_item_item_pool_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_consumable_item_item_pool_name(item_consumable_item_item_pool_name)
        return self

    def get_item_consumable_item_item_name(self):
        """
        GS2-ConsumableItem アイテム名を取得
        :return: GS2-ConsumableItem アイテム名
        :rtype: unicode
        """
        return self.__item_consumable_item_item_name

    def set_item_consumable_item_item_name(self, item_consumable_item_item_name):
        """
        GS2-ConsumableItem アイテム名を設定
        :param item_consumable_item_item_name: GS2-ConsumableItem アイテム名
        :type item_consumable_item_item_name: unicode
        """
        if item_consumable_item_item_name and not (isinstance(item_consumable_item_item_name, str) or isinstance(item_consumable_item_item_name, unicode)):
            raise TypeError(type(item_consumable_item_item_name))
        self.__item_consumable_item_item_name = item_consumable_item_item_name

    def with_item_consumable_item_item_name(self, item_consumable_item_item_name):
        """
        GS2-ConsumableItem アイテム名を設定
        :param item_consumable_item_item_name: GS2-ConsumableItem アイテム名
        :type item_consumable_item_item_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_consumable_item_item_name(item_consumable_item_item_name)
        return self

    def get_item_amount(self):
        """
        入手数量を取得
        :return: 入手数量
        :rtype: int
        """
        return self.__item_amount

    def set_item_amount(self, item_amount):
        """
        入手数量を設定
        :param item_amount: 入手数量
        :type item_amount: int
        """
        if item_amount and not isinstance(item_amount, int):
            raise TypeError(type(item_amount))
        self.__item_amount = item_amount

    def with_item_amount(self, item_amount):
        """
        入手数量を設定
        :param item_amount: 入手数量
        :type item_amount: int
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_amount(item_amount)
        return self

    def get_item_option(self):
        """
        アイテムの入手処理にまつわるオプション値を取得
        :return: アイテムの入手処理にまつわるオプション値
        :rtype: unicode
        """
        return self.__item_option

    def set_item_option(self, item_option):
        """
        アイテムの入手処理にまつわるオプション値を設定
        :param item_option: アイテムの入手処理にまつわるオプション値
        :type item_option: unicode
        """
        if item_option and not (isinstance(item_option, str) or isinstance(item_option, unicode)):
            raise TypeError(type(item_option))
        self.__item_option = item_option

    def with_item_option(self, item_option):
        """
        アイテムの入手処理にまつわるオプション値を設定
        :param item_option: アイテムの入手処理にまつわるオプション値
        :type item_option: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_item_option(item_option)
        return self

    def get_open_condition_type(self):
        """
        購入許可判定の種類を取得
        :return: 購入許可判定の種類
        :rtype: unicode
        """
        return self.__open_condition_type

    def set_open_condition_type(self, open_condition_type):
        """
        購入許可判定の種類を設定
        :param open_condition_type: 購入許可判定の種類
        :type open_condition_type: unicode
        """
        if open_condition_type and not (isinstance(open_condition_type, str) or isinstance(open_condition_type, unicode)):
            raise TypeError(type(open_condition_type))
        self.__open_condition_type = open_condition_type

    def with_open_condition_type(self, open_condition_type):
        """
        購入許可判定の種類を設定
        :param open_condition_type: 購入許可判定の種類
        :type open_condition_type: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_open_condition_type(open_condition_type)
        return self

    def get_open_condition_limit_name(self):
        """
        購入許可判定 に実行されるGS2-Limitを取得
        :return: 購入許可判定 に実行されるGS2-Limit
        :rtype: unicode
        """
        return self.__open_condition_limit_name

    def set_open_condition_limit_name(self, open_condition_limit_name):
        """
        購入許可判定 に実行されるGS2-Limitを設定
        :param open_condition_limit_name: 購入許可判定 に実行されるGS2-Limit
        :type open_condition_limit_name: unicode
        """
        if open_condition_limit_name and not (isinstance(open_condition_limit_name, str) or isinstance(open_condition_limit_name, unicode)):
            raise TypeError(type(open_condition_limit_name))
        self.__open_condition_limit_name = open_condition_limit_name

    def with_open_condition_limit_name(self, open_condition_limit_name):
        """
        購入許可判定 に実行されるGS2-Limitを設定
        :param open_condition_limit_name: 購入許可判定 に実行されるGS2-Limit
        :type open_condition_limit_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_open_condition_limit_name(open_condition_limit_name)
        return self

    def get_open_condition_limit_counter_name(self):
        """
        購入許可判定 に実行されるGS2-Limit のカウンターを取得
        :return: 購入許可判定 に実行されるGS2-Limit のカウンター
        :rtype: unicode
        """
        return self.__open_condition_limit_counter_name

    def set_open_condition_limit_counter_name(self, open_condition_limit_counter_name):
        """
        購入許可判定 に実行されるGS2-Limit のカウンターを設定
        :param open_condition_limit_counter_name: 購入許可判定 に実行されるGS2-Limit のカウンター
        :type open_condition_limit_counter_name: unicode
        """
        if open_condition_limit_counter_name and not (isinstance(open_condition_limit_counter_name, str) or isinstance(open_condition_limit_counter_name, unicode)):
            raise TypeError(type(open_condition_limit_counter_name))
        self.__open_condition_limit_counter_name = open_condition_limit_counter_name

    def with_open_condition_limit_counter_name(self, open_condition_limit_counter_name):
        """
        購入許可判定 に実行されるGS2-Limit のカウンターを設定
        :param open_condition_limit_counter_name: 購入許可判定 に実行されるGS2-Limit のカウンター
        :type open_condition_limit_counter_name: unicode
        :return: this
        :rtype: UpdateItemMasterRequest
        """
        self.set_open_condition_limit_counter_name(open_condition_limit_counter_name)
        return self
