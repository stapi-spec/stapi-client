class StapiClient:

    # The following methods provide access to the endpoints defined in:
    # https://github.com/stapi-spec/stapi-spec/blob/main/README.md#stapi-description
    # For now, method parameters are left intentionally sparse/undefined,
    # and output types have been omitted.

    # CONFORMANCE

    def get_conformance(self):
        raise NotImplementedError()

    # PRODUCTS

    def get_products(self):
        raise NotImplementedError()

    def get_product(self, product_id: str):
        raise NotImplementedError()

    def get_product_parameters(self, product_id: str):
        raise NotImplementedError()

    # ORDERS

    def get_orders(self):
        raise NotImplementedError()

    def create_order(self, *args, **kwargs):
        raise NotImplementedError()

    def get_order(self, order_id: str):
        raise NotImplementedError()

    def get_order_status(self, order_id: str):
        raise NotImplementedError()

    # OPPORTUNITIES

    def fetch_opportunities(self, *args, **kwargs):
        raise NotImplementedError()
