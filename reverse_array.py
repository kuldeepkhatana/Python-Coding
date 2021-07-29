def revArray(a, start, end):

    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
a = [1,2,3,4,5,6,7]
print(a)
start = 0

end = len(a) - 1
print(end)
revArray(a,0,end)
print(a)
