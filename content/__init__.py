# -*- coding: utf-8 -*-
"""서울 출장마사지 — 페이지 모음.

build.py 가 PAGES 를 읽어 정적 HTML을 생성한다.
"""
from .pages import MAIN_PAGE, build_check_pages, build_use_pages
from .geo import build_life_pages, build_district_pages, build_station_pages
from .info import INFO_PAGES

PAGES = (
    [MAIN_PAGE]
    + build_check_pages()
    + build_use_pages()
    + build_life_pages()
    + build_district_pages()
    + build_station_pages()
    + INFO_PAGES
)
