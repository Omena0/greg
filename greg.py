# sourcery skip: for-append-to-extend
import random as r

names = ['Yousuuf gaimar', "Greg", "Gregory", "Useef gaimar"]

titleVerbs = ['Slayer', 'Destroyer', 'Obliterator']
titles_ = ["The .. of gods", "The .. of gregs", "The chosen one", "The greg", "The gregger"]
suffixes = ["the I", "the II", "the III", "the IV", "of the Greg", "of the Gregory"]

verbs = ["wrote", "developed", "created", "made", "invented", "did", "generated", "compiled", "implemented", "debugged", "programmed", "coded", "greg", "gregged", "did", "coped on", "is", "is not"]
adjectives = ["an amazing", "a cool", "an awesome", "a fantastic", "a great", "an incredible", "an outstanding", "a marvelous", "a superb", "a brilliant", "an insane", "a fire", "a greg", "a W", "a cool", "a real", "a fucking"]
things = ["game", "website", "script", "program", "software", "app", "AI", "robot", "machine learning model", "neural network", "greg", "greg generator", "programming language", "compiler", "interperter", "chat application", "thing"]

shuffle = False

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

    if shuffle: r.shuffle(gregs)
    return gregs


def greg():  # sourcery skip: for-append-to-extend
    """Greg generator"""
    gregs_did_what = []
    gregs = greg_names_frfr_ong()
    for greg in gregs:
        for verb in verbs:
            for adjective in adjectives:
                for thing in things:
                    gregs_did_what.append(f'{greg} {verb} {adjective} {thing}\n')

    if shuffle: r.shuffle(gregs_did_what)
    return gregs_did_what

gregs = greg()

if shuffle: r.shuffle(gregs)

with open('greg.txt','w') as f: f.writelines(gregs)
