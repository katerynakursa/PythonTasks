def vowelsCount(s):
    count = 0
    for i in s:
        if i in 'aeiou':
            count += 1
    return count

if __name__ == '__main__':
    s = input('enter the string:')

    print('Number of vowels:aa %s' % vowelsCount(s))


