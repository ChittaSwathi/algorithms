#overlapping intervals
#non-overlapping intervals


intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)]  

intervals.sort(key = lambda x: x[1])

end = 0
res = []

for interval in intervals:
    if end <= interval[0]:
        res += [interval]
        end = interval[1]

print('Number of intervals that can be scheduled ,',len(res))
print('List of intervals are --', res)