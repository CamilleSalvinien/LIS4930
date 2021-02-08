firstString = str(input())
insertString = str(input())

middle = int(len(firstString)/2)
newSentence = firstString[:middle] + insertString + firstString[middle:]

print(newSentence)
