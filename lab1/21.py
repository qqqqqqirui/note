def lowercaseOnly(text):
    lowercase_text = ""
    for char in text:
        if char.islower():
            lowercase_text += char
    return lowercase_text

print(lowercaseOnly("aDDx2_ @ 2xef2n0)"))
