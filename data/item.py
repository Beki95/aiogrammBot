from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.items import Item

Tesla_model_S = Item(
    title="Tesla model S",
    description="dslknfk;dsnvjfkdsvnfdv",
    start_parameter="tesla_model_s_start",
    currency="RUB",
    prices=[
        LabeledPrice(
            "Tesla_model_s Купи срочно",
            amount=10_000_00
        )
    ],
    payload="123234",
    photo_url="https://110km.ru/attachment/9bef71e81d7da1df881ba957df2e12187a480b2f/6720421acca7ce1cef1cdee2dd3ca9a7.jpg",
    need_shipping_address=True,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(
    id="post_reg",
    title="Обычная доставка",
    prices=[
        types.LabeledPrice(
            "Обычная коробка", 500_00
        )
    ]
)

POST_FAST_SHIPPING = types.ShippingOption(
    id="fast",
    title="Быстрая доставка",
    prices=[
        types.LabeledPrice(
            "Быстрая доставка (3 дней)", 3000_00
        )
    ]
)

PICUP = types.ShippingOption(
    id="picup",
    title="Самовывоз",
    prices=[
        types.LabeledPrice(
            "Самовывоз", -500_00
        )
    ]
)

