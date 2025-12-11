from collections import Counter
import re
import heapq
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break

    return lines

def extract_data(lines):
    data = []
    configurations = []
    joltages = []
    switches = []
    for line in lines:
        ind = line.find("]")
        config = line[1:ind]
        configurations.append(config)
        line = line[ind+1:]

        ind = line.find("{")
        joltages.append(list(map(int, line[ind + 1:-1].split(","))))
        line = line[:ind].strip()

        line = re.findall(r'\((.*?)\)', line)
        line = [list(map(int, line.split(","))) for line in line]
        #line = list(map(int, line[0].split(",")))
        switches.append(line)

    return configurations, switches, joltages

def find_minumum_toggle(switches, initial_state, target_state, switches_state):
    
    # Logic is not optimal complexity wise, but works for problem size

    if initial_state == target_state:
        return switches_state.count('1')

    switch_ind = len(switches_state)
    if switch_ind >= len(switches):
        return float('inf')
    
    toggled_state = list(initial_state)  
    for s in switches[switch_ind]:
        if toggled_state[s] == '#':
            toggled_state[s] = "."
        else:
            toggled_state[s] = "#"
    toggled_state = "".join(toggled_state)    

    num_toggles_0 = find_minumum_toggle(switches, initial_state, target_state, switches_state + "0")
    num_toggles_1 = find_minumum_toggle(switches, toggled_state, target_state, switches_state + "1")
    return min(num_toggles_0, num_toggles_1)

def optimize(switches, target):

    A = np.array([[1 if i in switch else 0 for switch in switches] for i in range(len(target))])
    b_u = np.array([i for i in target])
    b_l = np.array([i for i in target])
    c = np.array([1] * len(switches))
    lb = np.zeros_like(c)

    constraints = LinearConstraint(A, b_l, b_u)
    integrality = np.ones_like(c)
    bounds = Bounds(lb=lb)
    options = {"presolve": True, "mip_rel_gap": 1e-18}
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds, options = options)
    if res.success:
        ans = int(np.round(res.fun))
    else:
        raise RuntimeError("Optimization failed")    
    return ans

def solve_part_1(configurations, switches):
    ans = 0
    for i in range(len(configurations)):
        initial_state = "." * len(configurations[i])
        target_state = configurations[i]
        ans += find_minumum_toggle(switches[i], initial_state, target_state, "") 
    return ans
        
def solve_part_2(configurations, switches):
    ans = 0
    for i in range(len(configurations)):
        ans += optimize(switches[i], configurations[i])
    return ans

if __name__ == "__main__":
    print("AOC 2025 Day 10")
    lines = parse_input()
    configurations, switches, joltages = extract_data(lines)
    print("Part 1 Answer:", solve_part_1(configurations, switches))

    print("Part 2 Answer:", solve_part_2(joltages, switches))
    
    