fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']


def count_fruits(target):
    count = 0
    for fruit in fruits:
        if fruit == '사과':
            count += 1
    return count

print(count_fruits('수빅'))
