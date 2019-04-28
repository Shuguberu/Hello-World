import requests
r = requests.get("https://item.jd.com/5089253.html")
print(r.status_code)
print(r.encoding)
print(r.text[:1000])
