def canJump(nums):
    count = 0
    for n in nums:
        print(f'{n}, {count}')
        if count < 0:
            return False
        elif n > count:
            count = n
        count -= 1
        print(count)
    return True


#__main__
length = int(input())
nums = list(map(int,input().split(" ")))
print(canJump(nums))