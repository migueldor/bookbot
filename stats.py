def word_count(text):
    return len(text.split())

def char_count(text):
    lower_text = text.lower()
    char_set = set(lower_text)
    count_dict = {}
    for char in char_set:
        count_dict[char] = lower_text.count(char)
    return count_dict


def char_count_dict_list(char_dict):
    chars = []
    for char in char_dict:
        single_char_dict = {"char": char, "num": char_dict[char]}
        chars.append(single_char_dict)
    return chars