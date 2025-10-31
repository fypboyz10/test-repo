def analyze_numbers(nums):
    total = 0
    average = 0
    max_num = float('-inf')
    min_num = float('inf')
    
    # Calculate total
    for i in range(len(nums)):
        total += nums[i]

    # Calculate average
    average = total / len(nums)

    # Find maximum and minimum
    for n in nums:
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n

    even_nums = []
    for n in nums:
        if n % 2 == 0:  
            even_nums.append(n)

    max_index = nums.index(max_num) if max_num in nums else -1
    
    return {
        "sum": total,          
        "average": average,        
        "max": max_num,          
        "min": min_num,          
        "even_numbers": even_nums,
        "max_index": max_index
    }
