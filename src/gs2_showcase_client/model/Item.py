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


class Item(object):

    def __init__(self, params=None):
        if params is None:
            self.__showcase_item_id = None
            self.__name = None
            self.__meta = None
            self.__currency_type = None
            self.__currency_money_name = None
            self.__currency_gold_name = None
            self.__currency_consumable_item_item_pool_name = None
            self.__currency_consumable_item_name = None
            self.__currency_option = None
            self.__price = None
            self.__item_type = None
            self.__item_money_name = None
            self.__item_gold_name = None
            self.__item_stamina_stamina_pool_name = None
            self.__item_consumable_item_item_pool_name = None
            self.__item_consumable_item_item_name = None
            self.__item_amount = None
            self.__item_option = None
            self.__can_buy = None
        else:
            self.set_showcase_item_id(params['showcaseItemId'] if 'showcaseItemId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
            self.set_currency_type(params['currencyType'] if 'currencyType' in params.keys() else None)
            self.set_currency_money_name(params['currencyMoneyName'] if 'currencyMoneyName' in params.keys() else None)
            self.set_currency_gold_name(params['currencyGoldName'] if 'currencyGoldName' in params.keys() else None)
            self.set_currency_consumable_item_item_pool_name(params['currencyConsumableItemItemPoolName'] if 'currencyConsumableItemItemPoolName' in params.keys() else None)
            self.set_currency_consumable_item_name(params['currencyConsumableItemName'] if 'currencyConsumableItemName' in params.keys() else None)
            self.set_currency_option(params['currencyOption'] if 'currencyOption' in params.keys() else None)
            self.set_price(params['price'] if 'price' in params.keys() else None)
            self.set_item_type(params['itemType'] if 'itemType' in params.keys() else None)
            self.set_item_money_name(params['itemMoneyName'] if 'itemMoneyName' in params.keys() else None)
            self.set_item_gold_name(params['itemGoldName'] if 'itemGoldName' in params.keys() else None)
            self.set_item_stamina_stamina_pool_name(params['itemStaminaStaminaPoolName'] if 'itemStaminaStaminaPoolName' in params.keys() else None)
            self.set_item_consumable_item_item_pool_name(params['itemConsumableItemItemPoolName'] if 'itemConsumableItemItemPoolName' in params.keys() else None)
            self.set_item_consumable_item_item_name(params['itemConsumableItemItemName'] if 'itemConsumableItemItemName' in params.keys() else None)
            self.set_item_amount(params['itemAmount'] if 'itemAmount' in params.keys() else None)
            self.set_item_option(params['itemOption'] if 'itemOption' in params.keys() else None)
            self.set_can_buy(params['canBuy'] if 'canBuy' in params.keys() else None)

    def get_showcase_item_id(self):
        """
        陳列商品IDを取得
        :return: 陳列商品ID
        :rtype: unicode
        """
        return self.__showcase_item_id

    def set_showcase_item_id(self, showcase_item_id):
        """
        陳列商品IDを設定
        :param showcase_item_id: 陳列商品ID
        :type showcase_item_id: unicode
        """
        self.__showcase_item_id = showcase_item_id

    def get_name(self):
        """
        商品名を取得
        :return: 商品名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        商品名を設定
        :param name: 商品名
        :type name: unicode
        """
        self.__name = name

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
        self.__meta = meta

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
        self.__currency_type = currency_type

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
        self.__currency_money_name = currency_money_name

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
        self.__currency_gold_name = currency_gold_name

    def get_currency_consumable_item_item_pool_name(self):
        """
        GS2-ConsumableItem アイテムプール名を取得
        :return: GS2-ConsumableItem アイテムプール名
        :rtype: unicode
        """
        return self.__currency_consumable_item_item_pool_name

    def set_currency_consumable_item_item_pool_name(self, currency_consumable_item_item_pool_name):
        """
        GS2-ConsumableItem アイテムプール名を設定
        :param currency_consumable_item_item_pool_name: GS2-ConsumableItem アイテムプール名
        :type currency_consumable_item_item_pool_name: unicode
        """
        self.__currency_consumable_item_item_pool_name = currency_consumable_item_item_pool_name

    def get_currency_consumable_item_name(self):
        """
        GS2-ConsumableItem アイテム名を取得
        :return: GS2-ConsumableItem アイテム名
        :rtype: unicode
        """
        return self.__currency_consumable_item_name

    def set_currency_consumable_item_name(self, currency_consumable_item_name):
        """
        GS2-ConsumableItem アイテム名を設定
        :param currency_consumable_item_name: GS2-ConsumableItem アイテム名
        :type currency_consumable_item_name: unicode
        """
        self.__currency_consumable_item_name = currency_consumable_item_name

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
        self.__currency_option = currency_option

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
        self.__price = price

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
        self.__item_type = item_type

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
        self.__item_money_name = item_money_name

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
        self.__item_gold_name = item_gold_name

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
        self.__item_stamina_stamina_pool_name = item_stamina_stamina_pool_name

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
        self.__item_consumable_item_item_pool_name = item_consumable_item_item_pool_name

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
        self.__item_consumable_item_item_name = item_consumable_item_item_name

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
        self.__item_amount = item_amount

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
        self.__item_option = item_option

    def get_can_buy(self):
        """
        購入可能かを取得
        :return: 購入可能か
        :rtype: bool
        """
        return self.__can_buy

    def set_can_buy(self, can_buy):
        """
        購入可能かを設定
        :param can_buy: 購入可能か
        :type can_buy: bool
        """
        self.__can_buy = can_buy

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Item, self).__getitem__(key)

    def to_dict(self):
        return {
            "showcaseItemId": self.__showcase_item_id,
            "name": self.__name,
            "meta": self.__meta,
            "currencyType": self.__currency_type,
            "currencyMoneyName": self.__currency_money_name,
            "currencyGoldName": self.__currency_gold_name,
            "currencyConsumableItemItemPoolName": self.__currency_consumable_item_item_pool_name,
            "currencyConsumableItemName": self.__currency_consumable_item_name,
            "currencyOption": self.__currency_option,
            "price": self.__price,
            "itemType": self.__item_type,
            "itemMoneyName": self.__item_money_name,
            "itemGoldName": self.__item_gold_name,
            "itemStaminaStaminaPoolName": self.__item_stamina_stamina_pool_name,
            "itemConsumableItemItemPoolName": self.__item_consumable_item_item_pool_name,
            "itemConsumableItemItemName": self.__item_consumable_item_item_name,
            "itemAmount": self.__item_amount,
            "itemOption": self.__item_option,
            "canBuy": self.__can_buy,
        }
