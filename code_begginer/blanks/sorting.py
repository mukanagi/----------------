

def quick_sort(s):
    element = s[0]
    left = list(filter(lambda x: x < element, s))