import time
from random import random as rand
from pylsl import StreamInfo, StreamOutlet
from muselsl.constants import MUSE_SCAN_TIMEOUT, AUTO_DISCONNECT_DELAY,  \
    MUSE_NB_EEG_CHANNELS, MUSE_SAMPLING_EEG_RATE, LSL_EEG_CHUNK,  \
    MUSE_NB_PPG_CHANNELS, MUSE_SAMPLING_PPG_RATE, LSL_PPG_CHUNK, \
    MUSE_NB_ACC_CHANNELS, MUSE_SAMPLING_ACC_RATE, LSL_ACC_CHUNK, \
    MUSE_NB_GYRO_CHANNELS, MUSE_SAMPLING_GYRO_RATE, LSL_GYRO_CHUNK

info = StreamInfo('BioSemi', 'EEG', 8, 100, 'float32', 'myuid34234')
outlet = StreamOutlet(info)

print("now sending data...")
while True:
    mysample = [rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()]
    outlet.push_sample(mysample)
    time.sleep(0.01)
