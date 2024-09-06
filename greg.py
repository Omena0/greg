import random

names = ["Greg"]
verbs = ["wrote", "developed", "created", "made", "invented", "did", "generated", "compiled", "implemented", "debugged", "programmed", "coded", "greg", "gregged", "did"]
adjectives = ["an amazing", "a cool", "an awesome", "a fantastic", "a great", "an incredible", "an outstanding", "a marvelous", "a superb", "a brilliant", "an insane", "a fire", "greg", "a W", "a cool", "a real"]
things = ["game", "website", "script", "program", "software", "app", "AI", "robot", "machine learning model", "neural network", "greg", "greg generator", "programming language", "compiler", "interperter", "chat application"]


def greg():
    """Greg generator"""
    gregs = []
    for name in names:
        for verb in verbs:
            for adjective in adjectives:
                for thing in things:
                    gregs.append(f'{name} {verb} {adjective} {thing}\n')
    return gregs

i = 0

try:
    gregs = greg()
except KeyboardInterrupt: ...

with open('greg.txt','w') as f: f.writelines(gregs)
