sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonent_count = 0

for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:" , vowel_count)
print("Consonents" , consonent_count)

