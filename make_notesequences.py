#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:09:11 2017

@author: swingpants
"""

from magenta.scripts import convert_dir_to_note_sequences

print 'Converting midi to notesequence'
INPUT_DIRECTORY='./data/midi/'#<folder containing MIDI and/or MusicXML files. can have child folders.>

# TFRecord file that will contain NoteSequence protocol buffers.
SEQUENCES_TFRECORD='notesequences.tfrecord'

convert_dir_to_note_sequences 
#--input_dir=$INPUT_DIRECTORY --output_file=$SEQUENCES_TFRECORD --recursive

Training model:
/tmp/melody_rnn/logdir/run1/train

Create NoteSequences
python /usr/local/lib/python2.7/dist-package/magenta/scripts/convert_dir_to_note_sequences --input_dir=./data/midi --output_file=./notesequences.tfrecord --recursive

Create Sequence Examples
python /usr/local/lib/python2.7/dist-packages/magenta/models/melody_rnn/melody_rnn_create_dataset.py --config='attention_rnn' --input=./notesequences.tfrecord --output_dir=./server --eval_ratio=0.10

Train and Evaluate Model
python /usr/local/lib/python2.7/dist-packages/magenta/models/melody_rnn/melody_rnn_train.py --config=attention_rnn --run_dir=/tmp/melody_rnn/logdir/run1 --sequence_example_file=./server/training_melodies.tfrecord --hparams="{'batch_size':64,'rnn_layer_sizes':[64,64]}" --num_training_steps=20000
                                                                                                                                                                                                                                
Generate Melody
single note primer:
python /usr/local/lib/python2.7/dist-packages/magenta/models/melody_rnn/melody_rnn_generate.py --config=attention_rnn --run_dir=/tmp/melody_rnn/logdir/run1 --output_dir=/tmp/melody_rnn/generated --num_outputs=10 --num_steps=128 --hparams="{'batch_size':64,'rnn_layer_sizes':[64,64]}" --primer_melody="[60]"

Twinkle twinkle primer:
python /usr/local/lib/python2.7/dist-packages/magenta/models/melody_rnn/melody_rnn_generate.py --config=attention_rnn --run_dir=/tmp/melody_rnn/logdir/run1 --output_dir=/tmp/melody_rnn/generated --num_outputs=10 --num_steps=128 --hparams="{'batch_size':64,'rnn_layer_sizes':[64,64]}" --primer_melody="[60, -2, 60, -2, 67, -2, 67, -2]"

                                                                                                                                                                                                                                               
Create a Bundle file
python /usr/local/lib/python2.7/dist-packages/magenta/models/melody_rnn/melody_rnn_generate.py --config=attention_rnn --run_dir=/tmp/melody_rnn/logdir/run1 --hparams="{'batch_size':64,'rnn_layer_sizes':[64,64]}" --bundle_file=/tmp/attention_rnn.mag --save_generator_bundle  
                                                                                              