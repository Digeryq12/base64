import math
from textwrap import wrap

base64_dict = {
    0: 'A',  1: 'B',  2: 'C',  3: 'D',  4: 'E',  5: 'F',  6: 'G',  7: 'H',
    8: 'I',  9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
   16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
   24: 'Y', 25: 'Z',

   26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f',
   32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l',
   38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r',
   44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x',
   50: 'y', 51: 'z',

   52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5',
   58: '6', 59: '7', 60: '8', 61: '9',
   62: '+', 63: '/'
}

def encode():
    plaintext = input("Plaintext: ")

    ascii_array = []
    for char in plaintext:
        ascii_array.append(ord(char))

    binary_string = ""
    for ascii_int in ascii_array:
        ebbc = ""
        while ascii_int > 0:
            ebbc += str(ascii_int % 2)
            ascii_int = math.floor(ascii_int / 2)

        while len(ebbc) != 8:
            ebbc += "0"
        
        binary_string += (ebbc[::-1])

    six_bit_binary_array = wrap(binary_string, 6)

    decimal_array = []
    for sbbc in six_bit_binary_array:
        while len(sbbc) != 6:
            sbbc += "0"

        p = 0
        decimal_res = 0
        for d in sbbc[::-1]:
            decimal_res += int(d) * math.pow(2, p)
            p += 1

        decimal_array.append(int(decimal_res))

    base64_result = ""
    for decimal_int in decimal_array:
        base64_result += base64_dict[decimal_int]

    while len(base64_result) % 4 != 0:
        base64_result += "="

    return base64_result

def decode():
    base64 = input("Base64: ")

    if len(base64) % 4 != 0:
        return "Invalid base64 input."

    padding_start = base64.find("=")

    if padding_start > -1:
        base64 = base64[0 : padding_start]

    decimal_array = []
    for base64_char in base64:
        decimal_res = 0

        if base64_char not in base64_dict.values(): return "Invalid base64 character."

        for val in base64_dict.values():
            if val == base64_char:
                decimal_array.append(decimal_res)
                break
            
            decimal_res += 1
    
    binary_string = ""
    for decimal_int in decimal_array:
        sbbc = ""
        while decimal_int > 0:
            sbbc += str(decimal_int % 2)
            decimal_int = math.floor(decimal_int / 2)

        while len(sbbc) != 6:
            sbbc += "0"
            
        binary_string += (sbbc[::-1])
    
    eight_bit_binary_array = wrap(binary_string, 8)

    ascii_array = []
    for ebbc in eight_bit_binary_array:
        if len(ebbc) == 8:
            p = 0
            ascii_res = 0
            for d in ebbc[::-1]:
                ascii_res += int(d) * math.pow(2, p)
                p += 1

            ascii_array.append(int(ascii_res))

    text_result = ""
    for ascii_int in ascii_array:
        text_result += chr(ascii_int)

    return text_result


method = input("Encode/Decode: ")
if method.lower() == "encode":
    print(encode())
elif method.lower() == "decode":
    print(decode())
else:
    print("Invalid method.")