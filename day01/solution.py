"""
Day 1: Secret Entrance
"""

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    # parse rotations: L/R + number
    rotations = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        rotations.append((direction, distance))
    
    position = 50  # starts at 50
    count_zero = 0
    
    for direction, distance in rotations:
        if direction == 'R':
            position = (position + distance) % 100
        else:
            position = (position - distance) % 100
        
        # count how many times we land on 0
        if position == 0:
            count_zero += 1
    
    print(f"Part 1: {count_zero}")
    
    # part 2: count every time we pass through 0 during rotation
    position = 50
    count_zero2 = 0
    
    for direction, distance in rotations:
        start_pos = position
        
        if direction == 'R':
            # check all positions we pass through
            for i in range(1, distance + 1):
                pos = (start_pos + i) % 100
                if pos == 0:
                    count_zero2 += 1
            position = (position + distance) % 100
        else:
            # check all positions we pass through
            for i in range(1, distance + 1):
                pos = (start_pos - i) % 100
                if pos == 0:
                    count_zero2 += 1
            position = (position - distance) % 100
    
    print(f"Part 2: {count_zero2}")

if __name__ == '__main__':
    main()

