    def is_password_good(password):

        if len(password) < 8:
        return False
    Flag1 = False
    Flag2 = False
    Flag3 = False
    for c in password:
        if c.isupper():
            Flagg1 = True
        elif c.islower():
            Flag2 = True
        elif c.isdigit():
            Flag3 = True
    return Flag1 and Flag2 and Flag3


txt = input()
print(is_password_good(txt))




