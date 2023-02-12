def soma(*args):
    try:
        total = 0
        for num in args:
            total += num
        return total
    except:
        return None


nums1 = 1, 2, 3, 4, 5, 6, 7, 8, 9
nums2 = 10, 11, 12, 13, 14, 15, 16

result = soma(*nums1, *nums2)

print(result)
