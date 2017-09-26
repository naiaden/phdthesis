tr1 = {}
te1 = {}

with open('train-1bw-t100.unigrams.freqs') as f:
    for pos, line in enumerate(f):
        (pattern, freq) = line.strip().split("\t")
        tr1[pattern] = (pos,freq)
    
with open('test-1bw.unigrams.freqs') as f:
    for pos, line in enumerate(f):
        (pattern, freq) = line.strip().split("\t")
        te1[pattern] = (pos,freq)

trj = {}
tej = {}

with open('train-jrc.unigrams.freqs') as f:
    for pos, line in enumerate(f):
        (pattern, freq) = line.strip().split("\t")
        trj[pattern] = (pos,freq)
    
with open('test-jrc.unigrams.freqs') as f:
    for pos, line in enumerate(f):
        (pattern, freq) = line.strip().split("\t")
        tej[pattern] = (pos,freq)

tre = {}
tee = {}

with open('train-emea.unigrams.freqs') as f:
    for pos, line in enumerate(f):
        (pattern, freq) = line.strip().split("\t")
        tre[pattern] = (pos,freq)
    
with open('test-emea.unigrams.freqs') as f:
    for pos, line in enumerate(f):
        (pattern, freq) = line.strip().split("\t")
        tee[pattern] = (pos,freq)

##

tr1te1 = {}
tr1tej = {}
tr1tee = {}
for pattern, tr1info in tr1.iteritems():
    (tr1pos, tr1freq) = tr1info
    tr1pos = int(tr1pos)
    tr1te1[tr1pos] = (tr1freq, te1.get(pattern, (0,0))[1])
    tr1tej[tr1pos] = (tr1freq, tej.get(pattern, (0,0))[1])
    tr1tee[tr1pos] = (tr1freq, tee.get(pattern, (0,0))[1])

trjte1 = {}
trjtej = {}
trjtee = {}
for pattern, trjinfo in trj.iteritems():
    (trjpos, trjfreq) = trjinfo
    trjte1[trjpos] = (trjfreq, te1.get(pattern, (0,0))[1])
    trjtej[trjpos] = (trjfreq, tej.get(pattern, (0,0))[1])
    trjtee[trjpos] = (trjfreq, tee.get(pattern, (0,0))[1])

trete1 = {}
tretej = {}
tretee = {}
for pattern, treinfo in tre.iteritems():
    (trepos, trefreq) = treinfo
    trete1[trepos] = (trefreq, te1.get(pattern, (0,0))[1])
    tretej[trepos] = (trefreq, tej.get(pattern, (0,0))[1])
    tretee[trepos] = (trefreq, tee.get(pattern, (0,0))[1])

##

import numpy

tr1counts = sorted(list(set(numpy.logspace(0,numpy.log10(len(tr1)),100).astype(int).tolist())))
trjcounts = sorted(list(set(numpy.logspace(0,numpy.log10(len(trj)),100).astype(int).tolist())))
trecounts = sorted(list(set(numpy.logspace(0,numpy.log10(len(tre)),100).astype(int).tolist())))

##

with open ('tr1-all', 'w') as f:
    f.write("tr1pos\ttr1val\tte1val\ttejval\tteeval\n")
    for i in tr1counts:
        tr1val = int(tr1te1[int(i-1)][0])
        te1val = int(tr1te1[int(i-1)][1])
        tejval = int(tr1tej[int(i-1)][1])
        teeval = int(tr1tee[int(i-1)][1])
        f.write(str(i-1) + "\t" + str(tr1val) + "\t" + str(te1val) + "\t" + str(tejval) + "\t" + str(teeval) + "\n")

with open ('trj-all', 'w') as f:
    f.write("trjpos\ttrjval\tte1val\ttejval\tteeval\n")
    for i in trjcounts:
        trjval = int(trjtej[int(i-1)][0])
        te1val = int(trjte1[int(i-1)][1])
        tejval = int(trjtej[int(i-1)][1])
        teeval = int(trjtee[int(i-1)][1])
        f.write(str(i-1) + "\t" + str(trjval) + "\t" + str(te1val) + "\t" + str(tejval) + "\t" + str(teeval) + "\n")

with open ('tre-all', 'w') as f:
    f.write("trepos\ttreval\tte1val\ttejval\tteeval\n")
    for i in trecounts:
        treval = int(tretee[int(i-1)][0])
        te1val = int(trete1[int(i-1)][1])
        tejval = int(tretej[int(i-1)][1])
        teeval = int(tretee[int(i-1)][1])
        f.write(str(i-1) + "\t" + str(treval) + "\t" + str(te1val) + "\t" + str(tejval) + "\t" + str(teeval) + "\n")
