"""
Store the fixed Solfeggio frequencies of your channel in an immutable Tuple. 
Design a function using Lambda expressions that applies a floating-point multiplier factor to the elements, 
raising controlled exceptions if an attempt is made to mutate the base tuple.
"""
frequencies = (528.0, 432.0, 963.0, 396.0, 639.0, 417.0, 741.0, 852.0, 888.0, 174.0, 285.0, 936.0, 480.0, 444.0, 111.0, 221.2, 126.2, 333.0, 144.0, 421.3)

def apply_frequency_factor(frequencies, factor):
    applied_factor = tuple(map(lambda x: x * factor, frequencies))
    return applied_factor

def validate_tuple_immutability(frequencies, index, new_value):
    try:
        frequencies[index] = (new_value)
        return frequencies
    except TypeError:
        return ("Security Alert: Mutation attempt blocked. Base frequencies are immutable.")

def run_solfeggio_audit(frequencies, factor, index, new_value):
    scaled_frequencies = apply_frequency_factor(frequencies, factor)
    audit_status = validate_tuple_immutability(frequencies, index, new_value)
    return scaled_frequencies, audit_status

scaled_frequencies, audit_status = run_solfeggio_audit(frequencies, 2.0, 3, (888))
print(f"Scaled frequencies: {scaled_frequencies}\n{audit_status}")


"""
Output: Scaled frequencies: (1056.0, 864.0, 1926.0, 792.0, 1278.0, 834.0, 1482.0, 1704.0, 1776.0, 348.0, 570.0, 1872.0, 960.0, 888.0, 222.0, 442.4, 252.4, 666.0, 288.0, 842.6)
Security Alert: Mutation attempt blocked. Base frequencies are immutable.
"""