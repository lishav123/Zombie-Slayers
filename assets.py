from os import listdir

files = listdir("assets/protagonist/png/")

class NinjaSprite:
    idle = sorted(list(filter(lambda x: "Idle" in x, files)))
    run  = sorted(list(filter(lambda x: "Run"  in x, files)))

if __name__ == '__main__':
    print(f"Idle figure: {NinjaSprite().idle}")
    print(f"Run  figure: {NinjaSprite().run}")
