# Login Log Reporter
A reporter written in Python that parses a Linux auth.log and prints successful and failed login attempts (and the IP addresses associated with the failures). I haven't robustly tested it on every single log scenario, so treat this more as a learning project rather than a real tool.

The repo includes a dummy `auth.log` that I tested the script on. You can use whatever filename you want as long as you pass it as the argument of the `logger()` function at the end of the script.

Works by using `.split()` and the `ipaddress` module to parse the logs.

## How to Run
1. Paste your `auth.log` file in **THE SAME WORKING DIRECTORY** as the script
2. run `login_log_reporter.py`

## Example
```
--- Login report ---

Login attempts: 2060
Failed logins: 2013
Successful logins: 47

IPs behind failed logins:
198.51.100.7
192.0.2.201
192.0.2.44
203.0.113.77
2001:db8:9a1::2
198.51.100.23
203.0.113.5
2001:db8:4f::17
192.0.2.10
```