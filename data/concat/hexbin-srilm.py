utterances = []
cur_utterance = []

with open('utterance/compare-srilm-slm.u.srilm-out1', 'r', encoding='iso-8859-1') as f:
    for line in f:
        if line.startswith("\tp") and not "<s> | <s>" in line:
            if "| <s> ...)" in line:
                utterances.append(cur_utterance)
                cur_utterance = []
            split = line.strip().split("\t= ")
            pattern = split[0].strip()
            prob = split[1].split(" [ ")[1].replace(" ]", "")
            cur_utterance.append([pattern, prob])
        
    utterances.append(cur_utterance)

all_concat = []

with open('concat/compare-srilm-slm.c.srilm-out1', 'r', encoding='iso-8859-1') as f:
    for line in f:
        if line.startswith("\tp") and not "<s> | <s>" in line:
            split = line.strip().split("\t= ")
            pattern = split[0].strip()
            prob = split[1].split(" [ ")[1].replace(" ]", "")
            all_concat.append([pattern, prob])


all_counter = 0

first_words = []
second_words = []
third_words = []
fourth_words = []

rest_words = []

third_to_last_words = []
second_to_last_words = []
first_to_last_words = []
last_words = []
last_words_clear = []

for utterance in utterances[1:]:
    for pc, pattern in enumerate(utterance):
        if pattern[0] == all_concat[all_counter][0] or "<s>" in pattern[0]:
            if pc == 0:
                first_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
                #print(pattern[0] + "\t" + all_concat[all_counter][0])
            if pc == 1:
                second_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            if pc == 2:
                third_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            if pc == 3:
                fourth_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            if pc >= 3 and pc <= len(utterance)-4:
                rest_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            if pc == len(utterance)-4:
                third_to_last_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            if pc == len(utterance)-3:
                second_to_last_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            if pc == len(utterance)-2:
                first_to_last_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            if pc == len(utterance)-1:
                last_words.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
                #print(pattern[0] + "\t" + all_concat[all_counter][0])
            if len(utterance) > 4 and pc == len(utterance)-1:
                last_words_clear.append([2**float(pattern[1]),2**float(all_concat[all_counter][1])])
            all_counter += 1


import numpy as np
import numpy.random
import matplotlib as mpl
#mpl.use('pgf')

import matplotlib.pyplot as plt







c_or_u = "SRILM"
f, ((ax11, ax12, ax13, ax14, ax15), (ax21, ax22, ax23, ax24, ax25)) = plt.subplots(2, 5, sharex=True, sharey=True)
f.suptitle(c_or_u + ": utterance op x, concat op y")
hb11 = ax11.hexbin(numpy.asarray(first_words)[:,0], numpy.asarray(first_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax11.set_title('1e woord')

hb12 = ax12.hexbin(numpy.asarray(second_words)[:,0], numpy.asarray(second_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax12.set_title('2e woord')

hb13 = ax13.hexbin(numpy.asarray(third_words)[:,0], numpy.asarray(third_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax13.set_title('3e woord')

hb14 = ax14.hexbin(numpy.asarray(fourth_words)[:,0], numpy.asarray(fourth_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax14.set_title('4e woord')

hb15 = ax15.hexbin(numpy.asarray(rest_words)[:,0], numpy.asarray(rest_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax15.set_title('4e tem -3e woord')

hb21 = ax21.hexbin(numpy.asarray(third_to_last_words)[:,0], numpy.asarray(third_to_last_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax21.set_title('-3e woord')

hb22 = ax22.hexbin(numpy.asarray(second_to_last_words)[:,0], numpy.asarray(second_to_last_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax22.set_title('-2e woord')

hb23 = ax23.hexbin(numpy.asarray(first_to_last_words)[:,0], numpy.asarray(first_to_last_words)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax23.set_title('-1e woord')

hb24 = ax24.hexbin(numpy.asarray(last_words_clear)[:,0], numpy.asarray(last_words_clear)[:,1],gridsize=15, bins='log', xscale='log', yscale='log')
ax24.set_title('-1e woord (lengte utt > 4)')

cb = f.colorbar(hb24, ax=ax25)
cb.set_label('log10(N)')

plt.show()
