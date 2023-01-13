import sys
import statistics
def stat():
    filepath = str(sys.argv[1])
    numbers = []
    with open(filepath, 'r') as f:
        for line in f:
            numbers.append(int(line))
    meann = statistics.mean(numbers)
    std = statistics.stdev(numbers)
    minn = min(numbers)
    maxx = max(numbers)
    print('Statistics Summary')
    print('mean:', meann)
    print('std:', std)
    print('min:', minn)
    print('max:', maxx)
stat()
