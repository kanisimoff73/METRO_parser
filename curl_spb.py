import requests

cookies = {
    '_slid_server': '65291529e9350a001307f18d',
    'metroStoreId': '15',
    '_slid': '65291529e9350a001307f18d',
    '_ga': 'GA1.1.202942623.1697191211',
    '_ym_uid': '1697191212672075593',
    '_ym_d': '1697191212',
    'metro_user_id': '25248f82f1118d901722dcb91dfe51f7',
    'uxs_uid': '4cc77f40-69af-11ee-b26f-092bce132afb',
    '_gcl_au': '1.1.1859906898.1697191213',
    'tmr_lvid': '1a5d545c54a9099afbdd30b24b05e1b4',
    'tmr_lvidTS': '1697191212628',
    'flocktory-uuid': '3b4ec47c-0a53-413f-8793-64285100f6e1-7',
    'mindboxDeviceUUID': '9df2fcbc-5d9d-4722-aee1-a47b0c3f106b',
    'directCrm-session': '%7B%22deviceGuid%22%3A%229df2fcbc-5d9d-4722-aee1-a47b0c3f106b%22%7D',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '_slid_server': '65291529e9350a001307f18d',
    'is18Confirmed': 'true',
    '_ym_isad': '1',
    'exp_auth': '3Rd5fv0vTUylyTasdzAcqA.1',
    '_slsession': '531D0D61-1ACF-4775-A2E8-F69F5462C0CF',
    '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1697302958%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1697302958%3B6490039afadf0f1d430966df%3A64e35a6b6c71a1d5090937fb%3A1697278042',
    '_ym_visorc': 'b',
    'tmr_detect': '1%7C1697295762683',
    '_ga_VHKD93V3FV': 'GS1.1.1697295751.7.1.1697295903.0.0.0',
}

headers = {
    'authority': 'online.metro-cc.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_slid_server=65291529e9350a001307f18d; metroStoreId=10; _slid=65291529e9350a001307f18d; _ga=GA1.1.202942623.1697191211; _ym_uid=1697191212672075593; _ym_d=1697191212; metro_user_id=25248f82f1118d901722dcb91dfe51f7; uxs_uid=4cc77f40-69af-11ee-b26f-092bce132afb; _gcl_au=1.1.1859906898.1697191213; tmr_lvid=1a5d545c54a9099afbdd30b24b05e1b4; tmr_lvidTS=1697191212628; flocktory-uuid=3b4ec47c-0a53-413f-8793-64285100f6e1-7; mindboxDeviceUUID=9df2fcbc-5d9d-4722-aee1-a47b0c3f106b; directCrm-session=%7B%22deviceGuid%22%3A%229df2fcbc-5d9d-4722-aee1-a47b0c3f106b%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _slid_server=65291529e9350a001307f18d; is18Confirmed=true; _ym_isad=1; exp_auth=3Rd5fv0vTUylyTasdzAcqA.1; _slsession=531D0D61-1ACF-4775-A2E8-F69F5462C0CF; _slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1697302958%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1697302958%3B6490039afadf0f1d430966df%3A64e35a6b6c71a1d5090937fb%3A1697278042; _ym_visorc=b; tmr_detect=1%7C1697295762683; _ga_VHKD93V3FV=GS1.1.1697295751.7.1.1697295903.0.0.0',
    'if-none-match': '"1e5031-4lW6J2g/LPmKbRll8iqLlhQ0UoA"',
    'referer': 'https://docs.google.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

response = requests.get(
    url='https://online.metro-cc.ru/category/sladosti-chipsy-sneki/shokolad-batonchiki',
    cookies=cookies,
    headers=headers,
)
