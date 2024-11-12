"""
Name: Decode the Morse code for real
Link: https://www.codewars.com/kata/decode-the-morse-code-for-real
Level: 2kyu
Desc.: Part 3 of a 3 part series of decoding Morse code Kata
Finished: No
"""

import re

from utilities.cw_hidden_variables import MORSE_CODE


def decode_bits(bits: str):
    bits = bits.strip("0")

    if not bits:
        return ""

    on_units = [len(match.group()) for match in re.finditer(r"1+", bits)]
    off_units = [len(match.group()) for match in re.finditer(r"0+", bits)]

    on_mid_point = (min(on_units) + max(on_units)) / 2
    off_mid_point = (min(off_units) + max(off_units)) / 2

    dot_lengths = []
    dash_lengths = []
    intra_lengths = []  # spaces between dots/dashes for a single character
    inter_lengths = []  # spaces between words

    # group based on proximity to dot or dash
    for i in on_units:
        if i <= on_mid_point:
            dot_lengths.append(i)
        else:
            dash_lengths.append(i)

    # replace sequences of ones with dots and dashes based on length of sequence in decreasing order
    for i in sorted(list(set(dot_lengths)), reverse=True):
        bits = re.sub(r"1{%d}" % i, ".", bits)

    for i in sorted(list(set(dash_lengths)), reverse=True):
        bits = re.sub(r"1{%d}" % i, "-", bits)

    return bits


def decode_morse(morseCode: str):
    print("morseCode:", morseCode)
    return " ".join(
        "".join(MORSE_CODE[letter] for letter in word.split("/"))
        for word in morseCode.strip().split("   ")
    )


if __name__ == "__main__":
    print(
        "ans: ",
        decode_morse(
            decode_bits(
                "0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000"
            )
        ),
    )
