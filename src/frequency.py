import matplotlib.pyplot as plt
import numpy as np

class PitchFrequency:
    notes = range(0, 12)
    A_freq = 440
    
    def get_freq(self):
        ret = []
        for r in range(-3, 3):
            base = self.A_freq * (2 ** r)
            ret.extend([base * (2 ** (note / 12)) for note in self.notes])
        return ret