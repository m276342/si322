#!/usr/bin/env python3

# Title:        main.py
# Description:  Lab3
# Author:       Chris Taylor (m276342)

import requests

url = "https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery"

alpha = input("Enter Alpha: ")

data = {
    "P_ALPHA": f"{alpha}",
    "P_LAST_NAME": "",
    "P_MICO_CO_NBR": "",
    "P_SECOF_COOF_SEBLDA_AC_YR": "2026",
    "P_SECOF_COOF_SEBLDA_SEM": "FALL",
    "P_SECOF_COOF_SEBLDA_BLK_NBR": "1",
    "P_MAJOR_CODE": "",
    "P_NOMI_FORMATTED_NAME": "",
    "Z_ACTION": "QUERY",
    "Z_CHK": "0"
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
    "Cookie" : "f5_cspm=1234; WSG$DRGWQ010$URL0=/ITSD/mids/drgwq010$.startup; WSG$DRGWQ010$CAP0=Schedules_-_Query_Midshipmen; WSG$DRGWQ010$URL2=/ITSD/mids/drgwq010$mids.queryview?K_MIDS_ID=77049&K_SECOF_ID=200613&P_ALPHA=&P_LAST_NAME=&P_MICO_CO_NBR=&P_SECOF_COOF_SEBLDA_AC_YR=&P_SECOF_COOF_SEBLDA_SEM=&P_SECOF_COOF_SEBLDA_BLK_NBR=&P_MAJOR_CODE=&P_NOMI_FORMATTED_NAME=&Z_EXECUTE_QUERY=&Z_START=1&Z_ACTION=&Z_CHK=16758; WSG$DRGWQ010$CAP2=Schedule; f5avraaaaaaaaaaaaaaaa_session_=MEPLMIGBCPIBPGKNGHMOEEDGKAHDADIOCCFGHBGPEGFHNKMHBLCCNNAJFFBIMIFKNHLDNNEPJJDECBLNDLJACLDMAMMLGEAJNOLEABDEHILFDHDLDOBBMCLBHMJEFPGJ; _ga=GA1.1.205993241.1719338122; nmstat=751f859d-6290-a9c1-4c78-b366919ffe78; _ga_LY79N0FLBS=GS2.1.s1757592475$o3$g1$t1757593391$j60$l0$h0; _gid=GA1.2.1281845804.1757592476; BIGipServermids_prod=!ft8exm7c3eramZ1GgKQlRzHXMv4uPYgtCCOkshV0nVoJZpkLBM8zwJHmUnQ21Gg7LdqPRl2uASROKA==; f5avraaaaaaaaaaaaaaaa_session_=NEBJFAADMJGEBPOMKILONMLBPODJBGPEIOMAJIFMEAEEEJHLBPKJEKHPLDPCDABDFAADOHHKGJNKBHMMLALAPMOPBMEKAEMMLKFFCKBHKFLOOCBIILDNGKNBNMDAMFCF; OAMAuthnCookie_mids.usna.edu:443=faBrEpx%2Bc9N4qW3QW0oVuk8qyJNNxRShKFYOoTBsgub5f6X%2FauDMHclC8xnb%2F%2FK1j4DBz8xxrpUN7L1yUfpUzw6KKFCJgUEyLXK1qE7pGSKj7fL9QUAFbOYcsLXa9aeXP8QEqdjnJY2gLIb4wQO26Mxl0c2KfJ%2B1aRsFs9ePmqG3H1Hifjt5Up%2FefeOz%2FJjHmOewXkQizI1bmOQ%2BbmKV8cnciYkfQLju8Vh9dK8qyI%2Bn7Y18H2Skbqu%2FAkfuWQGXOHbta1QUB%2FNUXO46U6YV4k569Id1d4m38SQ%2BGhAa7SiCpJkmBOVGZf07BXQXN%2FgPpGBIOLkx4MhwtgXbIHX0CE3ra0QUtFEA72Zp0k8DaLwnG45%2BNejDKoVr1uos7dNlE3Ilq%2BYX96DIUAsRBeoiFfTFOjH0xUydCTdc%2FrnDaWn2FuhSeh%2B0voYZ9aHEdzXl8ii7Jo7u0K%2FLl4yX4baY%2FNLFK6RuWX7zs%2F6NXHr98phzWxMJzrB3JCZAPN0gDn%2FCR6BkCJBC7KRruGFcj119WDxuRJd7dQe0nfwfLqYlDEfw9xKD9noQJuoQtp5YbRzUkXY3H8sQ7eHK%2BKBswCADJw%3D%3D"
}

resp = requests.post(url, headers=headers, data=data)
print(resp.text)
