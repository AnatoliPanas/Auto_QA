from base_requests import CompanyApi

base_url = "http://5.101.50.27:8000"
creds = {"username": "harrypotter", "password": "expelliarmus"}


def test_create_company():
    api = CompanyApi(base_url, creds)
    companies_before = api.get_company_list()
    companies_before_count = len(companies_before)
    api.create_company("Anatoli&Co", "ICH")
    companies_after = api.get_company_list()
    companies_after_count = len(companies_after)

    assert companies_before_count+1 == companies_after_count

def test_get_one_compony():
    api = CompanyApi(base_url, creds)
    result = api.create_company("Anatoli&Co v5", "ICH")
    company_id = result.get("id")
    company_by_id = api.get_company(company_id)

    assert company_by_id.get("name") == "Anatoli&Co v5"
    assert company_by_id.get("description") == "ICH"
    assert company_by_id.get("is_active") is True

def test_company_delete():
    api = CompanyApi(base_url, creds)
    result = api.create_company("Anatoli&Co v6", "ICH")
    company_id = result.get("id")
    api.delete_company(company_id)
    deleted = api.get_company(company_id)
    assert deleted['detail'] == "Компания не найдена"

