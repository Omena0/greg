# sourcery skip: for-append-to-extend
from humanfriendly import format_timespan
from colorama import Fore
import subprocess as s
import random as r
import time as t
import roman
import os

os.system('')

def colored(text,color):
    return f'{color}{text}{Fore.RESET}'

names = ['Yousuuf gaimar', 'Greg', 'Gregory', 'Useef gaimar', 'Grug', 'Grugory']

titleVerbs = ['slayer', 'destroyer', 'obliterator', 'tearer', 'dismantler', 'killer', 'defeater', 'hero']
titles_ = ['The .. of gods', 'The .. of gregs', 'The .. of the Gregory', 'The .. of useef gaimar', 'The chosen one', 'The greg', 'The gregger']
suffixes = ['of the Greg', 'of the Gregory', 'of the Gregory greg greg']
#nuh uh adverbs = ['badly', 'horribly', 'really', 'terribly', 'wonderfully']

verbs = ['wrote', 'developed', 'created', 'made', 'invented', 'did', 'generated', 'compiled', 'implemented', 'debugged', 'programmed', 'coded', 'greg', 'gregged', 'did', 'coped on', 'is', 'is not', 'generated', 'will always be', 'will never be', 'planned']
adjectives = ['an amazing', 'a cool', 'an awesome', 'a fantastic', 'a great', 'an incredible', 'an outstanding', 'a marvelous', 'a superb', 'a brilliant', 'an insane', 'a fire', 'a greg', 'a W', 'a cool', 'a real', 'a fucking']
things = ['game', 'website', 'script', 'program', 'software', 'app', 'AI', 'robot', 'machine learning model', 'neural network', 'greg', 'greg generator', 'programming language', 'compiler', 'interpreter', 'chat application', 'thing', 'greem', 'idea']

shuffle = False

for i in range(10):
    suffixes.append(f'The {roman.toRoman(i+1)}')

titles = []
for title in titles_:
    if '..' not in title:
        titles.append(title)
        continue

    for verb in titleVerbs:
        titles.append(title.replace('..', verb))

def greg_names_frfr_ong():  # sourcery skip: for-append-to-extend
    """greg greg generator"""
    gregs = []
    for name in names:
        for title in titles:
            for suffix in suffixes:
                gregs.append(f'{name} {title} {suffix}')

    return gregs

def greg():  # sourcery skip: for-append-to-extend
    """Greg generator"""
    i = 0
    eta = 0
    old_time = t.time()
    old_i = 0
    progress = 0

    gregs_did_what = []
    gregs = greg_names_frfr_ong()
    
    total_lines = len(gregs)*len(verbs)*len(adjectives)*len(things)

    print(f'Generating {total_lines} of GREG')

    for greg in gregs:
        for verb in verbs:
            for adjective in adjectives:
                for thing in things:
                    gregs_did_what.append(f'{greg} {verb} {adjective} {thing}\n')
                    s.call(f'py {__file__}', shell=True)
                    i += 1

        percent = i/total_lines*100
        pbar = colored('#',Fore.GREEN)*int(percent)

        if i%100 == 0:
            progress = i-old_i
            dt = t.time() - old_time
            old_time = t.time()
            old_i = i
            eta = (total_lines - i) / (progress * dt + 0.0001)

        print(f'Generating: {round(percent,3):<5}% | GPS: {progress} | ETA: {format_timespan(eta,max_units=2):<20}',f'{pbar:.<100}'.replace('.',colored('#',Fore.LIGHTBLACK_EX)),end='\r')

    return gregs_did_what

gregs = []
for _ in range(1):
    gregs.extend(greg())

print('\nShuffling...')

if shuffle: r.shuffle(gregs)

print('Saving...')

with open('greg.txt','w') as f: f.writelines(gregs)
