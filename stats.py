def word_count(text):
    return len(text.split())

def char_count(text):
    lower_text = text.lower()
    char_set = set(lower_text)
    count_dict = {}
    for char in char_set:
        count_dict[char] = lower_text.count(char)
    return count_dict