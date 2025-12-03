"""
Day 2: Gift Shop
"""

def is_invalid_part2(n):
    """Check if ID is made of digits repeated at least twice"""
    s = str(n)
    length = len(s)
    
    # try all possible pattern lengths (must repeat at least 2 times)
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len != 0:
            continue
        
        num_repeats = length // pattern_len
        if num_repeats < 2:
            continue
        
        pattern = s[:pattern_len]
        # check if the whole string is just this pattern repeated
        if s == pattern * num_repeats:
            return True
    
    return False

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
    
    # part 2: check all numbers in ranges for repeating patterns
    total2 = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_part2(n):
                total2 += n
    
    print(f"Part 2: {total2}")

if __name__ == '__main__':
    main()

