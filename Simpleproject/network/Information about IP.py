from geoip import geolite2

locator = "92.119.89.19"

print(geolite2.lookup(locator))
