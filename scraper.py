import requests
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was an issue: %s' % (exc))
len(res.text)
print(res.text[:250])
