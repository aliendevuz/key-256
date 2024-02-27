import os

# alpha = 0.75
#
#
# def add(text, pos, char):
#     print(len(text))
#     print(int(len(text) * pos))
#     return f"{text[:int(len(text) * pos)]}{char}{text[int(len(text) * pos):]}"
#
#
# def reset(text, pos, char):
#     print(text[int(len(text) * pos)])
#     return f"{text[:int(len(text) * pos)]}{text[int(len(text) * pos) + 1:]}" if text[int(len(text) * pos)] == char else text

# abc uchun qiymat
# a - boshlang'ich qiymat - (100 - 355) (0 bo'lishi mumkin emas!)
# b - increment qiymat - (100 - 355) (0 bo'lsa u ishdan chiqadi (shifrlamayb qo'yadi))
# c -

def enc(text: str):
    result = b''
    # text = add(text, alpha, "a")
    # a = 1
    # b = 1
    # c = 1

    for i in range(len(text)):
        result += (
            (
                text[i] + (i * 123456 + 100)
            ) % 256
        ).to_bytes()
    return result


def dec(text):
    result = b''
    for i in range(len(text)):
        result += (
            (
                text[i] - (i * 123456 + 100)
            ) % 256
        ).to_bytes()
    # print(result)
    # result = reset(result, alpha, "a")
    return result



def encoder(file):
    with open(file, "rb") as f:
        e = enc(f.read())
    with open(f'{file[:file.rfind(".")]}.enc', "wb") as f:
        f.write(e)
    os.remove(file)


def decoder(file):
    with open(f'{file[:file.rfind(".")]}.enc', "rb") as f:
        d = dec(f.read())
    with open(file, "wb") as f:
        f.write(d)
    os.remove(f'{file[:file.rfind(".")]}.enc')


# encoder("data.txt")
decoder("data.txt")
