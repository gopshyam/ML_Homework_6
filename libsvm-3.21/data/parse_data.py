#! /usr/bin/env python


input_file = "../../OCRdata/ocr_fold0_sm_train.txt"

train_output_file = "train.txt"
validation_output_file = "validation.txt"

#Parses the input file to the correct format

def create_feature_string(features):
    features = features[2:]
    feat_str = ""
    for index in range(len(features)):
        feat_str += str(index + 1) + ':' + str(features[index]) + ' '
    return feat_str

lines = list()

with open(input_file, 'r') as tf:
    lines = tf.readlines()

train_length = int(len(lines) * 0.8)

with open(validation_output_file, 'w+') as tof:
    for line in lines[train_length:]:
        if (len(line) < 5):
            continue
        line_split = line.strip().split('\t')
        features = line_split[1]
        label = ord(line_split[2]) - ord('a')
        feature_string = create_feature_string(features)
        output_line = str(label) + " " + feature_string + "\n"
        tof.write(output_line)
