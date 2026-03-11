def health(h1):
    if h1<20:
        return "its critical"
    elif h1<60:
        return "weak"
    return "Strong"
print(health(21))
