def importListFromFile(file):
    f = open(file)
    addresses = f.readlines()
    f.close()
    return addresses


def exportListFromFile(file, emails):
    f = open(file, 'w')

    for email in emails:
        f.write(email + '\n')

    f.close()
    return
