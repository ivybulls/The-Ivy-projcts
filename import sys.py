import sys

def solve():
    # Read n
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # Use a set to store unique levels passed
    passed_levels = set()
    
    # Process Little X's levels
    p = int(input_data[1])
    for i in range(p):
        passed_levels.add(int(input_data[2 + i]))
        
    # Process Little Y's levels
    # Offset starts after n, p, and X's p levels
    q_index = 2 + p
    q = int(input_data[q_index])
    for i in range(q):
        passed_levels.add(int(input_data[q_index + 1 + i]))
    
    # Check if they covered all levels from 1 to n
    if len(passed_levels) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
age=sys.stdin.readline().strip()
solve()

age=

