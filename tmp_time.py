from requests import get, utils
from datetime import datetime

# разбор работы модуля datetime
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
endcodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=endcodings)
date_req = (content[content.find('Date') + 6: (content.find('Date')) + 16:])
print(date_req, ' изначально')
date_req = (reversed(date_req.split('.')))
date_req = '-'.join(date_req)
print(date_req, ' преобразованный для datetime')
date_str = datetime.fromisoformat(date_req)
date_obj = datetime.strftime(date_str, "%d.%m.%Y")
print(date_obj, ' Итоговый вывод после работы модуля datetime')
# не понял зачем его применять в этом уроке :/
