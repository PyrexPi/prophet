from model import NoteModel
import numpy as np
import pyaudio as pa
from datetime import datetime
from pathlib import Path
import json
import os
from resource_path import resource_path


if __name__ == '__main__':
    my_file = Path(resource_path("sequence.txt"))
    if my_file.is_file():
        os.remove(my_file)

    # p = Process(target=interface.popup)
    # p.start()
    # p.join()

    model = NoteModel()

    p = pa.PyAudio()
    info = p.get_host_api_info_by_index(0)
    ndev = info.get('deviceCount')

    asked = False

    my_file = Path(resource_path("device.txt"))
    if my_file.is_file():
        with open(my_file, 'r') as f:
            input_index = int(f.readlines()[0])
    else:
        asked = True
        for i in range(0, ndev):
            print("Id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
        input_index = int(input("Choose your virtual device: "))

    if asked:
        keep = input("Do you want to keep your preferred device (delete device.txt to reset preferences) y/n: ")
        if keep in ['yes', 'Yes', 'y', 'Y']:
            with open(my_file, 'w') as f:
                f.write(str(input_index))

    encounter = input("Choose your encounter file ((t)emplar/(a)theon): ").lower()

    if encounter == 't':
        encounter = 'templar'
    elif encounter == 'a':
        encounter = 'atheon'

    with open(resource_path(encounter + '.json')) as f:
        oracle_map = json.load(f)

    if encounter == 'templar':
        time_threshold = 16
    else:
        time_threshold = 10

    stream = pa.PyAudio().open(format=pa.paInt16, channels=1, rate=44100, input=True, input_device_index=input_index,
                               frames_per_buffer=int(44100 / 2))
    current_note_string = []
    previous_string = []
    current_wave_list = []
    previous_max_length = 0
    start_time = datetime.now()
    send = False
    copy_previous_string = []

    while stream.is_active():
        new_wave = [np.frombuffer(stream.read(int(44100 / 2)), np.int16)]
        current_wave_list += new_wave
        if len(current_wave_list) >= 10:
            current_wave = np.concatenate(current_wave_list, axis=None)
            model.update_wave(current_wave)
            result = model.detect_note()
            current_result = result['note'].unique()
            current_note_string += current_result.tolist()
            current_note_string = list(dict.fromkeys(current_note_string))
            if len(current_note_string) > len(previous_string):
                previous_max_length = np.max([len(current_note_string), previous_max_length])
                send = previous_string != current_note_string
                # copy_previous_string = previous_string
                previous_string = current_note_string
                start_time = datetime.now()

            if (datetime.now() - start_time).seconds > time_threshold:
                current_wave_list = []
                previous_string = []
                current_note_string = []

        if (len(current_note_string) >= previous_max_length) & send:
            # print(current_note_string)
            print([oracle_map[x] for x in current_note_string])

            with open('sequence.txt', 'w+') as f:
                f.write('-'.join([str(oracle_map[x]) for x in current_note_string]))
