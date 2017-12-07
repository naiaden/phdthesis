


# slm
slm_lines = []
current_line = []
with open('compare-srilm-slm.c.slm_fulluniform.probs', 'r', encoding='iso-8859-1') as f:
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
with open('compare-srilm-slm.c.srilm-out1', 'r', encoding='iso-8859-1') as f:
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

f, axarr = plt.subplots(2, 5)
axarr[0, 0].hexbin(numpy.asarray(first_slm_lines), numpy.asarray(first_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[0, 0].set_title('Axis [0,0]')

axarr[0, 1].hexbin(numpy.asarray(second_slm_lines), numpy.asarray(second_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[0, 1].set_title('Axis [0,1]')

axarr[0, 2].hexbin(numpy.asarray(third_slm_lines), numpy.asarray(third_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[0, 2].set_title('Axis [0,2]')

axarr[0, 3].hexbin(numpy.asarray(fourth_slm_lines), numpy.asarray(fourth_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[0, 3].set_title('Axis [0,3]')

axarr[0, 4].hexbin(numpy.asarray(rest_slm_lines), numpy.asarray(rest_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[0, 4].set_title('Axis [0,4]')

axarr[1, 0].hexbin(numpy.asarray(last_slm_lines), numpy.asarray(last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[1, 0].set_title('Axis [1,0]')

axarr[1, 1].hexbin(numpy.asarray(second_to_last_slm_lines), numpy.asarray(second_to_last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[1, 1].set_title('Axis [1,1]')

axarr[1, 2].hexbin(numpy.asarray(third_to_last_slm_lines), numpy.asarray(third_to_last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[1, 2].set_title('Axis [1,2]')

axarr[1, 3].hexbin(numpy.asarray(fourth_to_last_slm_lines), numpy.asarray(fourth_to_last_srilm_lines),gridsize=15, bins='log', xscale='log', yscale='log')
axarr[1, 3].set_title('Axis [1,3]')
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
plt.show()
