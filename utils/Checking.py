import json

from requests import Response


class Checking():

    """Methods for checking status code changes"""

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Success!!! Status code = :" + str(result.status_code))

    """Methods for Checking tokens"""
    @staticmethod
    def cheking_json_token(result, expected_value):
        token = json.loads(result.text)
        assert set(token) == set(expected_value)
        print("Success!!! values exist")

    """Methods for checking """
    @staticmethod
    def check_json_values(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert expected_value == check_info
        print("Success!!! " + str(field_name) + " = :" + str(check_info))
