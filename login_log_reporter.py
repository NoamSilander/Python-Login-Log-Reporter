import ipaddress

def logger(file):
    failed_login_amount = 0
    succeeded_login_amount = 0
    failed_ips = []
    succeeded_ips = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            if 'Failed' in line:
                split_line = line.split()
                for item in split_line:
                    try:
                        ipaddress.ip_address(item)
                        failed_ips.append(item)
                    except ValueError:
                        pass
                failed_login_amount += 1
            elif 'Accepted' in line:
                split_line = line.split()
                for item in split_line:
                    try:
                        ipaddress.ip_address(item)
                        succeeded_ips.append(item)
                    except ValueError:
                        pass
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