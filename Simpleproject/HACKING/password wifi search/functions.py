def remove_spaces(string):        # " " to "/"  exemple: "a a" to "a/a"
    r = ""
    for i in range(len(string)):
        r+="/" if string[i]==" " else string[i]
    return r


def remove_backslash(string):  #"\n" to ""  exemple: "aze\n" to "aze"
    # "\naze" to "\naze"   ...  "\naze\naze\n" to "\naze\naze"
    if string[-1] == "\n":
        return string[:-1]
    else:
        return string



