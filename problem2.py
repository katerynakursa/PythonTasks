def countSub(s:str, subStr:str) -> int:
    """Counts the number of times the substring occurs in the string
    :return: number of entries"""
    l = [i for i in range(len(s)) if s.startswith(subStr, i)]
    return len(l)

s = input('Enter your string:')
subStr = 'bob'
print('Number of times bob occurs in s: ', countSub(s, subStr))
