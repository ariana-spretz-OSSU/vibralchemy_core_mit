"""• Para agregar un track al final (.append):
add_track_to_end(playlist, track)
• Para insertar un track urgente al inicio (.insert(0, track)):
insert_priority_track(playlist, track)
• Para sacar el track actual o el último (.pop):
remove_last_track(playlist) (si sacás el último con .pop())
• Para auditar la memoria en consola (id()):
log_memory_state(playlist, action_label)
• Para la función orquestadora principal:
run_playback_simulation()"""

"""
Design a sequential playback queue simulator for Vibralchemy. 
Implement native `.append()`, `.pop()`, and `.insert(0, track)` methods 
to dynamically manipulate the track list in real time, 
printing the memory state to the console.
"""
playlist = ['528 Miracle Tone', '432 Pure Harmony', '396 Dissolve Fears', '417 Cellular Renewal', '741 Intuitive Awakening']

def add_track_to_end(playlist, track):
    playlist.append(track)
    return playlist

def insert_priority_track(playlist, track):
    playlist.insert(0, track)
    return playlist

def remove_last_track(playlist):
    playlist.pop()
    return playlist

def log_memory_state(playlist, action_label):
    if action_label == 'initial_state' or action_label == 'after_append_track_end' or action_label == 'after_priority_insert' or action_label == 'after_pop_track':
        print(playlist.id())


def run_playback_simulation():
    add_track_to_end(playlist, trackA)
    insert_priority_track(playlist, trackB)
    remove_last_track(playlist)
    log_memory_state(playlist, action_label)

print(run_playback_simulation(playlist, '480 Cognitive Clarity', '444 Master Key Realignment'))