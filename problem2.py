def countSub(s, subStr):
    count = 0
    i = -1
    while True:
        i = s.find(subStr, i+1)
        if i == -1:
            return count
        count += 1

s = input('Enter your string:')
subStr = 'bob'
print('Number of times bob occurs in s: ', countSub(s, subStr))
