"""
Write a modular audio metadata engine. 
Program a master function that takes a list of technical data and
a helper function acting as a filter (e.g., a decibel filter),
while validating memory scope isolation.
"""
decibels = [-6.0, -14.5, -2.1, -24.0, -0.5, -36.0, -29.7, -10.6, -30.4, -18.5, -22.0, -15.3, -20.5, -10.0, -12.8, -26.2, -28.9, -32.0, -40.0, -1.1]

def is_unclipped(db):
    threshold = -3.0
    if db < threshold:
        return True
    else:
        return False  

print(is_unclipped(-15)) # Output: True
print(is_unclipped(-2)) # Output: False

def is_suitable_for_deep_sleep(db):
    friendly_threshold = -18.0
    if db < friendly_threshold:
        return True
    else:
        return False

print(is_suitable_for_deep_sleep(-25)) # Output: True
print(is_suitable_for_deep_sleep(-12)) # Output: False

def modular_audio_metadata_engine(list, f):
    filtered_db = []
    for db in list:
        if f(db):
            filtered_db.append(db)
    return filtered_db
 
print(modular_audio_metadata_engine(decibels, is_unclipped)) # Output: [-6.0, -14.5, -24.0, -36.0, -29.7, -10.6, -30.4, -18.5, -22.0, -15.3, -20.5, -10.0, -12.8, -26.2, -28.9, -32.0, -40.0]
print(modular_audio_metadata_engine(decibels, is_suitable_for_deep_sleep)) # Output: [-24.0, -36.0, -29.7, -30.4, -18.5, -22.0, -20.5, -26.2, -28.9, -32.0, -40.0]
print(f'The original list you passed as an argument was neither altered nor destroyed by the engine. {decibels}') # Output: [-6.0, -14.5, -2.1, -24.0, -0.5, -36.0, -29.7, -10.6, -30.4, -18.5, -22.0, -15.3, -20.5, -10.0, -12.8, -26.2, -28.9, -32.0, -40.0, -1.1]
print(f'Demonstrating that the scopes are isolated and there are no memory leaks into the global environment. {filtered_db}') # Output: NameError: name 'filtered_db' is not defined



