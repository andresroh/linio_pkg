class orders:

    def __init__(self, session) -> None:

        self.linio = session

    def list(self, **kwargs):
        """search a orders list

        Returns:
            dict: orders list
        """

        params = {
            "Action": "GetOrders"
        }

        if kwargs:
            params.update(kwargs)

        return self.linio.query('get', params)

    def get(self, order_id, **kwargs):
        """search order information

        Args:
            order_id (int): order id

        Returns:
            dict: return order information
        """
        params = {
            "Action": "GetOrder",
            "OrderId": order_id
        }

        if kwargs:
            params.update(kwargs)

        return self.linio.query('get', params)

    def items(self, order_id, template="JSON"):
        """search items from an order

        Args:
            order_id (int): order id
            template (str, optional): output formart. Defaults to "JSON".

        Returns:
            dict: return items from an order
        """
        params = {
            "Action": "GetOrderItems",
            "OrderId": order_id,
            "Format": template
        }

        return self.linio.query('get', params)

    def multiple_order_items(self, order_id_list, template="JSON"):
        """search items from an order list

        Args:
            order_id_list (list): order list
            template (str, optional): output formart. Defaults to "JSON".

        Returns:
            dict: return items from an order
        """
        params = {
            "Action": "GetMultipleOrderItems",
            "Format": template,
            "OrderIdList": order_id_list
        }

        return self.linio.query('get', params)
