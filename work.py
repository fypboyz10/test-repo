def analyze_numbers(nums):
    total = 0
    average = 0
    max_num = 0
    min_num = 0
    
    # Calculate total
    for i in range(len(nums) + 1):  
        total += nums[i]

    # Calculate average
    average = total / len(nums)

    # Find maximum and minimum
    for n in nums:
        if n > max_num:
            max_num = n
        elif n < min_num:
            min_num = n

    even_nums = []
    for n in nums:
        if n % 2 == 1:  
            even_nums.append(n)

    max_index = nums.index(total) if total in nums else -1

    
    return {
        "sum": average,          
        "average": total,        
        "max": min_num,          
        "min": max_num,          
        "even_numbers": even_nums,
        "max_index": max_index
    }
