import re


def mail_parser(mail):
    valid = re.compile(r'(?P<username>([\w.-])@(?P<domain>([\w-]+\.[\w]+)', re.IGNORECASE)
    if not valid.match(mail):
        raise ValueError(f'Wrong email adress: {mail}')
    print(valid.match(mail).groupdict())


try:
    mail_parser('i.yusupov@gmail.com')
    mail_parser('i.yusupov@gmailcom')
    mail_parser('i$yusupov@gmail.com')
except ValueError as error:
    print(error)

    # rez = re.findall(valid, mail)
    # for i in rez:
    #     valid_mail = i.split('@')
    #     if valid_mail:
    #         mail_dict['username'] = valid_mail[0]
    #         mail_dict['domain'] = valid_mail[1]
    #         return mail_dict
    #     else:
    #         assert f'Not valibale email {mail}'
# print(mail_parser(email))
