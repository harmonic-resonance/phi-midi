import phimidi as pm

VOICES = {
    'Solo Ooh': {'bank': 1, 'subbank': 0, 'channel': 8, 'program': 0},
    'Solo Aah': {'bank': 1, 'subbank': 0, 'channel': 10, 'program': 1},
    'Mixed Choir': {'bank': 1, 'subbank': 0, 'channel': 11, 'program': 2},
    'Little Swell Choir': {'bank': 1, 'subbank': 0, 'channel': 12, 'program': 3},
    'Swell Choir': {'bank': 1, 'subbank': 0, 'channel': 13, 'program': 4},
    'Choir Ooh': {'bank': 1, 'subbank': 0, 'channel': 14, 'program': 5},
    'Choir Aah': {'bank': 1, 'subbank': 0, 'channel': 15, 'program': 6},
}

def add_voice_track(mf, name='Mixed Choir'):
    track = pm.set_new_track(mf, name=name)
    v = VOICES[name]
    
    track.append(pm.Message(
        'control_change', 
        control =  0, 
        value = v['bank'], 
        channel = v['channel'], 
        time = 0
    ))
    track.append(pm.Message(
        'control_change', 
        control = 32, 
        value = v['subbank'], 
        channel = v['channel'], 
        time = 0
    ))
    track.append(pm.Message(
        'program_change', 
        program = v['program'],
        channel = v['channel'], 
        time = 1))
    return track

def add_voice_note(track, note, velocity=64, duration=1920):
    v = VOICES[track.name]
    pm.set_note(track, note, channel=v['channel'], velocity=64, duration=duration)

def add_voice_chord(track, root, chord='Major', velocity=64, duration=1920):
    v = VOICES[track.name]
    # pm.set_note(track, note, channel=v['channel'], duration=1920*2)
    pm.set_chord(track, root=root, chord=chord, channel=v['channel'], velocity=64, duration=duration)
 
