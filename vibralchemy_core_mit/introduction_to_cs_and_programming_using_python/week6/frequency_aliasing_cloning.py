"""
Write a script that compares an old list of audio frequencies against a new one. 
Intentionally trigger an aliasing bug by modifying a shared variable, 
then refactor the code using explicit cloning (`[:]` or `.copy()`) to ensure isolation.
"""

def simulate_aliasing_bug():
    old_frequencies = [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0]
    new_frequencies = old_frequencies
    print(f'Old frequencies are: {old_frequencies} and Id: {id(old_frequencies)}.')
    print(f'New frequencies after alliasing bug: {new_frequencies} and Id: {id(new_frequencies)}.')

    new_frequencies[-1] = 285.0

    print(f'Old frequencies after alliasing bug changing a value: {old_frequencies} and Id: {id(old_frequencies)}.')
    print(f'New frequencies after alliasing bug changing a value: {new_frequencies} and Id: {id(new_frequencies)}.')

def simulate_safe_cloning():
    old_frequencies = [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0]
    new_frequencies = old_frequencies.copy()
    print(f'Old frequencies are: {old_frequencies} and Id: {id(old_frequencies)}.')
    print(f'New frequencies after safe cloning: {new_frequencies} and Id: {id(new_frequencies)}.')
    
    new_frequencies[-1] = 285.0
    
    print(f'Old frequencies after safe cloning changing a value: {old_frequencies} and Id: {id(old_frequencies)}.')
    print(f'New frequencies after safe cloning changing a value: {new_frequencies} and Id: {id(new_frequencies)}.')
    
def run_memory_audit():
    simulate_aliasing_bug()
    simulate_safe_cloning()

run_memory_audit()

"""
Output:
Old frequencies are: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0] and Id: 140256098292096.
New frequencies after alliasing bug: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0] and Id: 140256098292096.
Old frequencies after alliasing bug changing a value: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 285.0] and Id: 140256098292096.
New frequencies after alliasing bug changing a value: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 285.0] and Id: 140256098292096.
Old frequencies are: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0] and Id: 140255919382272.
New frequencies after safe cloning: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0] and Id: 140255919381312.
Old frequencies after safe cloning changing a value: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0] and Id: 140255919382272.
New frequencies after safe cloning changing a value: [528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 285.0] and Id: 140255919381312.
"""