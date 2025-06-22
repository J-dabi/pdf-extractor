import re

def extract_info(text):
    result = {}

    # ✅ CPU: Intel Core, Atom, Celeron 등 유연하게 대응
    result["CPU"] = re.search(r"(Intel.*?Processor.*?)(?:\n|•|,)", text, re.IGNORECASE)

    # ✅ Memory: DDR3/4/5 등 다양한 형식 대응
    result["Memory"] = re.search(r"(DDR\d.*?SO-DIMM.*?(?:Supports.*?GB|up to.*?GB|Memory).*)", text, re.IGNORECASE)

    # ✅ LAN: 1x/2x/4x GbE, 2.5GbE, 10GbE 등 폭넓게 잡기
    result["LAN"] = re.search(r"(\d+ ?x ?(?:2\.5)?10?GbE.*?LAN.*?)", text, re.IGNORECASE)

    # ✅ Size: 150 x 105 x 56 mm 등 숫자 3개 + mm 형식
    result["Size"] = re.search(r"(\d{2,4}(?:\.\d+)? ?x ?\d{2,4}(?:\.\d+)? ?x ?\d{2,4}(?:\.\d+)? ?mm)", text, re.IGNORECASE)

    # ✅ 정제: 결과가 있으면 .group(1), 없으면 '정보 없음'
    for key in result:
        if result[key]:
            result[key] = result[key].group(1).strip()
        else:
            result[key] = "정보 없음"

    return result