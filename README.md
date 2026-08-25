


GLACIER GUARD
Mastery: 13,000
        │
        ├── Base Stats
        │
        ├── Commander Deck
        │      └── 20 Mods
        │
        ├── Army Deck
        │      └── 20 Mods
        │
        └── Shards
               ├── Slot 1
               ├── Slot 2
               ├── Slot 3
               ├── Slot 4
               └── Slot 5


# Aysel Combat Simulator

This project is a tiny Python prototype for the kind of systemic combat engine I want to investigate for Aysel Swarm.

The goal is small, honest, and useful: build a prototype that shows the core logic of the idea, not a polished game.

## What this demonstrates

- Unit data as a dictionary of stats
- Simple stat modifiers
- Total HP, damage, and DPS calculations for a battle
- A basic event system: trigger + condition + effect
- A card-like data structure representing a rules-driven ability

## The mental model

The core idea is:

> Something happened -> check a condition -> produce an effect.

That is the foundation of the eventual Aysel combat engine.

## Example flow

1. Unit: Crab Mech
2. Stats: HP, Damage, Fire Rate, Regen, Armor, Shield
3. Modifier: +1000 HP, +10 HP/s, +15% Fire Rate
4. Event: Damage Received
5. Condition: HP < 40%
6. Effect: Heal 10%
7. Result: HP is restored and the card enters cooldown

This is the beginning of a systemic combat design, not a full RTS or game implementation.

## How to run

From the project folder:

```bash
python main.py
```

## Why Python for Week 1

Python is a fast and friendly way to prototype game systems. It makes it easy to iterate quickly while learning logic, math, and data-driven design.
