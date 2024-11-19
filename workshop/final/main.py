import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import crawling

def send_mail(youremail, yourpw, reemail):
    # 네이버 SMTP 서버 정보
    smtp_server = "smtp.naver.com"
    smtp_port = 587

    # 네이버 이메일 계정 정보
    sender_email = youremail  # 네이버 이메일 주소
    sender_password = yourpw  # 네이버 메일 비밀번호
    receiver_email = reemail  #수신자 이메일 설정

    # 이메일 메시지 작성
    subject = "동국대학교 일반공지 알리미 서비스 입니다." #제목
    body = crawling.noti_page_parser('https://wise.dongguk.ac.kr/article/generalnotice/') #내용

    # 이메일 구성
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # 이메일 전송 및 예외처리
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # 보안 연결 설정
            server.login(sender_email, sender_password)  # 로그인
            server.sendmail(sender_email, receiver_email, message.as_string())  # 이메일 전송
        print("이메일이 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"이메일 전송 중 오류가 발생했습니다: {e}")


mail = input('네이버 이메일을 입력해주세요. \n')
pw = input('비번을 입력해주세요. \n')
receive = input('전송 받을 메일을 입력해주세요.\n')
send_mail(mail, pw, receive)
