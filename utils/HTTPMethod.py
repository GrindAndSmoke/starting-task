import allure
import requests

from utils.Logger import Logger

"""List of HTTP methods"""
class Http_methods:
    # Заголовки запроса
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache': 'no-cache',
        'content-type': 'application/json; charset=UTF-8',
        'cookie': "advref=brand_search:google-; advref_first=brand_search:google-; site_version=desktop; client_timestamp=1713727832; session=b5wTaQ2KHMrBhz7BMSu6sE; _ym_uid=1713727833983355321; _ym_d=1713727833; rrpvid=59234338255588; _userGUID=0:lv9xaz7z:IOdtnC0eJrna2sdhIw4Q8ffrGZEPIuel; _gcl_au=1.1.952122739.1713727834; rcuid=65aa6341fd14d69ea8a888ae; _ga=GA1.1.989259939.1713727834; _ga=GA1.3.989259939.1713727834; cart=9lVSs2IKQe2AWXxce9jH6o; rrlevt=1713727841627; city_is_selected=1; _rc_uid=704b4eb855a6f6b2604ff850d19a2732; chkuidsrv=7d94f72c4344d9716541163d78e0b7c8; _ym_isad=1; _ym_visorc=b; digi_uc=W1sidiIsIjY0NTE1MSIsMTcxMzcyNzg0MTU2OF0sWyJjdiIsIjU1NDUzNiIsMTcxNDA2ODA4NzgxNV0sWyJjdiIsIjc1MTM1NyIsMTcxNDA0NTY4NTY5MV0sWyJjdiIsIjU0OTcxMyIsMTcxNDAwMzQ1NjgzM10sWyJjdiIsIjM3OTA0NyIsMTcxMzk5OTM0MDc2NV0sWyJjdiIsIjY0NTE1MSIsMTcxMzcyNzk3MTY4NV0sWyJjdiIsIjU4MDI0OCIsMTcxNDkwNDUyMTE3MF1d; dSesn=673775f7-b4c2-fb06-539b-69ca3d108c0d; _dvs=0:lvtdvh70:xtUk0IKeGdDdbjML6DIiZdlCw641A1bU; _gid=GA1.3.614037585.1714904522; _gat_UA-22847688-1=1; _dc_gtm_UA-22847688-1=1; telemetryToken=b5wTaQ2KHMrBhz7BMSu6sE7RMb8UIuaxAx8oC8eSsl5R; backendStart=1714904539620; backendEnd=1714904540250; system_id=2d4beea01ecda526f376b05e844ad71fz1714904539; _ga_SFTLJVK4S7=GS1.1.1714904521.9.0.1714904540.41.0.0",
        'origin': 'https://krasnoyarsk.220-volt.ru',
        'priority': 'u=1, i',
        'referer': 'https://krasnoyarsk.220-volt.ru/catalog/prozhektory/jazzway/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request'
    }

    # JSON данные для запроса
    data = {
        'pageType': 3
    }

    @staticmethod
    def post(url, body):

        with allure.step("Post"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, headers=Http_methods.headers, json=Http_methods.data)
            Logger.add_response(result)
            return result

    def put(url, body):
        with allure.step("Put"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result


    def delete(url, body):
        with allure.step("Delete"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)
            return result


