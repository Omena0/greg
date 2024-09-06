
# Greg generator

```py
import random

def greg():
    """Greg generator"""
    names = ["Greg"]
    verbs = ["wrote", "developed", "created", "made", "invented", "did"]
    adjectives = ["amazing", "cool", "awesome", "fantastic", "great", "incredible", "outstanding", "marvelous", "superb", "brilliant"]
    things = ["a game", "a website", "a script", "a program", "a software", "an app", "an AI", "a robot", "a machine learning model", "a neural network"]
    return "{} {} {} {}".format(random.choice(names), random.choice(verbs), random.choice(adjectives), random.choice(things))
```
