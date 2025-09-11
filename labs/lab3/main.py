#!/usr/bin/env python3

# Title:        main.py
# Description:  Lab3
# Author:       Chris Taylor (m276342)

import requests

url = "https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery"

data = {
    "P_ALPHA": "276342",
    "P_LAST_NAME": "",
    "P_MICO_CO_NBR": "",
    "P_SECOF_COOF_SEBLDA_AC_YR": "2026",
    "P_SECOF_COOF_SEBLDA_SEM": "FALL",
    "P_SECOF_COOF_SEBLDA_BLK_NBR": "1",
    "P_MAJOR_CODE": "",
    "P_NOMI_FORMATTED_NAME": "",
    "Z_ACTION": "QUERY",
    "Z_CHK": "0",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://mids.usna.edu",
    "Referer": "https://mids.usna.edu/ITSD/mids/drgwq010$.startup",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
}

cookies = {
    "f5_cspm": "1234",
    "WSG$DRGWQ010$URL0": "/ITSD/mids/drgwq010$.startup",
    "WSG$DRGWQ010$CAP0": "Schedules_-_Query_Midshipmen",
    "_ga": "GA1.1.205993241.1719338122",
    "nmstat": "751f859d-6290-a9c1-4c78-b366919ffe78",
    "_ga_LY79N0FLBS": "GS2.1.s1757592475",
}

resp = requests.post(url, headers=headers, cookies=cookies, data=data)
print(resp.status_code)
print(resp.text[:500])
