from address import Address
from mailing import Mailing


to_address = Address("123456", "Москва", "Тверская", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Невский", "12", "7")


mailing_instance = Mailing(to_address, from_address, cost=450.75, track="TRACK123456")


print(mailing_instance)