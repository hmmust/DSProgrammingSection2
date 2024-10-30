import sys


def send_email(e,m):
    print(f'Sending to {e}:{m}')


def send_message(e,m):
    print(f'Messaging {e}:{m}')
    
email = sys.argv[1]
message = sys.argv[2]

send_email(email,message)
send_message(email,message)


