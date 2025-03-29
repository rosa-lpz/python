def generate_permutations(input_string, current_string=""):
    if len(input_string) == 0:
        print(current_string, "\n")
        return
    for i in range(len(input_string)):
        remaining_string = input_string[:i] + input_string[i+1:]
        generate_permutations(remaining_string, current_string + input_string[i])

# Test 1
input_string = input() # cat
generate_permutations(input_string)
