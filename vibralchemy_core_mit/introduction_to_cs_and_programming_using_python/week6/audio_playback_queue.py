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
print(playlist)

def add_track_to_end(playlist, track):
    playlist.append(track)
    return playlist
# print(playlist)

def insert_priority_track(playlist, track):
    playlist.insert(0, track)
    return playlist
# print(playlist)

def remove_last_track(playlist):
    playlist.pop()
    return playlist
# print(playlist)

def log_memory_state(playlist, action_label):
    if action_label == 'initial_state' or action_label == 'after_append_track_end' or action_label == 'after_priority_insert' or action_label == 'after_pop_track':
        print(f'Playlist id: {id(playlist)}')
# print(playlist)

def run_playback_simulation():
    log_memory_state(playlist, 'initial_state')
    add_track_to_end(playlist, '480 Cognitive Clarity')
    print(f'Playlist after add track to end. {playlist}')
    log_memory_state(playlist, 'after_append_track_end')
    insert_priority_track(playlist, '444 Master Key Realignment')
    print(f'Playlist after insert track to start. {playlist}')
    log_memory_state(playlist, 'after_priority_insert')
    remove_last_track(playlist)
    print(f'Playlist after remove track to end. {playlist}')
    log_memory_state(playlist, 'after_pop_track')

run_playback_simulation()

"""
Output:
['528 Miracle Tone', '432 Pure Harmony', '396 Dissolve Fears', '417 Cellular Renewal', '741 Intuitive Awakening']
Playlist id: 140362995279168
Playlist after add track to end. ['528 Miracle Tone', '432 Pure Harmony', '396 Dissolve Fears', '417 Cellular Renewal', '741 Intuitive Awakening', '480 Cognitive Clarity']
Playlist id: 140362995279168
Playlist after insert track to start. ['444 Master Key Realignment', '528 Miracle Tone', '432 Pure Harmony', '396 Dissolve Fears', '417 Cellular Renewal', '741 Intuitive Awakening', '480 Cognitive Clarity']
Playlist id: 140362995279168
Playlist after remove track to end. ['444 Master Key Realignment', '528 Miracle Tone', '432 Pure Harmony', '396 Dissolve Fears', '417 Cellular Renewal', '741 Intuitive Awakening']
Playlist id: 140362995279168
"""