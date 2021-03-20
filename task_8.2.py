import re

valid_str = re.compile(r'([\w\.\+\:\/\"]+)')


def parcer(line_fom_log):
    log_line = valid_str.findall(line_fom_log)
    print((log_line[0], log_line[1] + log_line[2], log_line[3][1:], log_line[4], log_line[6], log_line[7]))


with open('nginx_logs.txt', encoding='utf-8') as log:
    for line in log:
        parcer(line)
