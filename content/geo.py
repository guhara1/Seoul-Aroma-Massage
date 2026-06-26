# -*- coding: utf-8 -*-
"""서울 지역 페이지 — 생활권/행정구/행정동/지하철역 (데이터 기반 고유 본문 생성)."""

from .pages import _ul, _links, _checklist, CHECKLIST_BASE, OPERATION_NOTE
from .regions import DISTRICTS


# ─────────────────────────────────────────────────────────────────────────
# 생활권 (life-area)
# ─────────────────────────────────────────────────────────────────────────

LIFE_AREAS = [
    {
        "slug": "gangnam-yeoksam",
        "name": "강남역·역삼",
        "focus": "업무지구와 오피스텔이 밀집한 생활권",
        "intro": "강남역·역삼 생활권은 강남구와 서초구 인접 구간이 겹치는 지역으로, 대형 오피스와 오피스텔, 비즈니스호텔이 섞여 있습니다. 야근·출장 일정에 맞춘 방문이 많아, 건물 출입 방식과 정확한 호수 확인이 특히 중요합니다.",
        "parts": ["역삼동", "서초동", "논현동 일부"],
        "districts": [("강남구", "/district/gangnam-gu/"), ("서초구", "/district/seocho-gu/")],
        "stations": [("강남역", "/station/gangnam-station/")],
        "tip": "오피스텔·비즈니스호텔이 많아 방문자 출입 등록 방식을 미리 확인하면 대기 없이 진행됩니다.",
    },
    {
        "slug": "jamsil-songpa",
        "name": "잠실·송파",
        "focus": "주거지와 상권, 호텔이 인접한 생활권",
        "intro": "잠실·송파 생활권은 대규모 주거 단지와 상권, 호텔이 가까이 있는 지역입니다. 아파트 공동현관 출입과 주차 확인이 잦고, 잠실역 주변 호텔·오피스텔 방문도 함께 이루어집니다.",
        "parts": ["잠실동", "석촌동", "방이동"],
        "districts": [("송파구", "/district/songpa-gu/")],
        "stations": [("잠실역", "/station/jamsil-station/")],
        "tip": "대단지 아파트가 많아 동·호수와 공동현관 비밀번호를 함께 알려주시면 도착이 빠릅니다.",
    },
    {
        "slug": "hongdae-hapjeong",
        "name": "홍대·합정",
        "focus": "숙소와 상권, 유동인구가 많은 생활권",
        "intro": "홍대·합정 생활권은 서교동·연남동·합정동·망원동을 아우르는 상권 중심 지역입니다. 게스트하우스·호텔 등 숙소가 많고 유동인구가 많아, 비슷한 건물 사이에서 정확한 주소 확인이 핵심입니다.",
        "parts": ["서교동", "연남동", "합정동", "망원동"],
        "districts": [("마포구", "/district/mapo-gu/")],
        "stations": [("홍대입구역", "/station/hongik-univ-station/")],
        "tip": "숙소 방문이 많은 지역이라 호텔명·객실 번호 또는 건물명과 호수를 정확히 알려주세요.",
    },
    {
        "slug": "yeouido-yeongdeungpo",
        "name": "여의도·영등포",
        "focus": "업무지구와 오피스, 호텔 중심 생활권",
        "intro": "여의도·영등포 생활권은 금융가 오피스와 영등포 상권, 호텔이 섞인 지역입니다. 평일 야근 일정에 맞춘 오피스·호텔 방문이 많아, 야간 건물 출입 가능 시간 확인이 중요합니다.",
        "parts": ["여의도동", "영등포동", "당산동"],
        "districts": [("영등포구", "/district/yeongdeungpo-gu/")],
        "stations": [("여의도역", "/station/yeouido-station/")],
        "tip": "대형 오피스가 많아 야간에는 건물 출입 가능 시간을 먼저 확인하면 좋습니다.",
    },
    {
        "slug": "seongsu-wangsimni",
        "name": "성수·왕십리",
        "focus": "상권·오피스·주거가 혼합된 생활권",
        "intro": "성수·왕십리 생활권은 카페·쇼룸 상권과 오피스, 주거가 빠르게 섞인 지역입니다. 옛 공장을 개조한 건물과 신축 오피스텔이 함께 있어, 건물 유형에 따른 출입 확인이 필요합니다.",
        "parts": ["성수동", "행당동", "왕십리"],
        "districts": [("성동구", "/district/seongdong-gu/")],
        "stations": [("성수역", "/station/seongsu-station/")],
        "tip": "리모델링 건물과 신축이 섞여 있어 건물명과 출입 방식을 함께 알려주시면 정확합니다.",
    },
    {
        "slug": "yongsan-seoul",
        "name": "용산·서울역",
        "focus": "숙소와 외국인 거주가 많은 생활권",
        "intro": "용산·서울역 생활권은 용산역·서울역 주변 호텔과 한남·이태원 거주지가 이어지는 지역입니다. 외국인 거주와 출장 방문이 많아 숙소 방문 정책 확인이 잦습니다.",
        "parts": ["한강로동", "남영동", "이태원동 일부"],
        "districts": [("용산구", "/district/yongsan-gu/")],
        "stations": [("용산역", "/station/yongsan-station/")],
        "tip": "역 주변 호텔 방문이 많아 호텔명·객실 번호와 예약자 이름을 함께 확인합니다.",
    },
    {
        "slug": "mokdong-yangcheon",
        "name": "목동·양천",
        "focus": "주거지와 학원가 중심 생활권",
        "intro": "목동·양천 생활권은 대단지 아파트와 학원가, 오목교 상권이 중심인 주거 지역입니다. 가족 단위 거주가 많아 자택 방문 시 공동현관과 주차 확인이 주로 이루어집니다.",
        "parts": ["목동", "신정동", "오목교"],
        "districts": [("양천구", "/district/yangcheon-gu/")],
        "stations": [],
        "tip": "대단지 주거 지역이라 동·호수와 방문 차량 등록 여부를 미리 확인하면 좋습니다.",
    },
    {
        "slug": "yeonsinnae-eunpyeong",
        "name": "연신내·은평",
        "focus": "주거 생활권과 3·6호선 환승 중심",
        "intro": "연신내·은평 생활권은 은평 뉴타운과 주거지가 넓게 자리한 지역으로, 3·6호선 환승역인 연신내역을 중심으로 이동합니다. 주거 방문이 많아 단지 출입과 이동 거리 확인이 중요합니다.",
        "parts": ["불광동", "응암동", "역촌동"],
        "districts": [("은평구", "/district/eunpyeong-gu/")],
        "stations": [],
        "tip": "서울 북서쪽 주거 생활권으로 이동 거리에 따라 추가 이동비가 있을 수 있어 미리 확인하세요.",
    },
]


def build_life_pages():
    hub = {
        "path": "life/",
        "title": "서울 생활권 안내｜출장마사지 방문 가능 지역｜간다GO",
        "desc": "강남·잠실·홍대·여의도·성수·용산·목동·연신내 등 서울 생활권별 방문 가능 지역을 안내합니다.",
        "h1": "서울 생활권 안내",
        "breadcrumb": [("생활권 안내", None)],
        "body": (
            "<section><h2>생활권으로 보는 서울 방문 가능 지역</h2>"
            "<p>행정구보다 실제 이동에 가까운 단위가 생활권입니다. 각 생활권은 성격이 "
            "달라 확인할 내용도 다릅니다. 강남·역삼은 업무지구, 잠실·송파는 주거·상권, "
            "홍대·합정은 숙소·상권 중심으로 안내합니다.</p>"
            + _links([(a["name"], f"/life/{a['slug']}/") for a in LIFE_AREAS])
            + "</section>"
        ),
    }
    pages = [hub]
    for a in LIFE_AREAS:
        body = f"<p class=\"lead\">{a['intro']}</p>"
        body += (
            f"<section><h2>{a['name']} 생활권의 성격</h2>"
            f"<p>이 지역은 <strong>{a['focus']}</strong>입니다. {a['tip']}</p></section>"
        )
        body += (
            "<section><h2>이 생활권에 포함되는 지역</h2>"
            + _ul(a["parts"]) + "</section>"
        )
        if a["stations"]:
            body += (
                "<section><h2>가까운 지하철역</h2>"
                + _links(a["stations"]) + "</section>"
            )
        body += (
            "<section><h2>이용 장소별 확인사항</h2>"
            "<p>방문 장소에 따라 확인할 내용이 다릅니다.</p>"
            + _links([
                ("자택 이용", "/use/home/"),
                ("호텔·숙소 이용", "/use/hotel/"),
                ("오피스텔 이용", "/use/officetel/"),
            ])
            + "</section>"
        )
        body += (
            "<section><h2>예약 전 확인하면 좋은 점</h2>"
            f"<p>{a['name']} 생활권에서 방문형 관리를 예약할 때는, 정확한 방문 주소와 "
            "건물 출입 방식을 먼저 확인하는 것이 가장 중요합니다. 같은 생활권 안에서도 "
            "건물 유형과 도로 사정이 달라, 가까운 역과 도로명 주소를 함께 알려주시면 도착이 "
            "빠릅니다. 외곽으로 이어지는 구간은 추가 이동비가 발생할 수 있으므로 통화에서 미리 "
            "확인하고, 야간 방문이라면 건물의 야간 출입 가능 시간도 함께 점검하세요. 아래 "
            "체크리스트로 빠진 항목이 없는지 확인하면 예약이 한결 수월합니다.</p></section>"
        )
        body += _checklist(CHECKLIST_BASE)
        related = list(a["districts"]) + [
            ("생활권 안내 전체", "/life/"),
            ("예약 전 확인사항", "/check/"),
            ("이용 장소별 안내", "/use/"),
        ]
        body += "<section><h2>관련 지역 보기</h2>" + _links(related) + "</section>"
        body += "<section><h2>운영 기준</h2>" + OPERATION_NOTE + "</section>"
        pages.append({
            "path": f"life/{a['slug']}/",
            "title": f"{a['name']} 생활권 출장마사지 안내｜간다GO",
            "desc": f"{a['name']} 생활권 출장마사지·홈타이 방문 가능 지역과 예약 전 확인사항을 안내합니다."[:80],
            "h1": f"{a['name']} 생활권 출장마사지 안내",
            "breadcrumb": [("생활권 안내", "/life/"), (a["name"], None)],
            "body": body,
            "faq": [
                (f"{a['name']} 생활권은 어디까지 방문하나요?", f"{', '.join(a['parts'])} 일대를 안내합니다. 정확한 주소는 예약 통화에서 확인합니다."),
                ("예약 전에 무엇을 확인하나요?", "방문 주소, 건물 출입 방식, 추가 이동비 여부를 먼저 확인합니다."),
            ],
        })
    return pages




def build_district_pages():
    # 행정구 hub 페이지
    hub = {
        "path": "district/",
        "title": "서울 행정구 안내｜25개 구별 출장마사지 방문 지역｜간다GO",
        "desc": "서울 25개 행정구 전역의 출장마사지·홈타이 방문 가능 지역을 구별로 안내합니다.",
        "h1": "서울 행정구 안내",
        "breadcrumb": [("행정구 안내", None)],
        "body": (
            "<section><h2>서울 25개 구별 방문 가능 지역</h2>"
            "<p>구 페이지는 대표 행정동·생활권·지하철역·예약 전 확인사항을 모은 허브입니다. "
            "같은 구 안에서도 생활권마다 이동 기준이 다르므로, 구 페이지에서 행정동으로 좁혀 "
            "확인하시면 좋습니다. 각 행정동 페이지에서는 지역 특성에 맞는 방문 안내를 제공합니다.</p>"
            + _links([(d["name"], f"/district/{d['slug']}/") for d in DISTRICTS])
            + "</section>"
        ),
    }
    pages = [hub]

    # 각 행정구 페이지 생성
    for d in DISTRICTS:
        body = f"<p class=\"lead\">{d['intro']}</p>"
        body += (
            f"<section><h2>{d['name']} 지역 특성</h2>"
            f"<p>{d['name']}는 <strong>{d['focus']}</strong> 지역입니다. "
            "각 행정동별로 방문 환경이 다르니, 방문 장소와 구체적인 주소로 확인하는 것이 좋습니다.</p>"
            + "</section>"
        )
        body += (
            "<section><h2>방문 가능 행정동</h2>"
            "<p>이 구의 행정동 전역에서 방문이 가능하며, 각 동별 상세 안내는 링크를 참고하세요.</p>"
            + _links([(dong, f"/district/{d['slug']}/{dong}/") for dong in d["dongs"]])
            + "</section>"
        )
        body += (
            "<section><h2>이용 장소별 확인사항</h2>"
            "<p>방문 장소에 따라 확인 포인트가 다릅니다.</p>"
            + _links([
                ("자택 이용", "/use/home/"),
                ("오피스텔 이용", "/use/officetel/"),
                ("업무지구 이용", "/use/business-district/"),
                ("호텔·숙소 이용", "/use/hotel/"),
            ])
            + "</section>"
        )
        body += (
            "<section><h2>예약 전 확인사항</h2>"
            f"<p>{d['name']}는 {d['focus']} 지역인 만큼, 방문하는 건물의 유형에 따라 확인할 "
            "내용이 달라집니다. 오피스텔과 주상복합은 방문자 출입 등록과 카드키 동행 여부를, "
            "아파트는 공동현관 비밀번호와 동·호수를, 호텔은 객실 번호와 예약자 이름을 미리 "
            f"확인하면 도착이 매끄럽습니다. {', '.join(d['dongs'][:3])} 등 주요 행정동은 생활권에 "
            "따라 이동 거리가 다르므로, 외곽 구간은 추가 이동비 발생 여부를 통화에서 함께 "
            "확인하세요. 아래 체크리스트로 빠진 항목이 없는지 점검하시기 바랍니다.</p></section>"
        )
        body += _checklist(CHECKLIST_BASE)
        related = [
            ("행정구 안내 전체", "/district/"),
            ("생활권 안내", "/life/"),
            ("예약 전 확인사항", "/check/"),
        ]
        body += "<section><h2>관련 지역 보기</h2>" + _links(related) + "</section>"
        body += "<section><h2>운영 기준</h2>" + OPERATION_NOTE + "</section>"
        pages.append({
            "path": f"district/{d['slug']}/",
            "title": f"{d['name']} 출장마사지｜{d['focus']} 방문 안내｜간다GO",
            "desc": f"{d['name']} 출장마사지·홈타이 방문 가능 행정동과 예약 전 확인사항을 안내합니다."[:80],
            "h1": f"{d['name']} 출장마사지 · 방문 가능 행정동 안내",
            "breadcrumb": [("행정구 안내", "/district/"), (d["name"], None)],
            "body": body,
            "faq": [
                (f"{d['name']}는 어느 동까지 방문하나요?", f"{', '.join(d['dongs'])} 등 {d['name']} 전역을 안내합니다. 외곽은 추가 이동비가 있을 수 있습니다."),
                ("구 안에서도 환경이 다른가요?", "네. 같은 구라도 행정동마다 오피스·주거·상권 비중이 달라 확인할 내용이 다릅니다."),
            ],
        })

        # 각 행정동 페이지 생성
        for dong in d["dongs"]:
            dong_slug = dong
            dong_body = (
                f"<p class=\"lead\">{d['name']} {dong}은 {d['focus']} 지역의 일부입니다. "
                f"정확한 방문 주소, 건물 유형, 그리고 가까운 역 정보를 함께 알려주시면 "
                "도착 시간을 더 정확히 안내할 수 있습니다.</p>"
            )
            dong_body += (
                f"<section><h2>{d['name']} {dong} 지역 안내</h2>"
                f"<p>{d['name']} 구청이 관할하는 {dong}은 이 구의 주요 행정동 중 하나입니다. "
                f"{d['intro']}"
                "</p></section>"
            )
            dong_body += (
                "<section><h2>예약 전 확인사항</h2>"
                "<p>이 지역에서 방문 예약을 할 때는 다음을 확인해주세요:</p>"
                + _ul([
                    "정확한 도로명 주소 또는 건물명과 동·호수",
                    "건물 유형(아파트/오피스텔/호텔/주상복합 등)",
                    "건물 출입 방식(공동현관 비밀번호/카드키/현장 도착 등)",
                    "야간 또는 특수 시간 방문 시 출입 가능 여부",
                    "주차 여부 또는 주차 위치",
                    "예약된 코스(60/90/120분)와 희망 시간대",
                ])
                + "</section>"
            )
            dong_body += (
                f"<section><h2>{d['name']} {dong} 근처 이용 안내</h2>"
                + _links([
                    ("자택 이용 시", "/use/home/"),
                    ("호텔·숙소 이용 시", "/use/hotel/"),
                    ("오피스텔 이용 시", "/use/officetel/"),
                ])
                + "</section>"
            )
            dong_body += _checklist(CHECKLIST_BASE)
            dong_body += (
                f"<section><h2>{d['name']} {dong} 관련 지역</h2>"
                + _links([
                    (f"{d['name']} 전체", f"/district/{d['slug']}/"),
                    ("행정구 안내", "/district/"),
                    ("생활권 안내", "/life/"),
                ])
                + "</section>"
            )
            dong_body += "<section><h2>운영 기준</h2>" + OPERATION_NOTE + "</section>"

            pages.append({
                "path": f"district/{d['slug']}/{dong_slug}/",
                "title": f"{d['name']} {dong} 출장마사지 예약｜간다GO",
                "desc": f"{d['name']} {dong} 출장마사지·홈타이 방문 가능 지역과 예약 안내입니다."[:80],
                "h1": f"{d['name']} {dong} 출장마사지 예약 안내",
                "breadcrumb": [
                    ("행정구 안내", "/district/"),
                    (d["name"], f"/district/{d['slug']}/"),
                    (dong, None)
                ],
                "body": dong_body,
                "faq": [
                    (f"{d['name']} {dong}에서 방문이 되나요?", f"네, {d['name']} {dong} 지역에서 방문이 가능합니다. 정확한 주소와 건물 유형을 알려주시면 예약을 진행할 수 있습니다."),
                    ("추가 이동비가 있을까요?", f"{d['name']} {dong}은 서울 시내 구간이므로 기본 이동비 범위 내에 포함됩니다. 외곽 경계 지역은 통화 시 확인합니다."),
                ],
            })

    return pages


# ─────────────────────────────────────────────────────────────────────────
# 지하철역 (station) — 역명 기준 1개 URL, 출구·노선 분리 없음
# ─────────────────────────────────────────────────────────────────────────

STATIONS = [
    {
        "slug": "gangnam-station", "name": "강남역",
        "intro": "강남역 주변에서 방문형 관리를 찾을 때는 역명보다 실제 방문 주소가 더 중요합니다. 강남역은 역삼동·서초동·논현동 생활권이 겹치고 비슷한 오피스 건물이 많아, 도로명 주소와 호수를 함께 확인합니다.",
        "dongs": ["역삼동", "서초동", "논현동"],
        "life": [("강남역·역삼", "/life/gangnam-yeoksam/")],
        "district": [("강남구", "/district/gangnam-gu/")],
        "transfer": "2호선·신분당선 환승역",
    },
    {
        "slug": "jamsil-station", "name": "잠실역",
        "intro": "잠실역 일대는 대단지 주거와 상권, 호텔이 가까이 있습니다. 아파트는 공동현관·동·호수 확인이, 호텔·오피스텔은 객실·출입 방식 확인이 주된 포인트입니다.",
        "dongs": ["잠실동", "석촌동", "방이동"],
        "life": [("잠실·송파", "/life/jamsil-songpa/")],
        "district": [("송파구", "/district/songpa-gu/")],
        "transfer": "2호선·8호선 환승역",
    },
    {
        "slug": "hongik-univ-station", "name": "홍대입구역",
        "intro": "홍대입구역은 서교동·연남동·합정동 생활권이 이어지는 상권 중심 지역입니다. 숙소와 상가 건물이 밀집해 비슷한 외관이 많으므로 건물명과 호수를 정확히 확인합니다.",
        "dongs": ["서교동", "연남동", "합정동"],
        "life": [("홍대·합정", "/life/hongdae-hapjeong/")],
        "district": [("마포구", "/district/mapo-gu/")],
        "transfer": "2호선·공항철도·경의중앙선 환승역",
    },
    {
        "slug": "yeouido-station", "name": "여의도역",
        "intro": "여의도역 주변은 금융가 오피스와 호텔이 밀집한 업무지구입니다. 평일 야근 일정 방문이 많아 야간 건물 출입 가능 시간을 먼저 확인하면 좋습니다.",
        "dongs": ["여의도동"],
        "life": [("여의도·영등포", "/life/yeouido-yeongdeungpo/")],
        "district": [("영등포구", "/district/yeongdeungpo-gu/")],
        "transfer": "5호선·9호선 환승역",
    },
    {
        "slug": "seongsu-station", "name": "성수역",
        "intro": "성수역 일대는 옛 공장을 개조한 상권 건물과 신축 오피스텔이 섞여 빠르게 변하는 지역입니다. 건물 유형에 따라 출입 방식이 다르므로 건물명과 출입 방법을 함께 확인합니다.",
        "dongs": ["성수동", "행당동"],
        "life": [("성수·왕십리", "/life/seongsu-wangsimni/")],
        "district": [("성동구", "/district/seongdong-gu/")],
        "transfer": "2호선",
    },
    {
        "slug": "yongsan-station", "name": "용산역",
        "intro": "용산역 주변은 호텔·오피스와 한강로 주거가 가까이 있는 지역입니다. 역 주변 호텔 방문이 많아 호텔명·객실 번호·예약자 이름을 함께 확인합니다.",
        "dongs": ["한강로동", "남영동"],
        "life": [("용산·서울역", "/life/yongsan-seoul/")],
        "district": [("용산구", "/district/yongsan-gu/")],
        "transfer": "1호선·경부선",
    },
]


def build_station_pages():
    hub = {
        "path": "station/",
        "title": "서울 지하철역 안내｜역세권 출장마사지 방문 기준｜간다GO",
        "desc": "강남역·잠실역·홍대입구역·여의도역·성수역·용산역 등 역세권 방문 기준을 안내합니다.",
        "h1": "서울 지하철역 안내",
        "breadcrumb": [("지하철역 안내", None)],
        "body": (
            "<section><h2>역세권으로 보는 방문 기준</h2>"
            "<p>역 페이지는 역명 기준 1개만 두며, 환승역도 노선·출구별로 나누지 않습니다. "
            "역명보다 실제 방문 주소가 더 중요하므로, 역 주변 생활권과 함께 확인하세요.</p>"
            + _links([(s["name"], f"/station/{s['slug']}/") for s in STATIONS])
            + "</section>"
        ),
    }
    pages = [hub]
    for s in STATIONS:
        body = f"<p class=\"lead\">{s['intro']}</p>"
        body += (
            f"<section><h2>{s['name']} 인접 생활권</h2>"
            f"<p>{s['name']}는 {s['transfer']}으로, 아래 생활권과 행정동이 인접합니다.</p>"
            + _links(s["life"]) + "</section>"
        )
        body += "<section><h2>가까운 행정동</h2>" + _ul(s["dongs"]) + "</section>"
        body += (
            "<section><h2>이용 장소별 확인사항</h2>"
            "<p>역 주변은 오피스텔·호텔·상가가 섞여 있어 장소별 확인이 필요합니다.</p>"
            + _links([
                ("오피스텔 이용", "/use/officetel/"),
                ("호텔·숙소 이용", "/use/hotel/"),
                ("역세권 이용", "/use/station-area/"),
            ])
            + "</section>"
        )
        body += _checklist(CHECKLIST_BASE)
        related = list(s["district"]) + list(s["life"]) + [
            ("지하철역 안내 전체", "/station/"),
            ("예약 전 확인사항", "/check/"),
        ]
        body += "<section><h2>관련 지역 보기</h2>" + _links(related) + "</section>"
        body += "<section><h2>운영 기준</h2>" + OPERATION_NOTE + "</section>"
        pages.append({
            "path": f"station/{s['slug']}/",
            "title": f"{s['name']} 출장마사지｜인접 생활권·방문 안내｜간다GO",
            "desc": f"{s['name']} 주변 출장마사지·홈타이 인접 생활권과 예약 전 확인사항을 안내합니다."[:80],
            "h1": f"{s['name']} 출장마사지 · 인접 생활권 안내",
            "breadcrumb": [("지하철역 안내", "/station/"), (s["name"], None)],
            "body": body,
            "faq": [
                (f"{s['name']} 근처라고만 하면 되나요?", "역·출구에 더해 건물명과 동·호수를 알려주시면 도착이 정확하고 빠릅니다."),
                ("환승역은 출구별로 나뉘나요?", "아니요. 역명 기준 한 곳으로 안내하며, 정확한 위치는 방문 주소로 확인합니다."),
            ],
        })
    return pages
