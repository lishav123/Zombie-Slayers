from os import listdir

files = listdir("assets/protagonist/png/")
zombies = listdir("assets/enemy/male/")

class NinjaSprite:
    IDLE = sorted(list(filter(lambda x: "Idle" in x, files)))
    RUN  = sorted(list(filter(lambda x: "Run"  in x, files)))
    THROW = sorted(list(filter(lambda x: x.startswith("Throw"), files)))
    ATTACK = sorted(list(filter(lambda x: x.startswith("Attack"), files)))


class ZombieSprite:
    IDLE = sorted(list(filter(lambda x: "Idle" in x, zombies)))
    RUN  = sorted(list(filter(lambda x: "Walk" in x, zombies)))
    attack = sorted(list(filter(lambda x: "Attack" in x, zombies)))

if __name__ == '__main__':
    print("(Ninja Figures)", "=" * 20, sep="")
    print(f"Idle figure: {len(NinjaSprite.IDLE)}")
    print(f"Run  figure: {len(NinjaSprite.RUN)}")
    print(f"throw figure: {len(NinjaSprite.THROW)}")
    print(f"Attack figure: {len(NinjaSprite.ATTACK)}")
    print("\n(Zombie Figures)", "=" * 20, sep="")
    print(f"Idle Z figure: {len(ZombieSprite.IDLE)}")
    print(f"Walk Z figure: {len(ZombieSprite.RUN)}")
    print(f"Attack Z figure: {len(ZombieSprite().attack)}")
