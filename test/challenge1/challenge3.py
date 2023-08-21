def solve(word):
    def consonant_value(substring):
        value = 0
        for char in substring:
            value += ord(char) - ord('a') + 1
        return value
    
    consonant_substrings = []
    current_substring = ""
    
    for char in word:
        if char not in "aeiou":
            current_substring += char
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
            current_substring = ""
    
    if current_substring:
        consonant_substrings.append(current_substring)
    
    max_value = 0
    for substring in consonant_substrings:
        value = consonant_value(substring)
        if value > max_value:
            max_value = value
    
    return max_value
