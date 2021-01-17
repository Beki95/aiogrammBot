from aiogram import Dispatcher


# from .is_admin import AdminFilter
# from .admins import AdminFilter
from .is_forward import IsForward


def setup(dp: Dispatcher):
    # dp.filters_factory.bind(AdminFilter)
    # dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsForward)
    pass
