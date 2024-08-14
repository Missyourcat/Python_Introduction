# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/21 下午11:39
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 编写一个程序，可以打印10句“你好，python”
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums, type(nums))
for i in nums:
    print("我爱python", i)
for i in [1, 2, 3, 4]:
    print("我爱python", i)

# 内存分析法
print(nums, id(nums), nums[0], id(nums[0]))
print(nums, id(nums), nums[1], id(nums[1]))
print(nums, id(nums), nums[2], id(nums[2]))
print(id(1))
nums2 = [1, 2]
print(nums2, id(nums2), nums2[0], id(nums[0]))
print(nums2, id(nums2), nums2[1], id(nums[1]))
