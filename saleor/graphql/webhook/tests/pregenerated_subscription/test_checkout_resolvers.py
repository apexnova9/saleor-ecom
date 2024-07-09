from datetime import timedelta
from unittest import mock

from django.test import override_settings
from django.utils import timezone

from ....core.utils import to_global_id_or_none
from ....tests.utils import get_graphql_content


@override_settings(PLUGINS=["saleor.plugins.webhook.plugin.WebhookPlugin"])
@mock.patch("saleor.webhook.transport.synchronous.transport.send_webhook_request_sync")
@mock.patch(
    "saleor.webhook.transport.synchronous.transport.generate_payload_from_subscription"
)
def test_checkout_total_price_use_pregenerated_payload(
    mock_generate_payload,
    mock_request,
    checkout,
    api_client,
    tax_data_response,
    tax_app,
):
    # given
    checkout.price_expiration = timezone.now() - timedelta(days=1)
    checkout.save()
    checkout_global_id = to_global_id_or_none(checkout)
    checkout_total_price_query = """
        query getCheckout($id: ID!) {
            checkout(id: $id) {
                id
                totalPrice {
                    net {
                        amount
                    }
                    gross {
                        amount
                    }
                }
            }
        }
    """
    variables = {"id": checkout_global_id}

    mock_request.return_value = tax_data_response

    # when
    response = api_client.post_graphql(checkout_total_price_query, variables)
    content = get_graphql_content(response)

    # then
    mock_generate_payload.assert_not_called()
    mock_request.assert_called_once()
    assert content["data"]["checkout"]["id"] == checkout_global_id


@override_settings(PLUGINS=["saleor.plugins.webhook.plugin.WebhookPlugin"])
@mock.patch("saleor.webhook.transport.synchronous.transport.send_webhook_request_sync")
@mock.patch(
    "saleor.webhook.transport.synchronous.transport.generate_payload_from_subscription"
)
def test_checkout_subtotal_price_use_pregenerated_payload(
    mock_generate_payload,
    mock_request,
    checkout,
    api_client,
    tax_data_response,
    tax_app,
):
    # given
    checkout.price_expiration = timezone.now() - timedelta(days=1)
    checkout.save()
    checkout_global_id = to_global_id_or_none(checkout)
    checkout_total_price_query = """
        query getCheckout($id: ID!) {
            checkout(id: $id) {
                id
                subtotalPrice {
                    net {
                        amount
                    }
                    gross {
                        amount
                    }
                }
            }
        }
    """
    variables = {"id": checkout_global_id}

    mock_request.return_value = tax_data_response

    # when
    response = api_client.post_graphql(checkout_total_price_query, variables)
    content = get_graphql_content(response)

    # then
    mock_generate_payload.assert_not_called()
    mock_request.assert_called_once()
    assert content["data"]["checkout"]["id"] == checkout_global_id


@override_settings(PLUGINS=["saleor.plugins.webhook.plugin.WebhookPlugin"])
@mock.patch("saleor.webhook.transport.synchronous.transport.send_webhook_request_sync")
@mock.patch(
    "saleor.webhook.transport.synchronous.transport.generate_payload_from_subscription"
)
def test_checkout_total_total_balance_use_pregenerated_payload(
    mock_generate_payload,
    mock_request,
    checkout,
    api_client,
    tax_data_response,
    tax_app,
):
    # given
    checkout.price_expiration = timezone.now() - timedelta(days=1)
    checkout.save()
    checkout_global_id = to_global_id_or_none(checkout)
    checkout_total_price_query = """
        query getCheckout($id: ID!) {
            checkout(id: $id) {
                id
                totalBalance {
                    amount
                }
            }
        }
    """
    variables = {"id": checkout_global_id}

    mock_request.return_value = tax_data_response

    # when
    response = api_client.post_graphql(checkout_total_price_query, variables)
    content = get_graphql_content(response)

    # then
    mock_generate_payload.assert_not_called()
    mock_request.assert_called_once()
    assert content["data"]["checkout"]["id"] == checkout_global_id


@override_settings(PLUGINS=["saleor.plugins.webhook.plugin.WebhookPlugin"])
@mock.patch("saleor.webhook.transport.synchronous.transport.send_webhook_request_sync")
@mock.patch(
    "saleor.webhook.transport.synchronous.transport.generate_payload_from_subscription"
)
def test_checkout_total_shipping_price_use_pregenerated_payload(
    mock_generate_payload,
    mock_request,
    checkout,
    api_client,
    tax_data_response,
    tax_app,
):
    # given
    checkout.price_expiration = timezone.now() - timedelta(days=1)
    checkout.save()
    checkout_global_id = to_global_id_or_none(checkout)
    checkout_total_price_query = """
        query getCheckout($id: ID!) {
            checkout(id: $id) {
                id
                shippingPrice{
                    net{
                        amount
                    }
                    gross{
                        amount
                    }
                    tax{
                        amount
                    }
                }
            }
        }
    """
    variables = {"id": checkout_global_id}

    mock_request.return_value = tax_data_response

    # when
    response = api_client.post_graphql(checkout_total_price_query, variables)
    content = get_graphql_content(response)

    # then
    mock_generate_payload.assert_not_called()
    mock_request.assert_called_once()
    assert content["data"]["checkout"]["id"] == checkout_global_id
