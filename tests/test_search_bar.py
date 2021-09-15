from page_objects import SearchBarPage


def test_search_popup_is_displayed(driver):
    page = SearchBarPage(driver)
    page.get(url='https://ozon.ru')
    page.search_bar.click()
    assert page.search_suggestions.element_is_displayed() == True, 'Search popup is not displayed'
