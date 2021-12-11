import requests
from readingSates import State


def getHTML(address):
    content = requests.get(url = address).text
    return content


def legalChar(char):
    if 'a' <= char <= 'z' or char == '.':
        return True
    else:
        return False


def distinct(elements: list):
    elements.sort()
    i = 0
    while i < len(elements) - 1:
        if elements[i] == elements[i + 1]:
            elements.pop(i + 1)
        else:
            i += 1

    return elements


def mergeDistinct(elem_a: list, elem_b: list):
    elem_a += elem_b
    return distinct(elem_a)


def find_eMails(text):
    emails = []
    word = ""
    state = State.INITIAL

    for char in text:

        if state == State.INITIAL:
            word = ""
            if legalChar(char):
                state = State.VALID_I
                word += char
            elif char == '@':
                state = State.INVALID
            else:
                state = State.INITIAL

        elif state == State.VALID_I:
            if legalChar(char):
                state = State.VALID_I
                word += char
            elif char == '@':
                state = State.AT
                word += char
            else:
                state = State.INITIAL

        elif state == State.AT:
            if legalChar(char):
                state = State.VALID_II
                word += char
            elif char == '@':
                state = State.INVALID
            else:
                state = State.INITIAL

        elif state == State.VALID_II:
            if legalChar(char):
                state = State.VALID_II
                word += char
            elif char == '@':
                state = State.INVALID
            else:
                emails.append(word)
                state = State.INITIAL

        elif state == State.INVALID:
            if legalChar(char):
                state = State.INVALID
            elif char == '@':
                state = State.INVALID
            else:
                state = State.INITIAL

    if state == State.VALID_II:
        emails.append(word)

    distinct(emails)
    return emails


def harvest(address):
    content = getHTML(address)
    emails = find_eMails(content)
    return emails
