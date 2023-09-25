import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 201
    assert response.json()["authToken"] != ""


def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400


def test_create_user_1_russian_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_create_user_2_english_letter_in_name_get_success_response():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc")
    positive_assert(kit_body)

def test_create_user_3_symbols_letter_in_name_get_success_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_create_user_4_symbols_letter_in_name_get_success_response():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd")
    negative_assert_code_400(kit_body)

def test_create_user_5_english_letter_in_name_get_success_response():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

def test_create_user_6_russian_letter_in_name_get_success_response():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

def test_create_user_7_special_symbols_letter_in_name_get_success_response():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert(kit_body)

def test_create_user_8_special_symbols_letter_in_name_get_success_response():
    kit_body = get_kit_body("Человек и КО")
    positive_assert(kit_body)

def test_create_user_9_numbers_letter_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_create_user_10_parameter_not_passed_letter_in_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

def test_create_user_11_another_parameter_passed_letter_in_name_get_success_response():
    kit_body = data.kit_body.copy(123)
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400


