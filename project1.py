

sampleList = ['f','a','t','i','m','a']

def reverse(charList):
    leftIndex = 0
    rightIndex = len(charList) - 1

    while (leftIndex < rightIndex):
        charList[leftIndex], charList[rightIndex] = charList[rightIndex], charList[leftIndex]
        leftIndex += 1
        rightIndex -= 1

reverse(sampleList)
print(sampleList);

    
