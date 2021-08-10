
emails = [
"test.email+james@coding.com",
"test.e.mail+toto.jane@coding.com",
"testemail+tom@cod.ing.com"
]

def uniqueEmails(emails):
    strSet = set()
    for email in emails:
        print(email)
        name, domain = email.split('@')
        local = name.split('+')[0].replace('.','')
        strSet.add(local+'@'+domain)
    print("check")
    print(strSet)
    return len(strSet)

print(uniqueEmails(emails))