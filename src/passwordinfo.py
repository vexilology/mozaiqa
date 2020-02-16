import math
import string
import config

class Passwordinfo:
    def __init__(self, s):
        self.a = s

    def finish(self):
        def complex_password(full_words):
            length = len(full_words)
            complexity = 0
            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            nums = string.digits
            has_lower = False
            has_upper = False
            has_sym = False
            has_num = False
            has_outwards_sym = False
            has_outwards_num = False
            has_outwards_upper = False

            symbols = "".join(c for c in string.printable if not c in lower \
                    and not c in upper and not c in nums)
            non_print = "".join(chr(n) for n in range(1, 255) \
                    if not chr(n) in string.printable)

            for index in range(0, length):
                if full_words[index] in non_print:
                    return 254 ** x
                if full_words[index] in lower:
                    has_lower = True
                if full_words[index] in upper:
                    if index == 0 or index == (length - 1):
                        has_outwards_upper = True
                    else:
                        has_upper = True
                if full_words[index] in symbols:
                    if index == 0 or index == (length - 1):
                        has_outwards_sym = True
                    else:
                        has_sym = True
                if full_words[index] in nums:
                    if index == 0 or index == (length - 1):
                        has_outwards_num = True
                    else:
                        has_num = True
            if has_lower:
                complexity += 26
            if has_upper:
                complexity += 26
                has_outwards_upper = False
            if has_sym:
                complexity += 38
                has_outwards_sym = False
            if has_num:
                complexity += 10
                has_outwards_num = False
            if complexity == 0: complexity = 1
            combinations = complexity ** length
            if has_outwards_num:
                combinations *= 10
            if has_outwards_upper:
                combinations *= 26
            if has_outwards_sym:
                combinations *= 38
            return combinations

        def load_dict(book_path):
            try:
                with open(config.book_path) as f:
                    return f.readlines()
            except FileNotFoundError as f:
                print("\033[31m-" * 50)
                print("Error path: this flag only for linux.")
                print("-" * 50)
                quit()

        def min_complex_password(full_words):
            return len("".join(set(full_words))) ** len(full_words)

        def complex_zero(full_words):
            total = 0
            for x in range(0, len(full_words)):
                total += complex_password(full_words[x:])
            return total

        def min_zero(full_words):
            total = 0
            for x in range(0, len(full_words)):
                total += min_complex_password(full_words[x:])
            return total

        def calc_mozaiqa(value):
            mozaiqa = 0
            while value > 2:
                value >>= 1
                mozaiqa += 1
            return mozaiqa

        while True:
            div = 1
            words = load_dict(config)

            b = complex_password(self.a) / div
            c = min_complex_password(self.a)
            d = complex_zero(self.a) / div
            e = min_zero(self.a)
            f = math.log(complex_password(self.a) / div, 2)

            print("{} -> would approximately take {} tries to bruteforce knowing" \
                    "the exact length.".format(self.a, b))
            print("{} -> would approximately take {} tries to bruteforce by knowing" \
                    "the exact character set and length.".format(self.a, c))
            print("{} -> would approximately take {} tries to bruteforce without knowing" \
                    "the exact length or character set.".format(self.a, d))
            print("{} -> would approximately take {} tries to bruteforce by knowing" \
                    "the character set but not the length.".format(self.a, e))
            print("{} -> has ~{} bits of mozaiqa.".format(self.a, f))
            quit()
