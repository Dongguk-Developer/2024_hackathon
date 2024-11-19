import requests
from bs4 import BeautifulSoup
from datetime import datetime


def noti_page_parser(noti_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(noti_link + 'list#none', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    # 현재 날짜와 시간 가져오기
    current_time = datetime.now().strftime("%Y-%m-%d %H시")
    Noti_num_list = list()
    Noti_num_list.append(f"{current_time} 공지 내역입니다. \n\n")

    # 한 페이지 전체를 크롤링 하도록 16으로 설정
    for i in range(1, 16):
        # 공지인 경우 크롤링을 진행하지 않음
        title = soup.select_one(
            '#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child(%d) > a > div.top > p > span' % i)
        if title is not None:
            continue

        # 공지 제목 추출
        title = soup.select_one(
            '#wrap > div.ly-right > div.contents > div > div.board > div.board_list > ul > li:nth-child(%d) > a > div.top > p' % i)

        if title is None:  # 만약 제목이 없다면 continue
            continue

        Notice_Title = title.get_text(strip=True)

        # 리스트 저장 부분
        Noti_num_list.append(f"- {Notice_Title}\n")

    # 리스트를 하나의 문자열로 결합하여 반환
    return ''.join(Noti_num_list)

print(noti_page_parser('https://wise.dongguk.ac.kr/article/generalnotice/'))
