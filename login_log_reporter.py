def logger(file):
    failed_login_amount = 0
    succeeded_login_amount = 0
    failed_ips = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            split_line = line.split()
            ip_line = split_line[-4]
            if 'Failed' in line:
                failed_login_amount += 1
                failed_ips.append(ip_line)
            elif 'Accepted' in line:
                succeeded_login_amount += 1
    login_amount = failed_login_amount + succeeded_login_amount
    print(f'--- Login report ---\n\nLogin attempts: {login_amount}\nFailed logins: {failed_login_amount}\nSuccessful logins: {succeeded_login_amount}')
    print(f'\nIPs behind failed logins:')
    used_ips = []
    for ip in failed_ips:
        if not ip in used_ips:
            used_ips.append(ip)
            print(ip)
    
if __name__ == '__main__':
    logger('auth.log')