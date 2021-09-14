class Header:
    class search_bar:
        input_search = {'xpath': '//div[@class="f9j4"]/input'}
        clear_search = {'class_name': 'f9j7'}

        select_category = {'xpath': '//span[@class="g0g3"]'}
        category_items = {'xpath': '//div[@class="g0a6"]/div[text()]'}

        selected_category = {'xpath': '//div[@class="g0g0 g0g1"]/span[@title]'}
        search_suggestions = {'xpath': '//section[@data-widget="searchSuggestions"]//a'}
        search_history = {'xpath': ''}
