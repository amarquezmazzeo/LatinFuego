calls, intervals = [int(number) for number in input().split(" ")]
while (calls != 0 and intervals != 0):
    call_list = [] # store sets here
    for i in range(calls):
        S, D, start, duration = [int(number) for number in input().split(" ")]
        call_list.append([start, start+duration])
    for i in range(intervals):
        count = 0
        start, duration = [int(number) for number in input().split(" ")]
        interval = [start, start+duration]
        # Check calls in interval
        for j in call_list:
            if interval[0] < j[0] < interval[1] or interval[0] < j[1] < interval[1] or (interval[1] <= j[1] and interval[0] >= j[0]):
                count += 1 
        print(count)

    calls, intervals = [int(number) for number in input().split(" ")]