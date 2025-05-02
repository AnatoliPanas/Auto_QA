from uuid import uuid4
import allure
from base_requests import CompanyApi
import pytest

BASE_URL = "http://5.101.50.27:8000"
CREDS = {"username": "harrypotter", "password": "expelliarmus"}

@pytest.fixture
def api():
    return CompanyApi(BASE_URL, CREDS)

@pytest.fixture
def unique_company_info():
    return f"Anatoly&Co-{uuid4()}", "ICH"

@allure.id('ICH-1')
@allure.story('Создание одной компании по ID')
@allure.feature('CREATE')
@allure.title('Создание компании и сравнение количества')
def test_create_company(api, unique_company_info):
    name, description = unique_company_info
    companies_before = api.get_company_list()
    companies_before_count = len(companies_before)
    api.create_company(name, description)
    companies_after = api.get_company_list()
    companies_after_count = len(companies_after)
    assert companies_before_count+1 == companies_after_count

@allure.id('ICH-2')
@allure.story('Получение одной компании по ID')
@allure.feature('CREATE_ONE')
@allure.title('Создание компании, получение ID')
def test_get_one_company(api, unique_company_info):
    name, description = unique_company_info
    result = api.create_company(name, description)
    company_id = result.get("id")
    company_by_id = api.get_company(company_id)

    assert company_by_id.get("name") == name
    assert company_by_id.get("description") == description
    assert company_by_id.get("is_active") is True

@allure.id('ICH-3')
@allure.story('Удаление одной компании по ID')
@allure.feature('DELETE')
@allure.title('Удаление компании')
def test_company_delete(api, unique_company_info):
    name, description = unique_company_info
    result = api.create_company(name, description)
    company_id = result.get("id")
    api.delete_company(company_id)
    deleted = api.get_company(company_id)
    assert deleted.get('detail') == "Компания не найдена"

@allure.id('ICH-4')
@allure.story('Деактивация одной компании по ID')
@allure.feature('DEACTIVATE')
@allure.title('Деактивация компании')
def test_deactivate_company(api, unique_company_info):
    name, description = unique_company_info
    result = api.create_company(name, description)
    company_id = result.get("id")
    json_result = api.set_active_state(company_id, is_active=False)
    assert json_result.get('is_active') is False, 'Ожидался False'

@allure.id('ICH-3')
@allure.story('Удаление всех компаний по ID')
@allure.feature('DELETE')
@allure.title('Удаление всех компаний')
def test_delete_all_company(api):
    companies = api.get_company_list()
    for company in companies:
        api.delete_company(company.get('id'))

@allure.id('ICH-3')
@allure.story('Создание и удаление компании по ID')
@allure.feature('DELETE')
@allure.title('Создание и удаление компании')
def test_delete_company(api, unique_company_info):
    with allure.step('получение уникального имени компании и ее описания'):
        name, description = unique_company_info
    with allure.step('создаем компанию'):
        result = api.create_company(name, description)
    with allure.step('получаем id из ответа сервера'):
        comp_id = result.get('id')

    with allure.step('удаляем компанию'):
        api.delete_company(comp_id)
        deleted = api.get_company(comp_id)
    with allure.step('проверка того что удаленная компания не найдется в списке'):
        assert deleted['detail'] == "Компания не найдена", 'неожиданный ответ сервера'