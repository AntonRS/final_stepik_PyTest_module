import pytest
from .pages.product_page import ProductPage

""" 
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
 """

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)   # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # Открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page =  ProductPage(browser, link)  # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # Открываем страницу товара
    page.add_to_basket()                # Добавляем товар в корзину
    page.solve_quiz_and_get_code()      # Вводим в alert расчитанный код
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    return True

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
def test_guest_cant_see_success_message(browser, link):
    page =  ProductPage(browser, link)  # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # Открываем страницу товара
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    return True

@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page =  ProductPage(browser, link)  # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # Открываем страницу товара
    page.add_to_basket()                # Добавляем товар в корзину
    page.solve_quiz_and_get_code()      # Вводим в alert расчитанный код
    page.should_be_success_message_disappeared()               #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    return True