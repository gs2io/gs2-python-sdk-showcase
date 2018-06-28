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

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2ShowcaseClient(AbstractGs2Client):

    ENDPOINT = "showcase"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2ShowcaseClient, self).__init__(credential, region)

    def get_current_showcase_master(self, request):
        """
        公開されているショーケースマスタを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.GetCurrentShowcaseMasterRequest.GetCurrentShowcaseMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.GetCurrentShowcaseMasterResult.GetCurrentShowcaseMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.GetCurrentShowcaseMasterRequest import GetCurrentShowcaseMasterRequest

        from gs2_showcase_client.control.GetCurrentShowcaseMasterResult import GetCurrentShowcaseMasterResult
        return GetCurrentShowcaseMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/item/master",
            service=self.ENDPOINT,
            component=GetCurrentShowcaseMasterRequest.Constant.MODULE,
            target_function=GetCurrentShowcaseMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_current_showcase_master(self, request):
        """
        公開するショーケースマスタを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.UpdateCurrentShowcaseMasterRequest.UpdateCurrentShowcaseMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.UpdateCurrentShowcaseMasterResult.UpdateCurrentShowcaseMasterResult
        """
        body = { 
            "settings": request.get_settings(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.UpdateCurrentShowcaseMasterRequest import UpdateCurrentShowcaseMasterRequest
        from gs2_showcase_client.control.UpdateCurrentShowcaseMasterResult import UpdateCurrentShowcaseMasterResult
        return UpdateCurrentShowcaseMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/item/master",
            service=self.ENDPOINT,
            component=UpdateCurrentShowcaseMasterRequest.Constant.MODULE,
            target_function=UpdateCurrentShowcaseMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_item_group_master(self, request):
        """
        商品グループを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.CreateItemGroupMasterRequest.CreateItemGroupMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.CreateItemGroupMasterResult.CreateItemGroupMasterResult
        """
        body = { 
            "name": request.get_name(),
            "itemNames": request.get_item_names(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.CreateItemGroupMasterRequest import CreateItemGroupMasterRequest
        from gs2_showcase_client.control.CreateItemGroupMasterResult import CreateItemGroupMasterResult
        return CreateItemGroupMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/itemGroup",
            service=self.ENDPOINT,
            component=CreateItemGroupMasterRequest.Constant.MODULE,
            target_function=CreateItemGroupMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_item_group_master(self, request):
        """
        商品グループを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DeleteItemGroupMasterRequest.DeleteItemGroupMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DeleteItemGroupMasterRequest import DeleteItemGroupMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/itemGroup/" + str(("null" if request.get_item_group_name() is None or request.get_item_group_name() == "" else url_encoder.encode(request.get_item_group_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteItemGroupMasterRequest.Constant.MODULE,
            target_function=DeleteItemGroupMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_item_group_master(self, request):
        """
        商品グループの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DescribeItemGroupMasterRequest.DescribeItemGroupMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.DescribeItemGroupMasterResult.DescribeItemGroupMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DescribeItemGroupMasterRequest import DescribeItemGroupMasterRequest

        from gs2_showcase_client.control.DescribeItemGroupMasterResult import DescribeItemGroupMasterResult
        return DescribeItemGroupMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/itemGroup",
            service=self.ENDPOINT,
            component=DescribeItemGroupMasterRequest.Constant.MODULE,
            target_function=DescribeItemGroupMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_item_group_master(self, request):
        """
        商品グループを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.GetItemGroupMasterRequest.GetItemGroupMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.GetItemGroupMasterResult.GetItemGroupMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.GetItemGroupMasterRequest import GetItemGroupMasterRequest

        from gs2_showcase_client.control.GetItemGroupMasterResult import GetItemGroupMasterResult
        return GetItemGroupMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/itemGroup/" + str(("null" if request.get_item_group_name() is None or request.get_item_group_name() == "" else url_encoder.encode(request.get_item_group_name()))) + "",
            service=self.ENDPOINT,
            component=GetItemGroupMasterRequest.Constant.MODULE,
            target_function=GetItemGroupMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_item_group_master(self, request):
        """
        商品グループを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.UpdateItemGroupMasterRequest.UpdateItemGroupMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.UpdateItemGroupMasterResult.UpdateItemGroupMasterResult
        """
        body = { 
            "itemNames": request.get_item_names(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.UpdateItemGroupMasterRequest import UpdateItemGroupMasterRequest
        from gs2_showcase_client.control.UpdateItemGroupMasterResult import UpdateItemGroupMasterResult
        return UpdateItemGroupMasterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/itemGroup/" + str(("null" if request.get_item_group_name() is None or request.get_item_group_name() == "" else url_encoder.encode(request.get_item_group_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateItemGroupMasterRequest.Constant.MODULE,
            target_function=UpdateItemGroupMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_item_master(self, request):
        """
        商品を新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.CreateItemMasterRequest.CreateItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.CreateItemMasterResult.CreateItemMasterResult
        """
        body = { 
            "name": request.get_name(),
            "currencyType": request.get_currency_type(),
            "price": request.get_price(),
            "itemType": request.get_item_type(),
            "itemAmount": request.get_item_amount(),
        }

        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        if request.get_currency_money_name() is not None:
            body["currencyMoneyName"] = request.get_currency_money_name()
        if request.get_currency_gold_name() is not None:
            body["currencyGoldName"] = request.get_currency_gold_name()
        if request.get_currency_option() is not None:
            body["currencyOption"] = request.get_currency_option()
        if request.get_item_money_name() is not None:
            body["itemMoneyName"] = request.get_item_money_name()
        if request.get_item_gold_name() is not None:
            body["itemGoldName"] = request.get_item_gold_name()
        if request.get_item_stamina_stamina_pool_name() is not None:
            body["itemStaminaStaminaPoolName"] = request.get_item_stamina_stamina_pool_name()
        if request.get_item_consumable_item_item_pool_name() is not None:
            body["itemConsumableItemItemPoolName"] = request.get_item_consumable_item_item_pool_name()
        if request.get_item_consumable_item_item_name() is not None:
            body["itemConsumableItemItemName"] = request.get_item_consumable_item_item_name()
        if request.get_item_option() is not None:
            body["itemOption"] = request.get_item_option()
        if request.get_open_condition_type() is not None:
            body["openConditionType"] = request.get_open_condition_type()
        if request.get_open_condition_limit_name() is not None:
            body["openConditionLimitName"] = request.get_open_condition_limit_name()
        if request.get_open_condition_limit_counter_name() is not None:
            body["openConditionLimitCounterName"] = request.get_open_condition_limit_counter_name()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.CreateItemMasterRequest import CreateItemMasterRequest
        from gs2_showcase_client.control.CreateItemMasterResult import CreateItemMasterResult
        return CreateItemMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/item",
            service=self.ENDPOINT,
            component=CreateItemMasterRequest.Constant.MODULE,
            target_function=CreateItemMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_item_master(self, request):
        """
        商品を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DeleteItemMasterRequest.DeleteItemMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DeleteItemMasterRequest import DeleteItemMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteItemMasterRequest.Constant.MODULE,
            target_function=DeleteItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_item_master(self, request):
        """
        商品の一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DescribeItemMasterRequest.DescribeItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.DescribeItemMasterResult.DescribeItemMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DescribeItemMasterRequest import DescribeItemMasterRequest

        from gs2_showcase_client.control.DescribeItemMasterResult import DescribeItemMasterResult
        return DescribeItemMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/item",
            service=self.ENDPOINT,
            component=DescribeItemMasterRequest.Constant.MODULE,
            target_function=DescribeItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_item_master(self, request):
        """
        商品を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.GetItemMasterRequest.GetItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.GetItemMasterResult.GetItemMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.GetItemMasterRequest import GetItemMasterRequest

        from gs2_showcase_client.control.GetItemMasterResult import GetItemMasterResult
        return GetItemMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=GetItemMasterRequest.Constant.MODULE,
            target_function=GetItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_item_master(self, request):
        """
        商品を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.UpdateItemMasterRequest.UpdateItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.UpdateItemMasterResult.UpdateItemMasterResult
        """
        body = { 
            "currencyType": request.get_currency_type(),
            "price": request.get_price(),
            "itemType": request.get_item_type(),
            "itemAmount": request.get_item_amount(),
        }
        if request.get_meta() is not None:
            body["meta"] = request.get_meta()
        if request.get_currency_money_name() is not None:
            body["currencyMoneyName"] = request.get_currency_money_name()
        if request.get_currency_gold_name() is not None:
            body["currencyGoldName"] = request.get_currency_gold_name()
        if request.get_currency_option() is not None:
            body["currencyOption"] = request.get_currency_option()
        if request.get_item_money_name() is not None:
            body["itemMoneyName"] = request.get_item_money_name()
        if request.get_item_gold_name() is not None:
            body["itemGoldName"] = request.get_item_gold_name()
        if request.get_item_stamina_stamina_pool_name() is not None:
            body["itemStaminaStaminaPoolName"] = request.get_item_stamina_stamina_pool_name()
        if request.get_item_consumable_item_item_pool_name() is not None:
            body["itemConsumableItemItemPoolName"] = request.get_item_consumable_item_item_pool_name()
        if request.get_item_consumable_item_item_name() is not None:
            body["itemConsumableItemItemName"] = request.get_item_consumable_item_item_name()
        if request.get_item_option() is not None:
            body["itemOption"] = request.get_item_option()
        if request.get_open_condition_type() is not None:
            body["openConditionType"] = request.get_open_condition_type()
        if request.get_open_condition_limit_name() is not None:
            body["openConditionLimitName"] = request.get_open_condition_limit_name()
        if request.get_open_condition_limit_counter_name() is not None:
            body["openConditionLimitCounterName"] = request.get_open_condition_limit_counter_name()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.UpdateItemMasterRequest import UpdateItemMasterRequest
        from gs2_showcase_client.control.UpdateItemMasterResult import UpdateItemMasterResult
        return UpdateItemMasterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateItemMasterRequest.Constant.MODULE,
            target_function=UpdateItemMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def buy_item(self, request):
        """
        購入処理を実行完了する為に必要となるスタンプシートを取得します。<br>
        スタンプシートの詳細は GS2 ドキュメントを参照してください。<br>
        <br>
        このAPIによって払い出されるスタンプシートが要求するタスクは以下のアクションの可能性があります。<br>
        <br>
        Gs2Money:VerifyByStampTask<br>
        Gs2Money:ConsumeWalletByStampTask<br>
        Gs2Gold:WithdrawFromWalletByStampTask<br>
        Gs2Stamina:ConsumeStaminaByStampTask<br>
        Gs2ConsumableItem:ConsumeInventoryByStampTask<br>
        Gs2Limit:UpCounterByStampTask<br>
        <br>
        このAPIによって払い出されるスタンプシートの完了は以下のアクションの可能性があります。<br>
        <br>
        Gs2Money:ChargeWalletByStampSheet<br>
        Gs2Gold:DepositIntoWalletByStampSheet<br>
        Gs2Stamina:ChangeStaminaByStampSheet<br>
        Gs2ConsumableItem:AcquisitionInventoryByStampSheet<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.BuyItemRequest.BuyItemRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.BuyItemResult.BuyItemResult
        """
        body = { 
            "keyName": request.get_key_name(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.BuyItemRequest import BuyItemRequest
        from gs2_showcase_client.control.BuyItemResult import BuyItemResult
        return BuyItemResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/item/" + str(("null" if request.get_showcase_item_id() is None or request.get_showcase_item_id() == "" else url_encoder.encode(request.get_showcase_item_id()))) + "",
            service=self.ENDPOINT,
            component=BuyItemRequest.Constant.MODULE,
            target_function=BuyItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def describe_item(self, request):
        """
        陳列されている商品一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DescribeItemRequest.DescribeItemRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.DescribeItemResult.DescribeItemResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DescribeItemRequest import DescribeItemRequest

        from gs2_showcase_client.control.DescribeItemResult import DescribeItemResult
        return DescribeItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/item",
            service=self.ENDPOINT,
            component=DescribeItemRequest.Constant.MODULE,
            target_function=DescribeItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_item(self, request):
        """
        陳列されている商品を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.GetItemRequest.GetItemRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.GetItemResult.GetItemResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.GetItemRequest import GetItemRequest

        from gs2_showcase_client.control.GetItemResult import GetItemResult
        return GetItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/item/" + str(("null" if request.get_showcase_item_id() is None or request.get_showcase_item_id() == "" else url_encoder.encode(request.get_showcase_item_id()))) + "",
            service=self.ENDPOINT,
            component=GetItemRequest.Constant.MODULE,
            target_function=GetItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def export_master(self, request):
        """
        ショーケースマスターデータをエクスポートする<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.ExportMasterRequest.ExportMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.ExportMasterResult.ExportMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.ExportMasterRequest import ExportMasterRequest

        from gs2_showcase_client.control.ExportMasterResult import ExportMasterResult
        return ExportMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master",
            service=self.ENDPOINT,
            component=ExportMasterRequest.Constant.MODULE,
            target_function=ExportMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def create_showcase_item_master(self, request):
        """
        陳列商品を新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.CreateShowcaseItemMasterRequest.CreateShowcaseItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.CreateShowcaseItemMasterResult.CreateShowcaseItemMasterResult
        """
        body = { 
            "category": request.get_category(),
            "priority": request.get_priority(),
        }

        if request.get_item_name() is not None:
            body["itemName"] = request.get_item_name()
        if request.get_item_group_name() is not None:
            body["itemGroupName"] = request.get_item_group_name()
        if request.get_release_condition_type() is not None:
            body["releaseConditionType"] = request.get_release_condition_type()
        if request.get_release_condition_schedule_name() is not None:
            body["releaseConditionScheduleName"] = request.get_release_condition_schedule_name()
        if request.get_release_condition_schedule_event_name() is not None:
            body["releaseConditionScheduleEventName"] = request.get_release_condition_schedule_event_name()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.CreateShowcaseItemMasterRequest import CreateShowcaseItemMasterRequest
        from gs2_showcase_client.control.CreateShowcaseItemMasterResult import CreateShowcaseItemMasterResult
        return CreateShowcaseItemMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/showcaseItem",
            service=self.ENDPOINT,
            component=CreateShowcaseItemMasterRequest.Constant.MODULE,
            target_function=CreateShowcaseItemMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_showcase_item_master(self, request):
        """
        陳列商品を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DeleteShowcaseItemMasterRequest.DeleteShowcaseItemMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DeleteShowcaseItemMasterRequest import DeleteShowcaseItemMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/showcaseItem/" + str(("null" if request.get_category() is None or request.get_category() == "" else url_encoder.encode(request.get_category()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "",
            service=self.ENDPOINT,
            component=DeleteShowcaseItemMasterRequest.Constant.MODULE,
            target_function=DeleteShowcaseItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_showcase_item_master(self, request):
        """
        陳列商品の一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DescribeShowcaseItemMasterRequest.DescribeShowcaseItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.DescribeShowcaseItemMasterResult.DescribeShowcaseItemMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DescribeShowcaseItemMasterRequest import DescribeShowcaseItemMasterRequest

        from gs2_showcase_client.control.DescribeShowcaseItemMasterResult import DescribeShowcaseItemMasterResult
        return DescribeShowcaseItemMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/showcaseItem",
            service=self.ENDPOINT,
            component=DescribeShowcaseItemMasterRequest.Constant.MODULE,
            target_function=DescribeShowcaseItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_showcase_item_master(self, request):
        """
        陳列商品を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.GetShowcaseItemMasterRequest.GetShowcaseItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.GetShowcaseItemMasterResult.GetShowcaseItemMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.GetShowcaseItemMasterRequest import GetShowcaseItemMasterRequest

        from gs2_showcase_client.control.GetShowcaseItemMasterResult import GetShowcaseItemMasterResult
        return GetShowcaseItemMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/showcaseItem/" + str(("null" if request.get_category() is None or request.get_category() == "" else url_encoder.encode(request.get_category()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "",
            service=self.ENDPOINT,
            component=GetShowcaseItemMasterRequest.Constant.MODULE,
            target_function=GetShowcaseItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_showcase_item_master(self, request):
        """
        陳列商品を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.UpdateShowcaseItemMasterRequest.UpdateShowcaseItemMasterRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.UpdateShowcaseItemMasterResult.UpdateShowcaseItemMasterResult
        """
        body = { 
            "releaseConditionType": request.get_release_condition_type(),
            "priority": request.get_priority(),
        }
        if request.get_release_condition_schedule_name() is not None:
            body["releaseConditionScheduleName"] = request.get_release_condition_schedule_name()
        if request.get_release_condition_schedule_event_name() is not None:
            body["releaseConditionScheduleEventName"] = request.get_release_condition_schedule_event_name()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.UpdateShowcaseItemMasterRequest import UpdateShowcaseItemMasterRequest
        from gs2_showcase_client.control.UpdateShowcaseItemMasterResult import UpdateShowcaseItemMasterResult
        return UpdateShowcaseItemMasterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/master/showcaseItem/" + str(("null" if request.get_category() is None or request.get_category() == "" else url_encoder.encode(request.get_category()))) + "/" + str(("null" if request.get_resource_id() is None or request.get_resource_id() == "" else url_encoder.encode(request.get_resource_id()))) + "",
            service=self.ENDPOINT,
            component=UpdateShowcaseItemMasterRequest.Constant.MODULE,
            target_function=UpdateShowcaseItemMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_showcase(self, request):
        """
        ショーケースを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.CreateShowcaseRequest.CreateShowcaseRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.CreateShowcaseResult.CreateShowcaseResult
        """
        body = { 
            "name": request.get_name(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_release_condition_trigger_script() is not None:
            body["releaseConditionTriggerScript"] = request.get_release_condition_trigger_script()
        if request.get_buy_trigger_script() is not None:
            body["buyTriggerScript"] = request.get_buy_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.CreateShowcaseRequest import CreateShowcaseRequest
        from gs2_showcase_client.control.CreateShowcaseResult import CreateShowcaseResult
        return CreateShowcaseResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase",
            service=self.ENDPOINT,
            component=CreateShowcaseRequest.Constant.MODULE,
            target_function=CreateShowcaseRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_showcase(self, request):
        """
        ショーケースを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DeleteShowcaseRequest.DeleteShowcaseRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DeleteShowcaseRequest import DeleteShowcaseRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteShowcaseRequest.Constant.MODULE,
            target_function=DeleteShowcaseRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_showcase(self, request):
        """
        ショーケースの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.DescribeShowcaseRequest.DescribeShowcaseRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.DescribeShowcaseResult.DescribeShowcaseResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.DescribeShowcaseRequest import DescribeShowcaseRequest

        from gs2_showcase_client.control.DescribeShowcaseResult import DescribeShowcaseResult
        return DescribeShowcaseResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase",
            service=self.ENDPOINT,
            component=DescribeShowcaseRequest.Constant.MODULE,
            target_function=DescribeShowcaseRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_showcase(self, request):
        """
        ショーケースを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.GetShowcaseRequest.GetShowcaseRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.GetShowcaseResult.GetShowcaseResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.GetShowcaseRequest import GetShowcaseRequest

        from gs2_showcase_client.control.GetShowcaseResult import GetShowcaseResult
        return GetShowcaseResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "",
            service=self.ENDPOINT,
            component=GetShowcaseRequest.Constant.MODULE,
            target_function=GetShowcaseRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_showcase_status(self, request):
        """
        ショーケースの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.GetShowcaseStatusRequest.GetShowcaseStatusRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.GetShowcaseStatusResult.GetShowcaseStatusResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.GetShowcaseStatusRequest import GetShowcaseStatusRequest

        from gs2_showcase_client.control.GetShowcaseStatusResult import GetShowcaseStatusResult
        return GetShowcaseStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "/status",
            service=self.ENDPOINT,
            component=GetShowcaseStatusRequest.Constant.MODULE,
            target_function=GetShowcaseStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_showcase(self, request):
        """
        ショーケースを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_showcase_client.control.UpdateShowcaseRequest.UpdateShowcaseRequest
        :return: 結果
        :rtype: gs2_showcase_client.control.UpdateShowcaseResult.UpdateShowcaseResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_release_condition_trigger_script() is not None:
            body["releaseConditionTriggerScript"] = request.get_release_condition_trigger_script()
        if request.get_buy_trigger_script() is not None:
            body["buyTriggerScript"] = request.get_buy_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_showcase_client.control.UpdateShowcaseRequest import UpdateShowcaseRequest
        from gs2_showcase_client.control.UpdateShowcaseResult import UpdateShowcaseResult
        return UpdateShowcaseResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/showcase/" + str(("null" if request.get_showcase_name() is None or request.get_showcase_name() == "" else url_encoder.encode(request.get_showcase_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateShowcaseRequest.Constant.MODULE,
            target_function=UpdateShowcaseRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))
