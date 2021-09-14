from page_objects import SearchBarPage


def test_select_search_category(driver):
    category = 'Книги'
    page = SearchBarPage(driver)
    page.get(url='https://ozon.ru')
    page.select_search_category(category=category)
    assert page.type_category() == category, 'Категория не выбрана'
