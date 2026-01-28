from os import listdir

files = listdir("assets/protagonist/png/")
zombies = listdir("assets/enemy/male/")

class NinjaSprite:
    idle = sorted(list(filter(lambda x: "Idle" in x, files)))
    run  = sorted(list(filter(lambda x: "Run"  in x, files)))
    throw = sorted(list(filter(lambda x: "Throw" in x, files)))

class ZombieSprite:
    idle = sorted(list(filter(lambda x: "Idle" in x, zombies)))
    run  = sorted(list(filter(lambda x: "Run" in x, zombies)))
    attack = sorted(list(filter(lambda x: "Attack" in x, zombies)))

if __name__ == '__main__':
    print(f"Idle figure: {NinjaSprite().idle}")
    print(f"Run  figure: {NinjaSprite().run}")
    print(f"throw figure: {NinjaSprite().throw}")
    print(f"Idle Z figure: {ZombieSprite().idle}")
    print(f"Walk Z figure: {ZombieSprite().run}")
    print(f"Attack Z figure: {ZombieSprite().attack}")
