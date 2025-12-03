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

if __name__ == '__main__':
    main()

