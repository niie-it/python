counts = dict()
print('Enter a line of text:')
line = input('').lower()

# Pre-processing: Remove commas, question mark (?),
remove_pattern = ",!?.@#$%^&*()"
for item in remove_pattern:
    line = line.replace(item, "")

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)