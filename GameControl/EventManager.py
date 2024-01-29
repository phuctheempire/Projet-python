import pygame as pg
import sys

pg.init()

# Gestion de la musique
pg.mixer.init()

selected_value_index = None
from GameControl.setting import Setting
from GameControl.game import *
from GameControl.gameControl import GameControl
from view.world import *
from view.utils import *
from Tiles.Bob import *
from Tiles.tiles import *
from GameControl.saveAndLoad import *
# Couleurs  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PATH = "assets/menu/"

setting = Setting.getSettings()
gameController = GameControl.getInstance()
# Ajoutez cette variable globale
return_to_menu = False


# Création de la fenêtre en plein écran
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption("Game Menu")

# Charger l'image de fond, plusieurs images disponibles dans le dossier (à en choisir une)
background_image = pg.image.load(PATH + "back2.png")
background_image = pg.transform.scale(background_image, screen.get_size())

# Charger la musique de fond
pg.mixer.music.load( PATH + "song.mp3")
pg.mixer.music.set_volume(0.5)  # Le volume de 0.0 à 1.0
pg.mixer.music.play(-1)  # -1 pour jouer en boucle

# Police pour les boutons
font = pg.font.Font(None, 40)

# Déclaration des rectangles des boutons de base
button_width, button_height = 300, 50
play_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 200, button_width, button_height)
settings_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 300, button_width, button_height)
quit_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 400, button_width, button_height)
# back_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 500, button_width, button_height)
back_button_rect = pg.Rect(20, 20, button_width, button_height)
stop_music_button_rect = pg.Rect(back_button_rect.right + 10, 20, button_width, button_height)
play_music_button_rect = pg.Rect(stop_music_button_rect.right + 10, 20, button_width, button_height)
increase_brightness_button_rect = pg.Rect(play_music_button_rect.right + 10, 20, button_width, button_height)
decrease_brightness_button_rect = pg.Rect(increase_brightness_button_rect.right + 10, 20, button_width, button_height)

grid_value_rects = dict()  # Réinitialise la liste des rectangles

# Déclaration des labels des grilles (à modifier en fonction du contenu de notre jeu, voir résumé du pdf du prof)
# grid_labels = ["GRID LENGTH", 
#                "NUMBER BOB","NUMBER SPAWNED FOOD",  "FOOD ENERGY" ,
#                "BOB SPAWN ENERGY", "BOB MAX ENERGY" ,"BOB NEWBORN ENERGY", "SEXUAL BORN ENERGY", "BOB STATIONARY ENERGY LOSS", "BOB SELF REPRODUCTION ENERGY LOSS", "BOB SEXUAL REPRODUCTION LOSS", "BOB SEXUAL REPRODUCTION LEVEL",
#                "PERCEPTION FLAT PENALTY", "MEMORY FLAT PENALTY",  
#                "DEFAULT VELOCITY", "DEFAULT MASS", "DEFAULT VISION", "DEFAULT MEMORY POINT", 
#                "MASS VARIATION", "VELOCITY VARIATION", "VISION VARIATION" , "MEMORY VARIATION", 
            #    "SELF_REPRODUCTIO","SEXUAL REPRODUCTION" ]
grid_dict = { "FPS": setting.getFps() ,"GRID LENGTH": setting.getGridLength(),
               "NUMBER BOB": setting.getNbBob(), "NUMBER SPAWNED FOOD": setting.getNbSpawnFood(),  "FOOD ENERGY": setting.getFoodEnergy(),
               "BOB SPAWN ENERGY": setting.getBobSpawnEnergy(), "BOB MAX ENERGY": setting.getBobMaxEnergy() ,"BOB NEWBORN ENERGY": setting.getBobNewbornEnergy(), "SEXUAL BORN ENERGY": setting.getSexualBornEnergy(), 
               "BOB STATIONARY ENERGY LOSS": setting.getBobStationaryEnergyLoss(), "BOB SELF REPRODUCTION ENERGY LOSS": setting.getBobSelfReproductionEnergyLoss(), "BOB SEXUAL REPRODUCTION LOSS": setting.getBobSexualReproductionLoss(), "BOB SEXUAL REPRODUCTION LEVEL": setting.getBobSexualReproductionLevel(),
                "PERCEPTION FLAT PENALTY": setting.getPerceptionFlatPenalty(), "MEMORY FLAT PENALTY": setting.getMemoryFlatPenalty(),
                "DEFAULT VELOCITY": setting.getDefaultVelocity(), "DEFAULT MASS": setting.getDefaultMass(), "DEFAULT VISION": setting.getDefaultVision(), "DEFAULT MEMORY POINT": setting.getDefaultMemoryPoint(),
                "MASS VARIATION": setting.getMassVariation(), "VELOCITY VARIATION": setting.getVelocityVariation(), "VISION VARIATION": setting.getVelocityVariation() , "MEMORY VARIATION": setting.getMemoryVariation(),
                "SELF REPRODUCTION": setting.getSelfReproduction(),"SEXUAL REPRODUCTION": setting.getSexualReproduction()
               }
# settingParam = ["GRID LENGTH", "NUMBER BOB", "NUMBER SPAWNED FOOD", "FOOD ENERGY", 
#                 "BOB SPAWN ENERGY", "BOB MAX ENERGY", "BOB_BIRTH1_ENERGY", "BOB_BIRTH2_ENERGY", "BOB STATIONARY ENERGY LOSS", "BOB SELF REPRODUCTION ENERGY LOSS", "BOB SEXUAL REPRODUCTION LOSS", "BOB SEXUAL REPRODUCTION LEVEL", 
#                 "PERCEPTION FLAT PENALTY", "MEMORY FLAT PENALTY", 
#                 "DEFAULT VELOCITY", "DEFAULT MASS", "DEFAULT VISION", "DEFAULT MEMORY POINT", 
#                 "VAR_MASS", "VAR_VELO", "VAR_VISION", "VAR_MEMORY_POINT", 
#                 "SELF REPRODUCTION", "SEXUAL REPRODUCTION"]
# grid_dict = [100, 200, 100, 100,200, 50, 100 ,0.5, 150, 100, 150, 1/5, 1/5, 1, 1, 4, 0, 0.1, 0.1, 1, 1, True, True]
# Calcul de la position x pour centraliser les grilles horizontalement
ingameparam = [ "FPS", "NUMBER SPAWNED FOOD" ,  "FOOD ENERGY", "BOB MAX ENERGY", "BOB NEWBORN ENERGY", "SEXUAL BORN ENERGY", "BOB STATIONARY ENERGY LOSS", "BOB SELF REPRODUCTION ENERGY LOSS", 
               "BOB SEXUAL REPRODUCTION LOSS", "BOB SEXUAL REPRODUCTION LEVEL", "PERCEPTION FLAT PENALTY", "MEMORY FLAT PENALTY"
               , "MASS VARIATION", "VELOCITY VARIATION", "VISION VARIATION" , "MEMORY VARIATION", "SELF REPRODUCTION", "SEXUAL REPRODUCTION" ]

grid_x = (screen.get_width() - len(max(grid_dict.keys(), key=len)) * 10) // 2

# Calcul de la position y pour centraliser les grilles verticalement
grid_y = (screen.get_height() - len(grid_dict.keys()) * 50) // 2

# État des paramètres
settings_open = False
load_open = False

# Fonction pour dessiner du texte sur l'écran
def drawText(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Fonction pour dessiner les boutons avec transparence 
def draw_transparent_button(text, rect, transparency):
    button_surface = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
    button_surface.fill((WHITE[0], WHITE[1], WHITE[2], transparency))
    screen.blit(button_surface, (rect.x, rect.y))
    drawText(text, BLACK, rect.x + rect.width // 2, rect.y + rect.height // 2)

# Fonction pour dessiner les grilles avec transparence (la transparence des grilles des settings à revoir)
def draw_transparent_grids(labels, values, x, y, transparency):
    # global grid_value_rects
    # grid_value_rects = dict()  # Réinitialise la liste des rectangles
    cliquer = dict()
    for i, (label, value) in enumerate(zip(labels, values)):
        drawText(label, WHITE, x, y + 20 + i * 50) # Vẽ label thông số
        value_rect = pg.Rect(x + 320, y + i * 50, 200, 40) # Tạo hình chữ nhật thông số
        pg.draw.rect(screen, (WHITE[0], WHITE[1], WHITE[2], transparency), value_rect) # Vẽ hình chữ nhật thông số
        drawText(str(value), BLACK, x + 420, y + 20 + i * 50) # Vẽ giá trị thông số
        # grid_value_rects[label] = value_rect #  Pour cliquer 
        cliquer[label] = value_rect
    return cliquer



# def draw_transparent_grids ( labels , values , x , y , transparency ):

# def save_settings():
#     global grid_dict, settingParam
#     # Sauvegarde les paramètres dans un fichier texte
#     f = open("GameControl/settings.py", "w")
#     for key, value in grid_dict.items(): 
#         f.write(key + " = " + str(value) + "\n")
#     f.write("TILE_SIZE = 32\n")
#     f.write("RESOLUTIONX = 1920\n")
#     f.write("RESOLUTIONY = 1080\n")
#     f.write("SURFACE_WIDTH = TILE_SIZE * GRID LENGTH * 2\n")
#     f.write("SURFACE_HEIGHT = TILE_SIZE * GRID LENGTH + TILE_SIZE * 2\n")
#     f.write("TICKS_PER_DAY = 50\n")
#     f.write("IMAGE_PATH = 'assets/graphics/'\n")
#     f.close()


    # print("Paramètres enregistrés avec succès.")

# Initialiser la luminosité à 1.0 (valeur normale)
luminosite = 1.0

def augmenter_luminosite():
    global luminosite
    luminosite += 0.1
    pg.display.set_gamma(luminosite)


def diminuer_luminosite():
    global luminosite
    luminosite -= 0.1
    pg.display.set_gamma(luminosite)

def play_music():
    pg.mixer.music.play(-1)

def stop_music():
    pg.mixer.music.stop()




# Dans la fonction open_settings
def open_settings():
    global selected_value_index, grid_value_rects, grid_dict, input_text, settings_open, ingameparam
    input_active = False
    input_text = ""
    back_button_rect = pg.Rect(20, 20, button_width, button_height)
    stop_music_button_rect = pg.Rect(back_button_rect.right + 10, 20, button_width, button_height)
    play_music_button_rect = pg.Rect(stop_music_button_rect.right + 10, 20, button_width, button_height)
    increase_brightness_button_rect = pg.Rect(play_music_button_rect.right + 10, 20, button_width, button_height)
    decrease_brightness_button_rect = pg.Rect(increase_brightness_button_rect.right + 10, 20, button_width, button_height)

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    # save_settings()
                    settings_open = False
                    return  # Retourner au menu principal
                
                if stop_music_button_rect.collidepoint(event.pos):
                    stop_music()
                
                if play_music_button_rect.collidepoint(event.pos):
                    play_music()

                if increase_brightness_button_rect.collidepoint(event.pos):
                    augmenter_luminosite()

                if decrease_brightness_button_rect.collidepoint(event.pos):
                    diminuer_luminosite()
                
                # Vérifie si la souris a cliqué sur une valeur spécifique

                for key,value in grid_value_rects.items() :
                    if value.collidepoint(event.pos):
                        selected_value_index = key
                        input_active = True
                        print("input_active")
                        # input_text = str(grid_dict[selected_value_index])  # Utiliser la valeur actuelle pour l'affichage initial
                        input_text = ""  # Utiliser la valeur actuelle pour l'affichage initial

            elif event.type == pg.KEYDOWN:
                if input_active:
                    match selected_value_index:
                        case None:
                            pass
                        case "FPS":
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 4:
                                                match new_value:
                                                    case 1:
                                                        setting.setFps(32)
                                                        grid_dict[selected_value_index] = 32
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    case 2:
                                                        setting.setFps(24)
                                                        grid_dict[selected_value_index] = 24
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    case 3:
                                                        setting.setFps(16)
                                                        grid_dict[selected_value_index] = 16
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    case 4:
                                                        setting.setFps(8)
                                                        grid_dict[selected_value_index] = 8
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 1:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 3 caractère.")
                        case "GRID LENGTH": # GridLength
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 200:
                                                setting.setGridLength(new_value)
                                                print("Setting grid length to ", new_value)
                                                print("Surface width: ", setting.getSurfaceWidth())
                                                print("Surface height: ", setting.getSurfaceHeight())
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 3:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 3 caractère.")
                        case "NUMBER BOB": # nbBobs                            
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 200:
                                                setting.setNbBob(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 3:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 3 caractère.")
                        case "NUMBER SPAWNED FOOD": # Nb Spawned Food
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1000:
                                                setting.setNbSpawnFood(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        case "FOOD ENERGY": # Food Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 2000:
                                                setting.setFoodEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        case "BOB SPAWN ENERGY": # Bob Spawned Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobSpawnEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        case "BOB MAX ENERGY": # Bob Max Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobMaxEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")

                        case "BOB NEWBORN ENERGY": # New Born Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobNewbornEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        
                        case "SEXUAL BORN ENERGY": # SEXUAL BORN ENERGY
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setSexualBornEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")                            
                        case "BOB STATIONARY ENERGY LOSS": # Stationary energy loss
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setBobStationaryEnergyLoss(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")

                        case "BOB SELF REPRODUCTION ENERGY LOSS": # Self Reproduction energy loss
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1000:
                                                setting.setBobSelfReproductionEnergyLoss(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   

                        case "BOB SEXUAL REPRODUCTION LOSS": # Sexual reproduction energy loss
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1000:
                                                setting.setBobSexualReproductionLoss(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   

                        case "BOB SEXUAL REPRODUCTION LEVEL": # Sexual reproduction level
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobSexualReproductionLevel(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")                                                          

                        case "PERCEPTION FLAT PENALTY": # Perception Flat Penalty
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1:
                                                setting.setPerceptionFlatPenalty(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   
                        case "MEMORY FLAT PENALTY": # Memory Flat Penalty
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1:
                                                setting.setMemoryFlatPenalty(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   
                        case "DEFAULT VELOCITY": # Default velocity
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 10:
                                                setting.setDefaultVelocity(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")   
                        case "DEFAULT MASS": # Default mass
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 10:
                                                setting.setDefaultMass(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")   
                        case "DEFAULT VISION": # Default Vision
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setDefaultVision(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")   
                        case "DEFAULT MEMORY POINT": # Default Memory point
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setDefaultMemoryPoint(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")   
                        case "MASS VARIATION": # Mass Variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setMassVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")           
                        case "VELOCITY VARIATION": # Velocity variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setVelocityVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   
                        case "VISION VARIATION": #Vision Variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setVisionVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 2:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 2 caractère.")
                        case "MEMORY VARIATION": # Memory point variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setMemoryVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 2:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 2 caractère.")
                        case "SELF REPRODUCTION": # Self Reproduction
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        grid_dict[selected_value_index] = ""
                                        if input_text == "":
                                            pass
                                        else:
                                            if input_text == "0":
                                                setting.setSelfReproduction(False)
                                                grid_dict[selected_value_index] = False
                                            else: 
                                                setting.setSelfReproduction(True)
                                                grid_dict[selected_value_index] = True
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 1:
                                    if event.unicode == "0":
                                        input_text += event.unicode
                                    elif event.unicode == "1":
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être 0 ou 1.")
                                else:
                                    print("La valeur ne doit pas dépasser 1 caractère.")    
                        case "SEXUAL REPRODUCTION": # Sexual reproduction
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        grid_dict[selected_value_index] = ""
                                        if input_text == "":
                                            pass
                                        else:
                                            if input_text == "0":
                                                setting.setSexualReproduction(False)
                                                grid_dict[selected_value_index] = False
                                            else: 
                                                setting.setSexualReproduction(True)
                                                grid_dict[selected_value_index] = True
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 1:
                                    if event.unicode == "0":
                                        input_text += event.unicode
                                    elif event.unicode == "1":
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être 0 ou 1.")
                                else:
                                    print("La valeur ne doit pas dépasser 1 caractère.") 
                
 

                            
        screen.blit(background_image, (0, 0))
        labels = list(grid_dict.keys())
        values = list(grid_dict.values())
        # Dessiner les grilles avec transparence
        grid_value_rects.update(draw_transparent_grids(labels[:len(labels)//2], values[:len(values)//2], 400, 300, 50))
        grid_value_rects.update(draw_transparent_grids(labels[len(labels)//2:], values[len(values)//2:], 1300, 300, 50))
   


        # draw_transparent_grids(grid_labels[len(grid_labels)//2:], grid_dict[len(grid_dict)//2:], 1100, 100, 50)
        # Dessiner le bouton de retour avec transparence
        draw_transparent_button("BACK", back_button_rect, 128)
        draw_transparent_button("Stop Music", stop_music_button_rect, 128)
        draw_transparent_button("Play Music", play_music_button_rect, 128)
        draw_transparent_button("Increase Brightness", increase_brightness_button_rect, 128)
        draw_transparent_button("Decrease Brightness", decrease_brightness_button_rect, 128)


        # Si une valeur est sélectionnée, dessine un contour autour de cette valeur
        if selected_value_index is not None:
            pg.draw.rect(screen, WHITE, grid_value_rects[selected_value_index], 2)

        # Si l'entrée est active, affiche le texte saisi
        if input_active:
            # Effacer l'ancien texte avec un rectangle blanc
            pg.draw.rect(screen, WHITE, (grid_value_rects[selected_value_index].x, grid_value_rects[selected_value_index].y, 200, 40))
            input_surface = font.render(input_text, True, BLACK)  # Couleur de la police en noir
            input_rect = input_surface.get_rect(center=(grid_value_rects[selected_value_index].centerx, grid_value_rects[selected_value_index].centery))
            # pg.draw.rect(screen, WHITE, (input_rect.x - 5, input_rect.y - 5, input_rect.width + 10, input_rect.height + 10), border_radius=5)  # Couleur de fond du rectangle en blanc
            screen.blit(input_surface, input_rect)

        pg.display.flip()

def openIngamesetting():
    global selected_value_index, grid_value_rects, grid_dict, input_text, settings_open, ingameparam
    input_active = False
    input_text = ""
    back_button_rect = pg.Rect(20, 20, button_width, button_height)
    stop_music_button_rect = pg.Rect(back_button_rect.right + 10, 20, button_width, button_height)
    play_music_button_rect = pg.Rect(stop_music_button_rect.right + 10, 20, button_width, button_height)
    increase_brightness_button_rect = pg.Rect(play_music_button_rect.right + 10, 20, button_width, button_height)
    decrease_brightness_button_rect = pg.Rect(increase_brightness_button_rect.right + 10, 20, button_width, button_height)
    

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    # save_settings()
                    settings_open = False
                    return  # Retourner au menu principal
                if stop_music_button_rect.collidepoint(event.pos):
                    stop_music()
                
                if play_music_button_rect.collidepoint(event.pos):
                    play_music()
                
                if increase_brightness_button_rect.collidepoint(event.pos):
                    augmenter_luminosite()

                if decrease_brightness_button_rect.collidepoint(event.pos):
                    diminuer_luminosite()
                
    
                # Vérifie si la souris a cliqué sur une valeur spécifique
                for key,value in grid_value_rects.items():
                    if value.collidepoint(event.pos):
                        selected_value_index = key
                        input_active = True
                        print("input_active")
                        # input_text = str(grid_dict[selected_value_index])  # Utiliser la valeur actuelle pour l'affichage initial
                        input_text = ""  # Utiliser la valeur actuelle pour l'affichage initial

            elif event.type == pg.KEYDOWN:
                if input_active:
                    match selected_value_index:
            #             grid_labels = ["GRID LENGTH", "NUMBER BOB", "BOB SPAWN ENERGY", "BOB MAX ENERGY" , "NUMBER SPAWNED FOOD"  "FOOD ENERGY", 
            #    "PERCEPTION FLAT PENALTY", "MEMORY FLAT PENALTY",  "DEFAULT VELOCITY", "DEFAULT MASS", "DEFAULT VISION", 
            #    "DEFAULT MEMORY POINT", "MASS VARIATION", "VELOCITY VARIATION", "VISION VARIATION" , "MEMORY VARIATION", "SELF REPRODUCTION  ",
            #     "SEXUAL REPRODUCTION" ]
                        case None:
                            pass
            #             grid_dict = {"GRID LENGTH": 100,
            #    "NUMBER BOB": 200, "NUMBER SPAWNED FOOD": 100,  "FOOD ENERGY": 100,
            #    "BOB SPAWN ENERGY": 200, "BOB MAX ENERGY": 50 ,"BOB NEWBORN ENERGY": 100, "SEXUAL BORN ENERGY": 0.5, "BOB STATIONARY ENERGY LOSS": 150, "BOB SELF REPRODUCTION ENERGY LOSS": 100, "BOB SEXUAL REPRODUCTION LOSS": 150, "BOB SEXUAL REPRODUCTION LEVEL": 1/5,
            #     "PERCEPTION FLAT PENALTY": 1/5, "MEMORY FLAT PENALTY": 1,
            #     "DEFAULT VELOCITY": 1, "DEFAULT MASS": 1, "DEFAULT VISION": 4, "DEFAULT MEMORY POINT": 0,
            #     "MASS VARIATION": 0.1, "VELOCITY VARIATION": 0.1, "VISION VARIATION": 1 , "MEMORY VARIATION": 1,
            #     "SELF REPRODUCTION  ": True,"SEXUAL REPRODUCTION": True
            #    }
                        case "FPS":
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 4:
                                                match new_value:
                                                    case 1:
                                                        setting.setFps(32)
                                                        grid_dict[selected_value_index] = 32
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    case 2:
                                                        setting.setFps(24)
                                                        grid_dict[selected_value_index] = 24
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    case 3:
                                                        setting.setFps(16)
                                                        grid_dict[selected_value_index] = 16
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    case 4:
                                                        setting.setFps(8)
                                                        grid_dict[selected_value_index] = 8
                                                        input_active = False
                                                        input_text = ""
                                                        selected_value_index = None
                                                    
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 1:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 3 caractère.")
                        case "GRID LENGTH": # GridLength
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 200:
                                                setting.setGridLength(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 3:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 3 caractère.")
                        case "NUMBER BOB": # nbBobs                            
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 200:
                                                setting.setNbBob(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 3:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 3 caractère.")
                        case "NUMBER SPAWNED FOOD": # Nb Spawned Food
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1000:
                                                setting.setNbSpawnFood(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        case "FOOD ENERGY": # Food Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 2000:
                                                setting.setFoodEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        case "BOB SPAWN ENERGY": # Bob Spawned Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobSpawnEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        case "BOB MAX ENERGY": # Bob Max Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobMaxEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")

                        case "BOB NEWBORN ENERGY": # New Born Energy
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobNewbornEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")
                        
                        case "SEXUAL BORN ENERGY": # SEXUAL BORN ENERGY
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setSexualBornEnergy(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")                            
                        case "BOB STATIONARY ENERGY LOSS": # Stationary energy loss
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setBobStationaryEnergyLoss(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")

                        case "BOB SELF REPRODUCTION ENERGY LOSS": # Self Reproduction energy loss
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1000:
                                                setting.setBobSelfReproductionEnergyLoss(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   

                        case "BOB SEXUAL REPRODUCTION LOSS": # Sexual reproduction energy loss
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1000:
                                                setting.setBobSexualReproductionLoss(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   

                        case "BOB SEXUAL REPRODUCTION LEVEL": # Sexual reproduction level
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 1000:
                                                setting.setBobSexualReproductionLevel(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")                                                          

                        case "PERCEPTION FLAT PENALTY": # Perception Flat Penalty
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1:
                                                setting.setPerceptionFlatPenalty(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   
                        case "MEMORY FLAT PENALTY": # Memory Flat Penalty
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 1:
                                                setting.setMemoryFlatPenalty(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   
                        case "DEFAULT VELOCITY": # Default velocity
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 10:
                                                setting.setDefaultVelocity(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")   
                        case "DEFAULT MASS": # Default mass
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 < new_value <= 10:
                                                setting.setDefaultMass(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")   
                        case "DEFAULT VISION": # Default Vision
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setDefaultVision(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")   
                        case "DEFAULT MEMORY POINT": # Default Memory point
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setDefaultMemoryPoint(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 5:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 5 caractère.")  
                        case "MASS VARIATION": # Mass Variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setMassVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")           
                        case "VELOCITY VARIATION": # Velocity variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = float(input_text)
                                        if not isinstance(new_value, float):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setVelocityVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 4:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    elif event.unicode == ".":
                                        if "." in input_text:
                                            print("La valeur doit être just 1 point.")
                                        else:
                                            input_text += event.unicode
                                    else:
                                        print("La valeur doit être un float.")
                                else:
                                    print("La valeur ne doit pas dépasser 4 caractère.")   
                        case "VISION VARIATION": #Vision Variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setVisionVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 2:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 2 caractère.")
                        case "MEMORY VARIATION": # Memory point variation
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        new_value = int(input_text)
                                        if not isinstance(new_value, int):
                                            # print("La valeur doit être un entier.")
                                            input_text = ""
                                            input_active = False
                                        else:
                                            if 0 <= new_value <= 10:
                                                setting.setMemoryVariation(new_value)
                                                grid_dict[selected_value_index] = new_value
                                                input_active = False
                                                input_text = ""
                                                selected_value_index = None
                                            else: 
                                                input_text = ""
                                                input_active = False
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 2:
                                    if event.unicode.isdigit():
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être un entier.")
                                else:
                                    print("La valeur ne doit pas dépasser 2 caractère.")
                        case "SELF REPRODUCTION": # Self Reproduction
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        grid_dict[selected_value_index] = ""
                                        if input_text == "":
                                            pass
                                        else:
                                            if input_text == "0":
                                                setting.setSelfReproduction(False)
                                                grid_dict[selected_value_index] = False
                                            else: 
                                                setting.setSelfReproduction(True)
                                                grid_dict[selected_value_index] = True
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 1:
                                    if event.unicode == "0":
                                        input_text += event.unicode
                                    elif event.unicode == "1":
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être 0 ou 1.")
                                else:
                                    print("La valeur ne doit pas dépasser 1 caractère.")    
                        case "SEXUAL REPRODUCTION": # Sexual reproduction
                            if event.key == pg.K_RETURN:
                                    if input_text == "":
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                                    else:                                
                                        grid_dict[selected_value_index] = ""
                                        if input_text == "":
                                            pass
                                        else:
                                            if input_text == "0":
                                                setting.setSexualReproduction(False)
                                                grid_dict[selected_value_index] = False
                                            else: 
                                                setting.setSexualReproduction(True)
                                                grid_dict[selected_value_index] = True
                                            input_active = False
                                            input_text = ""
                                            selected_value_index = None
                            elif event.key == pg.K_BACKSPACE:
                                input_text = input_text[:-1]
                            else:
                                if len(input_text) < 1:
                                    if event.unicode == "0":
                                        input_text += event.unicode
                                    elif event.unicode == "1":
                                        input_text += event.unicode
                                    else:
                                        print("La valeur doit être 0 ou 1.")
                                else:
                                    print("La valeur ne doit pas dépasser 1 caractère.")   
                            


                    

        screen.blit(background_image, (0, 0))
        new = [(key,value) for key, value in grid_dict.items() if key in ingameparam]
        new1 = dict(new)
        labels = list(new1.keys())
        values = list(new1.values())
        # Dessiner les grilles avec transparence
        grid_value_rects.update(draw_transparent_grids(labels[:len(labels)//2], values[:len(values)//2], 400, 300, 50))
        grid_value_rects.update(draw_transparent_grids(labels[len(labels)//2:], values[len(values)//2:], 1300, 300, 50))
   


        # Dessiner le bouton de retour avec transparence  
        draw_transparent_button("BACK", back_button_rect, 128)
        draw_transparent_button("Stop Music", stop_music_button_rect, 128)
        draw_transparent_button("Play Music", play_music_button_rect, 128)
        draw_transparent_button("Increase Brightness", increase_brightness_button_rect, 128)
        draw_transparent_button("Decrease Brightness", decrease_brightness_button_rect, 128)


        # Si une valeur est sélectionnée, dessine un contour autour de cette valeur
        if selected_value_index is not None:
            pg.draw.rect(screen, WHITE, grid_value_rects[selected_value_index], 2)

        # Si l'entrée est active, affiche le texte saisi
        if input_active:
            # Effacer l'ancien texte avec un rectangle blanc
            pg.draw.rect(screen, WHITE, (grid_value_rects[selected_value_index].x, grid_value_rects[selected_value_index].y, 200, 40))
            input_surface = font.render(input_text, True, BLACK)  # Couleur de la police en noir
            input_rect = input_surface.get_rect(center=(grid_value_rects[selected_value_index].centerx, grid_value_rects[selected_value_index].centery))
            # pg.draw.rect(screen, WHITE, (input_rect.x - 5, input_rect.y - 5, input_rect.width + 10, input_rect.height + 10), border_radius=5)  # Couleur de fond du rectangle en blanc
            screen.blit(input_surface, input_rect)

        pg.display.flip()
            
def open_load(screen, clock):
    global return_to_menu, load_open

    # Déclaration des rectangles des boutons de chargement
    button_width, button_height = 300, 50
    load1_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 200, button_width, button_height)
    load2_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 300, button_width, button_height)
    load3_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 400, button_width, button_height)
    load4_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 500, button_width, button_height)
    load5_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 600, button_width, button_height)
    back_button_rect = pg.Rect(20, 20, button_width, button_height)
    # Ajoutez d'autres boutons de chargement ici pour chaque sauvegarde

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if load1_button_rect.collidepoint(event.pos):
                    # load_game('save1.pkl')  # Remplacez par le nom de fichier approprié
                    load_open = False
                    return_to_menu = False  # Réinitialiser la variable
                    return 1  # Retourner au menu principal
                elif load2_button_rect.collidepoint(event.pos):
                    load_open = False
                    return_to_menu = False  # Réinitialiser la variable
                    return 2  # Retourner au menu principal
                elif load3_button_rect.collidepoint(event.pos):
                    load_open = False
                    return_to_menu = False  # Réinitialiser la variable
                    return 3  # Retourner au menu principal
                elif load4_button_rect.collidepoint(event.pos):
                    load_open = False
                    return_to_menu = False  # Réinitialiser la variable
                    return 4  # Retourner au menu principal
                elif load5_button_rect.collidepoint(event.pos):
                    load_open = False
                    return_to_menu = False  # Réinitialiser la variable
                    return 5  # Retourner au menu principal
                elif back_button_rect.collidepoint(event.pos):
                    load_open = False
                    return_to_menu = True
                    return None

                # Ajoutez des conditions pour d'autres boutons de chargement ici

        screen.blit(background_image, (0, 0))

        # Center the load buttons horizontally and vertically
        draw_transparent_button("Load Save 1", load1_button_rect, 128)
        draw_transparent_button("Load Save 2", load2_button_rect, 128)
        draw_transparent_button("Load Save 3", load3_button_rect, 128)
        draw_transparent_button("Load Save 4", load4_button_rect, 128)
        draw_transparent_button("Load Save 5", load5_button_rect, 128)
        draw_transparent_button("BACK", back_button_rect, 128)
        # Ajoutez d'autres boutons de chargement ici

        pg.display.flip()

# Dans la fonction show_menu
def show_menu(screen, clock):
    global selected_value_index, grid_value_rects, grid_dict, settings_open, return_to_menu, load_open

    # Déclaration des rectangles des boutons de base
    button_width, button_height = 300, 50
    play_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 200, button_width, button_height)
    load_game_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 300, button_width, button_height)
    settings_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 400, button_width, button_height)
    quit_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 500, button_width, button_height)
    # back_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 600, button_width, button_height)
    # stop_music_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 700, button_width, button_height)
    # play_music_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 800, button_width, button_height)
    # increase_brightness_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 900, button_width, button_height)
    # decrease_brightness_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 1000, button_width, button_height)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if settings_open:
                    if back_button_rect.collidepoint(event.pos):
                        settings_open = False
                        return_to_menu = True
                    if stop_music_button_rect.collidepoint(event.pos):
                        stop_music()
                    if play_music_button_rect.collidepoint(event.pos):
                        play_music()
                    if increase_brightness_button_rect.collidepoint(event.pos):
                        augmenter_luminosite()
                    if decrease_brightness_button_rect.collidepoint(event.pos):
                        diminuer_luminosite()
                if load_open:
                    if back_button_rect.collidepoint(event.pos):
                        load_open = False
                        return_to_menu = True
                else:
                    if play_button_rect.collidepoint(event.pos):
                        return_to_menu = False  # Réinitialiser la variable
                        print("Return to menu: ", return_to_menu)
                        return 0  # Retourner au menu principal
                    elif settings_button_rect.collidepoint(event.pos):
                        return_to_menu = False
                        settings_open = True
                        open_settings() 
                    elif quit_button_rect.collidepoint(event.pos):
                        pg.quit()
                        sys.exit()
                    elif load_game_button_rect.collidepoint(event.pos):
                        return_to_menu = False
                        load_open = True
                        i = open_load(screen, clock)
                        if i == None:
                            pass
                        else:
                            return i

        screen.blit(background_image, (0, 0))

        if settings_open:
            open_settings()
            # Center the buttons horizontally and vertically
        elif load_open:
            open_load(screen, clock)
        else:
            draw_transparent_button("NEWGAME", play_button_rect, 128)
            draw_transparent_button("LOAD GAME", load_game_button_rect, 128)
            draw_transparent_button("SETTINGS", settings_button_rect, 128)
            draw_transparent_button("QUIT", quit_button_rect, 128)

        pg.display.flip()


def pause( screen, camera ):
    # Declaration des rectangles des map:
    pauseSurface = pg.Surface((setting.getSurfaceWidth(), setting.getSurfaceHeight())).convert_alpha()
    print(setting.getSurfaceWidth(), setting.getSurfaceHeight())
    while True:
        ########################## Draw map #######################################################
        screen.fill((137, 207, 240))
        pauseSurface.fill((195, 177, 225))
        # surface.blit(loadMap(), (0,0))
        textureImg = loadGrassImage()
        flowImg = loadFlowerImage()
        for row in gameController.getMap(): # x is a list of a double list Map
            for tile in row: # tile is an object in list
                (x, y) = tile.getRenderCoord()
                offset = (x + setting.getSurfaceWidth()/2 , y + setting.getTileSize())
                a,b = offset
                if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                    if tile.flower:
                        pauseSurface.blit(flowImg, offset)
                    else:
                        pauseSurface.blit(textureImg, offset)
                else: pass
        

        ########################## Draw Bob #######################################################
        greenLeft = loadGreenLeft()
        blueLeft = loadBlueLeft()
        purpleLeft = loadPurpleLeft()
        for bob in gameController.listBobs:
            (destX, destY) = bob.getCurrentTile().getRenderCoord()
            (desX, desY) = (destX + setting.getSurfaceWidth()//2 , destY - ( + 50 - setting.getTileSize() ) )
            finish = (desX, desY + setting.getTileSize())
            a,b = finish
            # bar_width = int((bob.energy / bob.energyMax) * 50)
            # pg.draw.rect(surface, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
            if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                if bob.isHunting:
                    pauseSurface.blit(purpleLeft, finish)
                else: pauseSurface.blit(greenLeft, finish)
        ########################## Draw Food #######################################################
        foodTexture = loadFoodImage()
        for food in gameController.getFoodTiles():
            (x, y) = food.getRenderCoord()
            (X, Y) = (x + setting.getSurfaceWidth()//2  , y - (foodTexture.get_height() - setting.getTileSize() ) )
            position = (X , Y + setting.getTileSize() )
            a,b = position
            # bar_width = int((food.foodEnergy / setting.getFoodEnergy()) * 50)
            # pg.draw.rect(surface, (0, 0, 255), (position[0] + 5, position[1]+ 20, bar_width, 5))
            pauseSurface.blit(foodTexture, position)
        listRect = []
        camera.update()
        for row in gameController.getMap():
            for tile in row:
                (x,y) = tile.getRenderCoord()
                offset = ( x + setting.getSurfaceWidth()//2 , y + setting.getTileSize()  ) 
                a, b = offset
                if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                    listRect.append((tile,(a + camera.scroll.x, b + camera.scroll.y)))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return
        mouse_x, mouse_y = pg.mouse.get_pos()
        for coord in listRect:
            if coord[1][0] <= mouse_x <= coord[1][0] + 64 and coord[1][1] + 8 <= mouse_y <= coord[1][1] + 24:
                print(coord[0].gridX, coord[0].gridY)
                if len(coord[0].getBobs()) != 0:
                    nb = len(coord[0].getBobs())
                # for bob in coord[0].getBobs():
                    if ( mouse_y - 150 >= 0 ):
                        if ( mouse_x - 50*nb < 0 ):
                            pg.draw.rect(pauseSurface, (225, 255, 123), pg.Rect( mouse_x - camera.scroll.x +50 , mouse_y - camera.scroll.y -50 , 100 * nb, 100))
                            i = 0
                            for bob in coord[0].getBobs():
                                draw_text(pauseSurface, f"ID: {bob.id}", 15,(0,0,0),(mouse_x - camera.scroll.x +50 + 100*i + 5 , mouse_y - camera.scroll.y -50 + 5))
                                draw_text(pauseSurface, f"Energy: {bob.energy:.3f}", 15,(0,0,0),(mouse_x - camera.scroll.x +50+ 100*i + 5 , mouse_y - camera.scroll.y -50 + 15))
                                draw_text(pauseSurface, f"Mass: {bob.mass:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x +50+ 100*i + 5 , mouse_y - camera.scroll.y -50 + 25)))
                                draw_text(pauseSurface, f"Vision: {bob.vision:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x +50+ 100*i + 5 , mouse_y - camera.scroll.y -50 + 35)))
                                draw_text(pauseSurface, f"Velocity: {bob.velocity:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x +50+ 100*i + 5 , mouse_y - camera.scroll.y -50 + 45)))
                                draw_text(pauseSurface, f"Memory: {bob.memoryPoint:.3f}",15,(0,0,0) , ((mouse_x - camera.scroll.x +50+ 100*i + 5 , mouse_y - camera.scroll.y -50 + 55)))
                                # draw_text(pauseSurface, f"-------------------------------------------------------------",15,(0,0,0) , ((mouse_x - camera.scroll.x +50 + 5 , mouse_y - camera.scroll.y -50 + 65)))
                                i += 1


                        elif( mouse_x + 50*nb > 1920  ):
                            pg.draw.rect(pauseSurface, (225, 255, 123), pg.Rect( mouse_x - camera.scroll.x - 50 - 100*nb , mouse_y - camera.scroll.y - 50 , 100 * nb, 100))
                            i = 0
                            for bob in coord[0].getBobs():
                                draw_text(pauseSurface, f"ID: {bob.id}", 15,(0,0,0),(mouse_x - camera.scroll.x - 50 -100*nb + 100*i + 5 , mouse_y - camera.scroll.y -50 + 5))
                                draw_text(pauseSurface, f"Energy: {bob.energy:.3f}", 15,(0,0,0),(mouse_x - camera.scroll.x -50 -100*nb + 100*i + 5 , mouse_y - camera.scroll.y -50 + 15))
                                draw_text(pauseSurface, f"Mass: {bob.mass:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 -100*nb + 100*i + 5 , mouse_y - camera.scroll.y -50 + 25)))
                                draw_text(pauseSurface, f"Vision: {bob.vision:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 -100*nb + 100*i + 5 , mouse_y - camera.scroll.y -50 + 35)))
                                draw_text(pauseSurface, f"Velocity: {bob.velocity:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 -100*nb + 100*i + 5 , mouse_y - camera.scroll.y -50 + 45)))
                                draw_text(pauseSurface, f"Memory: {bob.memoryPoint:.3f}",15,(0,0,0) , ((mouse_x - camera.scroll.x -50 -100*nb + 100*i + 5 , mouse_y - camera.scroll.y -50 + 55)))
                                # draw_text(pauseSurface, f"-------------------------------------------------------------",15,(0,0,0) , ((mouse_x - camera.scroll.x -250 + 5 , mouse_y - camera.scroll.y -50 + 65)))
                                i += 1


                        else:
                            pg.draw.rect(pauseSurface, (225, 255, 123), pg.Rect( mouse_x - camera.scroll.x -50 * nb , mouse_y - camera.scroll.y - 150 , 100 * nb, 100))
                            i = 0
                            for bob in coord[0].getBobs():
                                draw_text(pauseSurface, f"ID: {bob.id}", 15,(0,0,0),(mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y -150 + 5))
                                draw_text(pauseSurface, f"Energy: {bob.energy:.3f}", 15,(0,0,0),(mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y -150 + 15))
                                draw_text(pauseSurface, f"Mass: {bob.mass:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y -150 + 25)))
                                draw_text(pauseSurface, f"Vision: {bob.vision:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y -150 + 35)))
                                draw_text(pauseSurface, f"Velocity: {bob.velocity:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y -150 + 45)))
                                draw_text(pauseSurface, f"Memory: {bob.memoryPoint:.3f}",15,(0,0,0) , ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y -150 + 55)))
                                # draw_text(pauseSurface, f"-------------------------------------------------------------",15,(0,0,0) , ((mouse_x - camera.scroll.x -100 + 5 , mouse_y - camera.scroll.y -150 + 65)))
                                i += 1

                    else:
                        pg.draw.rect(pauseSurface, (225, 255, 123), pg.Rect( mouse_x - camera.scroll.x -50 * nb , mouse_y - camera.scroll.y + 50 , 100 * nb, 100))
                        i = 0
                        for bob in coord[0].getBobs():
                            draw_text(pauseSurface, f"ID: {bob.id}", 15,(0,0,0),(mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y + 50 + 5))
                            draw_text(pauseSurface, f"Energy: {bob.energy:.3f}", 15,(0,0,0),(mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y + 50 + 15))
                            draw_text(pauseSurface, f"Mass: {bob.mass:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y + 50 + 25)))
                            draw_text(pauseSurface, f"Vision: {bob.vision:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y + 50 + 35)))
                            draw_text(pauseSurface, f"Velocity: {bob.velocity:.3f}",15,(0,0,0), ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y + 50 + 45)))
                            draw_text(pauseSurface, f"Memory: {bob.memoryPoint:.3f}",15,(0,0,0) , ((mouse_x - camera.scroll.x -50 * nb + 100*i + 5 , mouse_y - camera.scroll.y + 50 + 55)))
                            # draw_text(pauseSurface, f"-------------------------------------------------------------",15,(0,0,0) , ((mouse_x - camera.scroll.x -100 + 5 , mouse_y - camera.scroll.y + 50 + 65)))
                            i += 1

        screen.blit(pauseSurface, (camera.scroll.x, camera.scroll.y))    
        draw_text(screen, f"Paused", 40, (0,0,0), (screen.get_width()//2 - 50, 10))
        drawIndex ( screen)
        pg.display.flip()

def drawIndex( surface):

    draw_text(
        surface,
        'Tick: {}'.format(round(gameController.getTick())),
        25,
        (0,0,0),
        (10, 30)
    )  
    draw_text(
        surface,
        'Day: {}'.format(round(gameController.getDay())),
        25,
        (0,0,0),
        (10, 50)
    )  
    draw_text(
        surface,
        'Number of bobs: {}'.format(gameController.getNbBobs()) ,
        25,
        (0,0,0),
        (10, 70)
    )
    draw_text(
        surface,
        'Number of bob spawned: {}'.format(gameController.getNbBobsSpawned()) ,
        25,
        (0,0,0),
        (10, 90)
    )
