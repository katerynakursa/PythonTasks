def findLongest(s:str) -> str:
    """Find the longest substring of s in which letters occur in alphabetical order
    :param s: entered string
    :return: the longest substring"""
    longestSubstr = ''
    orderSubstr = ''
    prev = ''
    for i in s:
        if i >= prev:
            orderSubstr += i
            if len(longestSubstr) < len(orderSubstr):
                longestSubstr = orderSubstr
        else:
            orderSubstr = i
        prev = i
    return longestSubstr

s = input('Enter your string: ')
print('Longest substring in alfabetical order is: ', findLongest(s))