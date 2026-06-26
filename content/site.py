# 서울 출장마사지 사이트 공통 설정

from .regions import DISTRICTS as _DISTRICTS
from .geo import STATIONS as _STATIONS

BASE_URL = "https://seoul-aroma-massage.pages.dev"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"
TELEGRAM = "https://t.me/googleseolab"
AREA_SERVED = "서울특별시"

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시
NAV = [
    ("서울", "/", []),
    ("예약 전 확인", "/check/", [
        ("처음 이용 안내", "/check/first-time/"),
        ("방문 주소 확인", "/check/address/"),
        ("추가 이동비", "/check/travel-fee/"),
        ("건물 출입 방식", "/check/building-access/"),
        ("예약 변경 기준", "/check/reservation-change/"),
        ("개인정보 확인", "/check/privacy/"),
    ]),
    ("이용 장소별", "/use/", [
        ("자택 이용", "/use/home/"),
        ("호텔·숙소 이용", "/use/hotel/"),
        ("오피스텔 이용", "/use/officetel/"),
        ("업무지구 이용", "/use/business-district/"),
        ("역세권 이용", "/use/station-area/"),
        ("야간 예약", "/use/night/"),
    ]),
    ("생활권 안내", "/life/", [
        ("강남역·역삼", "/life/gangnam-yeoksam/"),
        ("잠실·송파", "/life/jamsil-songpa/"),
        ("홍대·합정", "/life/hongdae-hapjeong/"),
        ("여의도·영등포", "/life/yeouido-yeongdeungpo/"),
        ("성수·왕십리", "/life/seongsu-wangsimni/"),
        ("용산·서울역", "/life/yongsan-seoul/"),
        ("목동·양천", "/life/mokdong-yangcheon/"),
        ("연신내·은평", "/life/yeonsinnae-eunpyeong/"),
    ]),
    ("행정구 안내", "/district/", [
        (d["name"], f"/district/{d['slug']}/") for d in _DISTRICTS
    ]),
    ("지하철역 안내", "/station/", [
        (s["name"], f"/station/{s['slug']}/") for s in _STATIONS
    ]),
    ("예약 안내", "/reservation/", []),
    ("운영 기준", "/support/", [
        ("개인정보처리방침", "/support/privacy/"),
        ("서비스 이용 기준", "/support/terms/"),
    ]),
]
