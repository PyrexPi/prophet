import librosa
import numpy as np
from scipy import signal
import pandas as pd
# from matplotlib import pyplot as plt
import scipy.io.wavfile as sf
from resource_path import resource_path


class NoteModel:
    def __init__(self, wave=None, samples='samples', notes=('C', 'D', 'E', 'F', 'G', 'A', 'B'), sr=44100):
        self.wave = wave
        self.wave_notes = {}
        self.sr = sr
        self.detected_time = []
        self.detected_note = []

        for note in notes:
            self.wave_notes[note], _ = librosa.load(resource_path(samples) + '/' + note + '.wav', sr=sr)
            self.wave_notes[note] = self.wave_notes[note]/self.wave_notes[note].max()

    def update_wave(self, wave):
        self.wave = wave/wave.max()

    def remove_wave(self):
        self.wave = None

    def detect_note(self):
        self.detected_time = []
        self.detected_note = []
        for note in self.wave_notes.keys():
            note_detected = signal.correlate(self.wave, self.wave_notes[note])
            note_detected[note_detected < 500] = 0
            if sum(note_detected) > 0:
                times_detected = np.unique(np.trunc(np.where(note_detected > 0)[0] / self.sr)).tolist()
                self.detected_time += times_detected
                self.detected_note += [note] * len(times_detected)
                # print('Detected ' + note + str(np.count_nonzero(note_detected)) + ' times')
        return pd.DataFrame({'time': self.detected_time, 'note': self.detected_note}).set_index('time').sort_index()


if __name__ == '__main__':

    y, sr = librosa.load('audio/oracle_sample.mp3', sr=44100)
    # y_test, _ = librosa.load('audio/test_sample.mp3', sr=44100)

    model = NoteModel()
    model.update_wave(y)
    result = model.detect_note()
