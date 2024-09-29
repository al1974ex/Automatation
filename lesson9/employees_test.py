import requests
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
      #Создать новую компанию
    name = "BSK elektrik"
    descr = "electrical installation"
    result = api.create_company(name, descr)
    new_id = result["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # получить список сотруднико до...
    body = api.get_employees_list(companyId)
    len_before = len(body)
     # добавить нового сотрудника
    firstName = "Alex"
    lastName = "Kalashnikov"
    middleName = "Vladimirovich"
    company = companyId
    email = "alex4791@yandex.ru"
    url = "string"
    phone = "890434734544"
    birthdate = "2024-09-09T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Alex"
    assert body[-1]["lastName"] == "Kalashnikov"
    assert body[-1]["middleName"] == "Vladimirovich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "890434734544"
    assert body[-1]["birthdate"] == "2024-09-09"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    #Создать новую компанию
    name = "ООО Новстрой"
    descr = "строительство"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']
    # получить список сотрудников новой компании до....
    body = api.get_employees_list(companyId)
    begin_list = len(body)
    # добавить нового сотрудника
    firstName = "olga"
    lastName = "lichovitskaja"
    middleName = "alekseevna"
    company = companyId
    email = "olga123@mail.ru"
    url = "string"
    phone = "890523175411"
    birthdate = "1987-05-06T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "olga"
    assert body[-1]["lastName"] ==  "lichovitskaja"
    assert body[-1]["middleName"] == "alekseevna"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "890523175411"
    assert body[-1]["birthdate"] == "1987-05-06"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "ИП Чистота"
    descr = "мойка"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "roman"
    lastName = "somov"
    middleName = "petrovich"
    company = companyId
    email = "somov123@mail.ru"
    url = "string"
    phone = "890323175456"
    birthdate = "2003-02-06"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Ларин"
    new_email = "somov123@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "somov123@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False