from http.client import responses

import allure
import requests
BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Pet")
class TestPet:
    @allure.title("Попытка удалить несуществующий питомца")
    def test_delete_pet(self):
        with allure.step("Отправка запроса на удаление питомца"):
            response = requests.delete(url=f"{BASE_URL}/pet/9999")
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
        with allure.step("Провекра текстового содержимо ответа"):
           assert response.text == "Pet deleted", "Текст не совпадает с ожидаемым"


    @allure.title("Обновить несуществующего питомца")
    def test_update_pet(self):
        with allure.step("Отправка запроса"):
            payload = {
                       "id":9999,
                       "name":"Pet",
                       "status":"available"
                       }
            responses = requests.put(url=f"{BASE_URL}/pet",json=payload)
        with allure.step("Проверка статус кода"):
            responses.status_code == 404,"Код ошибки не равен 404"

        with allure.step("Проверка тексат"):
            responses.text == "Pet not found"

