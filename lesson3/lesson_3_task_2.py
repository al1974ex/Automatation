# lesson_3_task_2.py

from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79091234001"),
    Smartphone("Samsung", "Galaxy S22", "+79046543555"),
    Smartphone("Xiaomi", "PRO 13", "+79181234313"),
    Smartphone("Redmi", "P 16", "+79654321888"),
    Smartphone("Vertu", "9 Pro", "+79067891232"),
]


for smartphone in catalog:
    print(smartphone)