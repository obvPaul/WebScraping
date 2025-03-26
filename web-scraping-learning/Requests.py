import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
restest = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    restest.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
type(res)

res.status_code == requests.codes.ok

len(res.text)

print(res.text[:250])

