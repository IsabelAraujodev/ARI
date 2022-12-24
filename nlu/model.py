import yaml
import numpy as np
data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'])
    outputs.append('{}'.format(command['entity'], command['action']))

#text proccess: words, characters, bytes, sub-words

chars = set()

for ch in inputs + outputs:
    if ch not in chars:
        chars.add(ch)
print('Número de chars:', len(chars))

#criar o data set
chr2idx 

'''
print(inputs)
print(outputs)
'''
