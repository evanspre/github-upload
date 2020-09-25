import sys
import requests

print(sys.version)
print(sys.version_info)
print(sys.executable)
print(sys.api_version)
print(sys.copyright)
print(sys.platform)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Paul"))

# use requests to get stuff from a website
r = requests.get("http://www.bbc.co.uk")
print(r.status_code)
print(r.url)
print(r.encoding)