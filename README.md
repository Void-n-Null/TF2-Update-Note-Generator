# TF2-Update-Note-Generator

A simple markov chain based generator for generating Team Fortress 2 Update Notes. 

Uses the markovify python module and a dataset gathered by me from https://www.teamfortress.com/

To use, first install markovify  ```pip install markovify```

and then run main.py by doing ```python main.py``` or ```python3 main.py```

Here are some examples of the things generated
```
> Fixed the Festive Sapper not having their items removed when they enter spectator mode.
> Added a server crash caused by setting sv_enableboost to 1.
> Fixed an exploit related to sentry rockets in the future.
> Milk will no longer build teleporters behind the spawn door.
> Fixed problem in which the code worked.
> Jarate Extinguishing an ally will now return 20 health to the spy sapper.
> Fixed a bug which caused demos to crash.  
> Consecutive Airblasts will no longer randomly crit.
> Fixed switching to the Rocket Jumper.
> CPU overheating can now be gift wrapped.
```
<sub>written in Python 3.10</sub>
