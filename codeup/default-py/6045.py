b, n, m = map(int, input().split())

sum = b + n + m
avg = sum / 3

print(sum, end=' ')
print( format(avg, '.3f') )
