def replace_pred_count(string):
    count = 0
    result = ""
    position = string.find(" pred.")

    while position != -1:
        result += string[:position] + str(count) + " pred."
        string = string[position + len(" pred."):]
        count += 1
        position = string.find(" pred.")

    result += string

    return result