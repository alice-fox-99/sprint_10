import configuration
import requests
import data

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=kit_body,
                         headers=data.headers)


response = post_new_client_kit(data.kit_body)
print(response.status_code)
