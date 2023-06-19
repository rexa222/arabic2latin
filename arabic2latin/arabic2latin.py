MAPPING = {
    'أ': 'a', 'إ': 'e', 'ا': 'a', 'آ': 'aa', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 'th',
    'ج': 'j', 'ح': 'h', 'خ': 'kh', 'د': 'd', 'ذ': 'th', 'ر': 'r', 'ز': 'z',
    'ُژ': 'j', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'dh', 'ط': 't', 'ظ': 'z', 'ع': 'aa',
    'غ': 'gh', 'ف': 'f', 'ق': 'q', 'ك': 'k', 'ک': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm',
    'ن': 'n', 'ه': 'h', 'ة': 'ah', 'و': 'o', 'ؤ': 'o\'', 'ي': 'y', 'ی': 'y', 'ى': 'y',
    'ٰ': 'aa', 'َ': 'a', 'ُ': 'o', 'ِ': 'e', 'ٌ': 'on', 'ً': 'an', 'ٍ': 'en', 'ء': '', 'ئ': '\'e'
}

# vowels and sokoon sign:
VOWELS = ['a', 'e', 'i', 'o', 'u', 'ْ']


def arabic_to_latin(text: str, debug=False):
    n = len(text)
    result = ''
    no_vowel = False
    special_case = False
    for c, char in enumerate(text):
        if special_case:
            special_case = False
            continue

        if char in MAPPING:
            if c == 0 or text[c-1] == " ":
                if char in "اأ" and text[c+1] in "ىيی":
                    result += "ei"
                    special_case = True

                elif char in "اأ" and text[c+1] in "وؤ":
                    result += "ou"
                    special_case = True

                elif char in "ىيی" and text[c+1] in "ؤو":
                    result += "yoo"
                    special_case = True

                elif char == "و":
                    result += "v"

                else:
                    result += MAPPING[char]

            elif char in "ىيی" and (c != n-1 and text[c+1] in MAPPING):
                result += "i"

            elif char == "و":
                if (c != n-1 and text[c+1] in "اىيی") and (c == n-2 or text[c:].startswith("وا ")):
                    if result[-1] == "o":
                        result += "o"
                    else:
                        result += "oo"
                    special_case = True

                elif text[c-1] in "اىيی" or (c != n-1 and text[c+1] in "اىيی"):
                    if result[-1] not in VOWELS and result[-3:] not in " al" and MAPPING[char] != "y":
                        if not no_vowel:
                            result += "a"
                        else:
                            no_vowel = False

                    result += "v"

                else:
                    result += MAPPING[char]

            elif char == "ه" and (c == n-1 or (c != n-1 and text[c+1] == " ")):
                result += "ah"

            elif result:
                # handling special case of double ل in اللّه
                if char == "ل" and (c != n - 1 and text[c + 1] == "ل"):
                    special_case = True

                if result[-1] not in VOWELS and MAPPING[char][:1] not in VOWELS and result[-3:] not in " al" and MAPPING[char] != "y":
                    if not no_vowel:
                        result += "a"
                    else:
                        no_vowel = False

                # prevent occurrence of a letter for more than two times
                if not result.endswith(MAPPING[char] * 2):
                    # handle two character replacements
                    if result[-1] * 2 == MAPPING[char]:
                        result += MAPPING[char][0]
                    else:
                        result += MAPPING[char]

        elif ord(char) < 128:
            result += char

        # tashdid:
        elif char == "ّ":
            # prevent occurrence of a letter for more than two times
            if result[-2:] != MAPPING[text[c-1]] * 2:
                result += MAPPING[text[c - 1]]

        # sokoon:
        elif char == "ْ":
            no_vowel = True

        elif char == "ـْ":
            pass

        elif debug:
            return f"unknown character: {char}"

    return result


if __name__ == '__main__':
    print(arabic_to_latin('سيدعبدالله الموسوي', debug=True))
