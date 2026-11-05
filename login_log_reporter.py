def logger(file):
    with open(file, encoding='utf-8') as f:
        login_amount = 0
        for line in f:

            split_line = line.split()
            ip_line = split_line[-4]
            if 'Failed' in line:
                print(ip_line)

logger('auth.log')