import pytest

from stapi_client.client import StapiClient


@pytest.mark.parametrize(
    'method,args,kwargs', [
        ('get_conformance', [], {}),
        ('get_products', [], {}),
        ('get_product', ['product-123'], {}),
        ('get_product_parameters', ['product-123'], {}),
        ('get_orders', [], {}),
        ('create_order', [], {}),
        ('get_order', ['order-456'], {}),
        ('get_order_status', ['order-456'], {}),
        ('fetch_opportunities', [], {}),
    ]
)
def test_endpoint_not_implemented(method, args, kwargs):
    sc = StapiClient()
    with pytest.raises(NotImplementedError):
        getattr(sc, method)(*args, **kwargs)
