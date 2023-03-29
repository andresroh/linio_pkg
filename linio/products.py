class products:

    def __init__(self,session) -> None:
        self.linio = session

    def get(self, limit=1000, **kwargs):
        """get information for one product or a product list 

        Args:
            limit (int, optional): output results 1 to 1000. Defaults to 1000.

        Returns:
            dict: product information
        """
        params = {
            "Action": "GetProducts",
            "Limit": limit
        }

        if kwargs:
            params.update(kwargs)

        return self.linio.query('get', params)

    def create(self, payload):
        """create a products

        Args:
            payload (_type_): product information

        Returns:
            dict: operation response
        """
        params = {
            "Action": "ProductCreate"
        }

        return self.linio.query('post', params, payload)

    def update(self, payload):
        """update products

        Args:
            payload (XML): product information

        Returns:
            dict: operation response
        """
        params = {
            "Action": "ProductUpdate"
        }

        return self.linio.query('post', params, payload)

    def remove(self, payload):
        """remove product

        Args:
            payload (_type_): _description_

        Returns:
            dict: operation response
        """
        params = {
            "Action": "ProductRemove"
        }

        return self.linio.query('post', params, payload)

    def brands(self):
        """search seller brands

        Returns:
            dict: seller brands
        """
        params = {
            "Action": "GetBrands"
        }

        return self.linio.query('get', params)
