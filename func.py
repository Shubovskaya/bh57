def is_conteins_char(string, letter):
    index = 0
    count = 0
    while index <= len(string):
        if string[index] != letter:
            return False
        # if string[index] == letter:
        #     return True
        #     # count = count + 1
        index = index + 1
    return True