from random import randint

class Scene(object):
    
    def enter(self):
        print ("Hoofdstuk 1: De schatgrot")

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class dood(Scene):

    def enter(self):
        print ("U bent gestorven")
        exit(0)

class Grotingang(Scene):

    def enter(self):
        print ("U gaat via de grote boogingang naar binnen en ziet in de hoek een beer")

        action = input("Wat doet u? Ren Schiet Niks ")

        if action == "ren":
            print ("Bij het aanzicht van de beer neemt u meteen de benen")
            print ("Beren zijn helaas sneller als mensen")
            return 'dood'

        elif action == "schiet":
            print ("U pakt vliegensvlug uw pistool, en schiet op de beer")
            print ("De beer is niet onder de indruk en haalt uit")
            return 'dood'

        elif action == "niks":
            print ("Je doet niks en springt vervolgens toch, maar het dichtsbijzijnde gat in")
            return 'mijn_schacht'

        else:
            print ("kies uit: ren schiet niks>")
            return 'grot_ingang'


class mijnschacht(Scene):

    def enter(self):
        print ("Na een paar seconde in spanning valt u op de grond")
        print ("Als u om u heen kijkt ziet u dat u in een mijnschacht staat")
        print ("Tussen u en de rest van de mijnschacht staat een deur die alleen opengaat met een driecijferige code")
        code = "%d%d%d" % (randint(1,2), randint(1,2), randint(1,2))
        guess = input("Voer 3 cijfers tussen de 1 en 2 in> ")
        guesses = 0

        while guess != code and guesses < 10:
            print ("Errrr fout!")
            guesses += 1
            guess = input("Voer 3 cijfers tussen de 1 en 2 in> ")

        if guess == code:
            print ("De deur vliegt open! Deze code was juist")
            return 'diamant_grot'
        else:
            print ("Het slot weigert nu voor de laatste keer en u ziet iets in uw ooghoeken gebeuren")
            return 'dood'

class DiamantGrot(Scene):

    def enter(self):
        print ("U gaat door de deur van de mijnschacht")
        print ("Tot uw verbazing zie je overal diamanten voor het oprapen!")

        action = input("Wat doe je? Oprapen Juichen Niks> ")

        if action == "oprapen":
            print ("Vol verbazing pak je de diamant op en bekijkt hem wat beter")
            print ("Van dichtbij zie je dat het helemaal geen diamant is, maar een giftige steensoort")
            print ("Helaas komt u hier te laat achter")
            return 'dood'

        elif action == "juichen":
            print ("Bij het aanzien van al die diamanten begint u spontaan te juichen")
            print ("Door de echo begint de grot te beven")
            print ("Het plafond van de grot stort in")
            return 'dood'
        
        elif action == "niks":
            print ("U beslist niets met de diamanten te doen")
            print ("Als u wat langer naar de diamanten kijkt ziet u dat het een giftige steen is")
            print ("U besluit verder te lopen")
            return 'trol_grot'
        else:
            print ("Kies oprapen juichen of niks")
            return "diamant_grot"

class TrolGrot(Scene):

    def enter(self):
        print ("Na enige tijd lopen komt u in een grote open ruimte")
        print ("Overal op de grond liggen botten opgestapeld")
        print ("Uit de hoek van de ruimte komt een gestalte naar voren")

        good_pod = randint(1,2)
        guess = input("Kies optie 1 of 2> ")


        if int(guess) != good_pod:
            print ("De gestalte blijkt een trol te zijn")
            print ("De trol kijkt niet echt vriendelijk")
            return 'dood'
        else:
            print ("De gestalte blijkt een kat te zijn")
            print ("Achter de kat ziet u een schat liggen")
            return 'finished'

class Finished(Scene):

    def enter(self):
        print ("U heeft de grot overleeft")
        return 'finished'

class Map(object):

    scenes = {
        'grot_ingang': Grotingang(),
        'mijn_schacht': mijnschacht(),
        'diamant_grot': DiamantGrot(),
        'trol_grot': TrolGrot(),
        'dood': dood(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('grot_ingang')
a_game = Engine(a_map)
a_game.play()
