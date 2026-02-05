from os import listdir

files = listdir("assets/protagonist/png/")
zombies = listdir("assets/enemy/male/")

class NinjaSprite:
    IDLE = sorted(list(filter(lambda x: "Idle" in x, files)))
    RUN  = sorted(list(filter(lambda x: "Run"  in x, files)))
    THROW = sorted(list(filter(lambda x: x.startswith("Throw"), files)))

class ZombieSprite:
    IDLE = sorted(list(filter(lambda x: "Idle" in x, zombies)))
    RUN  = sorted(list(filter(lambda x: "Walk" in x, zombies)))
    attack = sorted(list(filter(lambda x: "Attack" in x, zombies)))

if __name__ == '__main__':
    print(f"Idle figure: {len(NinjaSprite.IDLE)}")
    print(f"Run  figure: {len(NinjaSprite.RUN)}")
    print(f"throw figure: {NinjaSprite.THROW}")
    print(f"Idle Z figure: {ZombieSprite.IDLE}")
    print(f"Walk Z figure: {ZombieSprite.RUN}")
    print(f"Attack Z figure: {ZombieSprite().attack}")
