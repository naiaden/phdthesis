
#slm_in = 'compare-srilm-slm.c.slm_fulluniform.probs'
slm_in = '../utterance/compare-srilm-slm.slm_fulluniform.probs'

#srilm_in = 'compare-srilm-slm.c.srilm-out1'
srilm_in = '../utterance/compare-srilm-slm.srilm-out1'

#c_or_u = 'Concat'
c_or_u = 'Utterance'


# slm
slm_lines = []
current_line = []
with open(slm_in, 'r', encoding='iso-8859-1') as f:
    for line in f:
        if "<s> <s> <s>" in line:
            slm_lines.append(current_line)
            current_line = []
        current_line.append(2**float(line.rstrip().split(" = ")[1]))

first_slm_lines = []
for file in slm_lines:
    if file:
        first_slm_lines.append(file[0])

second_slm_lines = []
for file in slm_lines:
    if len(file) > 1:
        second_slm_lines.append(file[1])

third_slm_lines = []
for file in slm_lines:
    if len(file) > 2:
        third_slm_lines.append(file[2])

fourth_slm_lines = []
for file in slm_lines:
    if len(file) > 3:
        fourth_slm_lines.append(file[3])

last_slm_lines = []
for file in slm_lines:
    if len(file) > 3:
        last_slm_lines.append(file[-1])

second_to_last_slm_lines = []
for file in slm_lines:
    if len(file) > 3:
        second_to_last_slm_lines.append(file[-2])

third_to_last_slm_lines = []
for file in slm_lines:
    if len(file) > 3:
        third_to_last_slm_lines.append(file[-3])

fourth_to_last_slm_lines = []
for file in slm_lines:
    if len(file) > 3:
        fourth_to_last_slm_lines.append(file[-4])

rest_slm_lines = []
for file in slm_lines:
    if len(file) > 6:
        rest_slm_lines.append(file[3:-3])
rest_slm_lines = sum(rest_slm_lines, [])

# srilm
srilm_lines = []
current_line = []
with open(srilm_in, 'r', encoding='iso-8859-1') as f:
    for line in f:
        if line.startswith("\tp") and not "<s> | <s>" in line:
            if "| <s> ...)" in line:
                srilm_lines.append(current_line)
                current_line = []
            prob = line.rstrip().split(" [ ")[1].strip(" ]")
            if prob is not "-inf":
                current_line.append(10**float(prob))

first_srilm_lines = []
for file in srilm_lines:
    if file:
        first_srilm_lines.append(file[0])

second_srilm_lines = []
for file in srilm_lines:
    if len(file) > 1:
        second_srilm_lines.append(file[1])

third_srilm_lines = []
for file in srilm_lines:
    if len(file) > 2:
        third_srilm_lines.append(file[2])

fourth_srilm_lines = []
for file in srilm_lines:
    if len(file) > 3:
        fourth_srilm_lines.append(file[3])

last_srilm_lines = []
for file in srilm_lines:
    if len(file) > 3:
        last_srilm_lines.append(file[-1])

second_to_last_srilm_lines = []
for file in srilm_lines:
    if len(file) > 3:
        second_to_last_srilm_lines.append(file[-2])

third_to_last_srilm_lines = []
for file in srilm_lines:
    if len(file) > 3:
        third_to_last_srilm_lines.append(file[-3])

fourth_to_last_srilm_lines = []
for file in srilm_lines:
    if len(file) > 3:
        fourth_to_last_srilm_lines.append(file[-4])

rest_srilm_lines = []
for file in srilm_lines:
    if len(file) > 6:
        rest_srilm_lines.append(file[3:-3])
rest_srilm_lines = sum(rest_srilm_lines, [])

import numpy as np
import numpy.random
import matplotlib as mpl
#mpl.use('pgf')

import matplotlib.pyplot as plt

#plt.savefig('hallo.pgf')

f, ((ax11, ax12, ax13, ax14, ax15), (ax21, ax22, ax23, ax24, ax25)) = plt.subplots(2, 5, sharex=True, sharey=True)
f.suptitle(c_or_u + ": slm op x, srilm op y")
hb11 = ax11.hexbin(numpy.asarray(first_slm_lines), numpy.asarray(first_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax11.set_title('1e woord')

hb12 = ax12.hexbin(numpy.asarray(second_slm_lines), numpy.asarray(second_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax12.set_title('2e woord')

hb13 = ax13.hexbin(numpy.asarray(third_slm_lines), numpy.asarray(third_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax13.set_title('3e woord')

hb14 = ax14.hexbin(numpy.asarray(fourth_slm_lines), numpy.asarray(fourth_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax14.set_title('4e woord')

hb15 = ax15.hexbin(numpy.asarray(rest_slm_lines), numpy.asarray(rest_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax15.set_title('4e tem -3e woord')

hb21 = ax21.hexbin(numpy.asarray(last_slm_lines), numpy.asarray(last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax21.set_title('-3e woord')

hb22 = ax22.hexbin(numpy.asarray(second_to_last_slm_lines), numpy.asarray(second_to_last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax22.set_title('-2e woord')

hb23 = ax23.hexbin(numpy.asarray(third_to_last_slm_lines), numpy.asarray(third_to_last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax23.set_title('-1e woord')

hb24 = ax24.hexbin(numpy.asarray(fourth_to_last_slm_lines), numpy.asarray(fourth_to_last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
ax24.set_title('</s>')

cb = f.colorbar(hb24, ax=ax25)
cb.set_label('log10(N)')

plt.show()
