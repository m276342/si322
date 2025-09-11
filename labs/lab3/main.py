#!/usr/bin/env python3
# Title:        main.py
# Description:  Lab3
# Author:       Chris Taylor (m276342)

import requests

url = "https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery"
myobj = {'somekey': 'somevalue'}

Frame 88: 2339 bytes on wire (18712 bits), 2339 bytes captured (18712 bits) on interface enp3s0, id 0
Ethernet II, Src: UniversalGlo_30:24:59 (8c:3b:4a:30:24:59), Dst: ArubaHewlett_a1:90:40 (88:3a:30:a1:90:40)
Internet Protocol Version 4, Src: 10.60.101.204, Dst: 10.1.85.14
Transmission Control Protocol, Src Port: 57788, Dst Port: 443, Seq: 2025, Ack: 8206, Len: 2273
Transport Layer Security
Hypertext Transfer Protocol
    POST /ITSD/mids/drgwq010$mids.actionquery HTTP/1.1\r\n
    Host: mids.usna.edu\r\n
    User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
    Accept-Language: en-US,en;q=0.5\r\n
    Accept-Encoding: gzip, deflate, br, zstd\r\n
    Content-Type: application/x-www-form-urlencoded\r\n
    Content-Length: 192\r\n
    Origin: https://mids.usna.edu\r\n
    Connection: keep-alive\r\n
    Referer: https://mids.usna.edu/ITSD/mids/drgwq010$.startup\r\n
     [truncated]Cookie: f5_cspm=1234; WSG$DRGWQ010$URL0=/ITSD/mids/drgwq010$.startup; WSG$DRGWQ010$CAP0=Schedules_-_Query_Midshipmen; _ga=GA1.1.205993241.1719338122; nmstat=751f859d-6290-a9c1-4c78-b366919ffe78; _ga_LY79N0FLBS=GS2.1.s1757592475
    Upgrade-Insecure-Requests: 1\r\n
    Sec-Fetch-Dest: document\r\n
    Sec-Fetch-Mode: navigate\r\n
    Sec-Fetch-Site: same-origin\r\n
    Sec-Fetch-User: ?1\r\n
    Priority: u=0, i\r\n
    \r\n
    [Full request URI: https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery]
    [HTTP request 1/1]
    [Response in frame: 116]
    File Data: 192 bytes
HTML Form URL Encoded: application/x-www-form-urlencoded
    Form item: "P_ALPHA" = "276342"
    Form item: "P_LAST_NAME" = ""
    Form item: "P_MICO_CO_NBR" = ""
    Form item: "P_SECOF_COOF_SEBLDA_AC_YR" = "2026"
    Form item: "P_SECOF_COOF_SEBLDA_SEM" = "FALL"
    Form item: "P_SECOF_COOF_SEBLDA_BLK_NBR" = "1"
    Form item: "P_MAJOR_CODE" = ""
    Form item: "P_NOMI_FORMATTED_NAME" = ""
    Form item: "Z_ACTION" = "QUERY"
    Form item: "Z_CHK" = "0"


#use the 'cookies' parameter to send cookies to the server:
x = requests.post(url, data = myobj, cookies = {"favcolor": "Red"})

print(x.text)
