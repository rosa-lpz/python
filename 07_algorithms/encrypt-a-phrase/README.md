# Encrypt a Phrase

**A program in python that can codify a word by selecting letter position to the left and the right. The program uses the English alphabet.**



```python
# Function to codify a word by shifting all letters by the same amount
def codify_word(word, shift):
    # English alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Result string
    codified_word = ''
    
    # Loop through each letter in the word and apply the same shift
    for letter in word:
        # Check if the letter is an alphabet letter
        if letter.isalpha():
            # Convert the letter to lowercase for uniformity
            lower_letter = letter.lower()
            
            # Find the position of the letter in the alphabet
            current_index = alphabet.index(lower_letter)
            
            # Calculate the new position by applying the shift
            new_index = (current_index + shift) % len(alphabet)
            
            # Get the new letter from the alphabet
            new_letter = alphabet[new_index]
            
            # Maintain the original case (upper or lower)
            if letter.isupper():
                new_letter = new_letter.upper()
            
            # Append the new letter to the codified word
            codified_word += new_letter
        else:
            # If the character isn't a letter, leave it unchanged
            codified_word += letter
    
    return codified_word


word = input("Enter a word to codify: ")
shift = int(input("Enter the shift value (positive for right, negative for left): "))

# Apply the codification
codified_word = codify_word(word, shift)
print("Codified word:", codified_word)


```



## Tests

```cmd
# Test 1
Enter a word to codify: can
Enter the shift value (positive for right, negative for left): 2
Codified word: ecp

# Test 2
Enter a word to codify: go
Enter the shift value (positive for right, negative for left): 1
Codified word: hp
```

