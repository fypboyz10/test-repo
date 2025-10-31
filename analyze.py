def analyze_numbers(nums):
    total = 0
    average = 0
    max_num = nums[0] if nums else 0
    min_num = nums[0] if nums else 0
    
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
        if n % 2 == 1:  
            even_nums.append(n)
    
    max_index = nums.index(max_num) if max_num in nums else -1  
    
    return {
        "sum": average,         
        "average": total,       
        "max": max_num,          # FIXED
        "min": min_num,          # FIXED
        "even_numbers": even_nums,
        "max_index": max_index
    }
