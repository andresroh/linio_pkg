# LinioPy

Este módulo permite interactuar con el API de Linio para leer, actualizar y crear productos, órdenes y datos de clientes. Este módulo es útil para integrar el API de Linio con otros sistemas.

## Instalación

Para instalar este módulo, ejecute el siguiente comando:

```bash
pip install liniopy
```

Uso básico
Para usar este módulo, primero debe obtener las credenciales de acceso al API de Linio desde el [sellercenter](https://sellercenter.linio.com.co/), en la sección de congifuración general > administrar usuarios

```python
from linio import products, orders, linio

# login

session = linio(user,key)

# Inquire about a product
 
items = products(session)

product_list = ["TP-19100"]

print(items.get(SkuSellerList=json.dumps(product_list)))

# Inquire about an order

purchase = orders(session)

print(purchase.get(11073979))
```

## Créditos

Camilo Andrés Rodriguez

## referencias

https://developers.falabella.com/

## Licencia

Este proyecto está bajo la Licencia [MIT].