# project : phone number extractor from the text



text = input("Enter any text with phone numbers: ")

# Remove punctuation symbols
cleaned_text = ""
for char in text:
    if char.isdigit() or char.isspace():
        cleaned_text += char
    else:
        cleaned_text += ' '

# Now split and check for 10-digit numbers
words = cleaned_text.split()

numbers = [word for word in words if len(word) == 10]

if numbers:
    print("10-digit phone numbers found:")
    for number in numbers:
        print(number)
else:
    print("No 10-digit phone numbers found.")


# Example usage
#Hi, my name is Mann and my phone number is 9876543210. My friend Heli can be contacted at 8765432109. Divyang is also a close friend, his number is 9988776655. Roshni's phone number is 9123456789. Vishvjit stays in touch at 9090909090, and Kanho recently shared his number as 9191919191. We’re all good friends and always stay connected.
