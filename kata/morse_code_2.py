"""
Name: Decode the Morse code, advanced
Link: https://www.codewars.com/kata/54b72c16cd7f5154e9000457
Level: 4kyu
Desc.: Part 2 of a 3 part series of decoding Morse code Kata
Finished: Yes
"""

import re

from utilities.cw_hidden_variables import MORSE_CODE


def get_time_scale(message: str):
    # get longest sequence of 0s

    if "0" not in message:
        ts_1 = min(map(len, re.findall(r"1+", message)))
        return ts_1

    ts_0 = min(map(len, re.findall(r"0+", message)))
    ts_1 = min(map(len, re.findall(r"1+", message)))
    return min(ts_0, ts_1)


def decode_bits(bits: str):
    ts = get_time_scale(bits := bits.strip().strip("0"))
    print(f"{ts=}, {bits=}")
    return (
        bits.replace("0" * (7 * ts), "   ")
        .replace("1" * (3 * ts), "-")
        .replace("0" * (3 * ts), "/")
        .replace("1" * ts, ".")
        .replace("0" * ts, "")
    )


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
                "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
            )
        ),
    )
