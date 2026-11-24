"""
Store the fixed Solfeggio frequencies of your channel in an immutable Tuple. 
Design a function using Lambda expressions that applies a floating-point multiplier factor to the elements, 
raising controlled exceptions if an attempt is made to mutate the base tuple.
"""
frequencies = (528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0, 285.0, 936.0, 480.0, 444.0, 111.0, 221.2, 126.2, 333.0, 144.0, 421.3)

def apply_frequency_factor(frequencies, factor):
    applied_factor = tuple(map(lambda x: x * factor, frequencies))
    return applied_factor
print(apply_frequency_factor(528.0, 0.5))

def validate_tuple_immutability(frequencies):
    try:
        frequencies[0] = 432
    except TypeError:
        print("Security Alert: Mutation attempt blocked. Base frequencies are immutable.")