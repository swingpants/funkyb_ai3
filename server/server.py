# 
# Copyright 2016 Google Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

from predict import generate_midi
import os
from flask import send_file, request
import pretty_midi
import sys
if sys.version_info.major <= 2:
    from cStringIO import StringIO
else:
    from io import StringIO
import time
import json

from flask import Flask
app = Flask(__name__, static_url_path='', static_folder=os.path.abspath('../static'))


@app.route('/predict', methods=['POST'])
def predict():
    now = time.time()
    values = json.loads(request.data)
    midi_data = pretty_midi.PrettyMIDI(StringIO(''.join(chr(v) for v in values)))
    duration = float(request.args.get('duration'))
    ret_midi = generate_midi(midi_data, duration)
    #print StringIO(''.join(chr(v) for v in values)), 'v', values, 'd', duration, 'md', midi_data, 'rm:',ret_midi
    return send_file(ret_midi, attachment_filename='return.mid', 
        mimetype='audio/midi', as_attachment=True)
#==============================================================================
# 
# #now: 1492603331.68 
# v [77, 84, 104, 100, 0, 0, 0, 6, 0, 0, 0, 1, 1, 224, 77, 84, 114, 107, 0, 0, 0, 19, 0, 255, 81, 3, 7, 161, 32, 0, 144, 48, 127, 0, 128, 48, 90, 0, 255, 47, 0] 
# d 1.0 
# md <pretty_midi.pretty_midi.PrettyMIDI object at 0x7f5cbc74e550> 
# rm: <open file '<fdopen>', mode 'w+b' at 0x7f5cbb3465d0>
# 
# 1492603428.8 
# v [77, 84, 104, 100, 0, 0, 0, 6, 0, 0, 0, 1, 1, 224, 77, 84, 114, 107, 0, 0, 0, 19, 0, 255, 81, 3, 7, 161, 32, 0, 144, 72, 127, 94, 128, 72, 90, 0, 255, 47, 0]
#  d 1.09866666667 
#  md <pretty_midi.pretty_midi.PrettyMIDI object at 0x7f5cbc74e8d0> 
#  rm: <open file '<fdopen>', mode 'w+b' at 0x7f5cbb3465d0>
# 
# 1492603761.03 
# v [77, 84, 104, 100, 0, 0, 0, 6, 0, 0, 0, 1, 1, 224, 77, 84, 114, 107, 0, 0, 0, 20, 0, 255, 81, 3, 7, 161, 32, 0, 144, 69, 127, 136, 28, 128, 69, 90, 0, 255, 47, 0] 
# d 2.192 md <pretty_midi.pretty_midi.PrettyMIDI object at 0x7f5cbb10dbd0> 
# rm: <open file '<fdopen>', mode 'w+b' at 0x7f5cbb3465d0>
#==============================================================================



@app.route('/', methods=['GET', 'POST'])
def index():
    return send_file('../static/index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
