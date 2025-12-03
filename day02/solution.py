"""
Day 2: Gift Shop
"""

def generate_invalid_ids(max_num):
    """Generate all invalid IDs (digits repeated twice) up to max_num"""
    invalid = []
    k = 1
    
    while True:
        # for half-length k, generate IDs like: n * (10^k + 1)
        # where n goes from 10^(k-1) to 10^k - 1
        multiplier = 10**k + 1
        start_half = 10**(k-1)
        end_half = 10**k - 1
        
        # check if smallest invalid ID exceeds max
        smallest = start_half * multiplier
        if smallest > max_num:
            break
        
        for n in range(start_half, end_half + 1):
            invalid_id = n * multiplier
            if invalid_id > max_num:
                break
            invalid.append(invalid_id)
        
        k += 1
    
    return invalid

def main():
    with open('input.txt', 'r') as f:
        line = f.read().strip()
    
    # parse ranges
    ranges = []
    max_num = 0
    for range_str in line.split(','):
        if not range_str:
            continue
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
        max_num = max(max_num, end)
    
    # generate all invalid IDs up to max range
    invalid_ids = generate_invalid_ids(max_num)
    
    # find which invalid IDs fall in any range
    total = 0
    for invalid_id in invalid_ids:
        for start, end in ranges:
            if start <= invalid_id <= end:
                total += invalid_id
                break  # only count once even if in multiple ranges
    
    print(f"Part 1: {total}")

if __name__ == '__main__':
    main()

