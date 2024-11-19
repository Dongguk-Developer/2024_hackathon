import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import crawling

def send_mail(youremail, yourpw, reemail):
    # 메일 서버 설정
    smtp_server = "smtp.naver.com"
    smtp_port = 587

    # 네이버 이메일 계정 정보
    sender_email = youremail
    sender_password = yourpw
    receiver_email = reemail

    # 이메일 메시지 작성
    subject = "제목: 파이썬을 이용하여 보내는 메일입니다." #제목
    body = "안녕하세요. 파이썬을 이용하여 보내는 테스트 메일 입니다" #내용

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # 이메일 전송 및 예외처리
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("이메일이 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"이메일 전송 실패: {e}")


mail = input('네이버 이메일을 입력해주세요. \n')
pw = input('비번을 입력해주세요. \n')
receive = input('전송 받을 메일을 입력해주세요.\n')
send_mail(mail, pw, receive)
