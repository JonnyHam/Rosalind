def string_slicer(string, a, b, c, d):
    string1 = string[a:b+1]
    string2 = string[c:d+1]
    return string1 + " " + string2

string = "mGct6CmSvRhabdophisz8QKoLwE12HDvPb7dxAy6AO2CgUkY8X6nyn2QRX3TAq07FZskU7tlLXjjdWenZWE9wSDmxFuA2aPcWwN0ieY42W0oXQbqKJeGIsrt3zWbrevipesfyomCvKuKrlXYmLsyBcw5W5HJxQZuDC1POSmDyLyOJ9XLKjuauo10KsABCibJMl."
a = 9
b = 18
c = 123
d = 130
print(string_slicer(string, a, b, c, d))