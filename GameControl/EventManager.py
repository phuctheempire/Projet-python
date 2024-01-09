import pygame as pg
import sys

pg.init()

# Gestion de la musique
pg.mixer.init()

selected_value_index = None

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ajoutez cette variable globale
return_to_menu = False

# Création de la fenêtre en plein écran
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption("Game Menu")

# Charger l'image de fond, plusieurs images disponibles dans le dossier (à en choisir une)
background_image = pg.image.load("back2.png")
background_image = pg.transform.scale(background_image, screen.get_size())

# Charger la musique de fond
pg.mixer.music.load("song.mp3")
pg.mixer.music.set_volume(0.5)  # Le volume de 0.0 à 1.0
pg.mixer.music.play(-1)  # -1 pour jouer en boucle

# Police pour les boutons
font = pg.font.Font(None, 40)

# Déclaration des rectangles des boutons de base
button_width, button_height = 300, 50
play_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 200, button_width, button_height)
settings_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 300, button_width, button_height)
quit_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 400, button_width, button_height)
back_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 500, button_width, button_height)

grid_value_rects = []

# Déclaration des labels des grilles (à modifier en fonction du contenu de notre jeu, voir résumé du pdf du prof)
grid_labels = ["Larg:", "Long:", "Energy:", "Velocity:", "Min Energy:", "Mass:", "ScoreMemory:"]
grid_values = [10, 20, 30, 40, 50, 60, 70]  # Exemple de valeurs initiales

# Calcul de la position x pour centraliser les grilles horizontalement
grid_x = (screen.get_width() - len(max(grid_labels, key=len)) * 10) // 2

# Calcul de la position y pour centraliser les grilles verticalement
grid_y = (screen.get_height() - len(grid_labels) * 50) // 2

# État des paramètres
settings_open = False

# Fonction pour dessiner du texte sur l'écran
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Fonction pour dessiner les boutons avec transparence 
def draw_transparent_button(text, rect, transparency):
    button_surface = pg.Surface((rect.width, rect.height), pg.SRCALPHA)
    button_surface.fill((WHITE[0], WHITE[1], WHITE[2], transparency))
    screen.blit(button_surface, (rect.x, rect.y))
    draw_text(text, BLACK, rect.x + rect.width // 2, rect.y + rect.height // 2)

# Fonction pour dessiner les grilles avec transparence (la transparence des grilles des Settings à revoir)
def draw_transparent_grids(labels, values, x, y, transparency):
    global grid_value_rects
    grid_value_rects = []  # Réinitialise la liste des rectangles
    for i, (label, value) in enumerate(zip(labels, values)):
        draw_text(label, WHITE, x, y + i * 50)
        value_rect = pg.Rect(x + 200, y + i * 50, 200, 40)
        pg.draw.rect(screen, (WHITE[0], WHITE[1], WHITE[2], transparency), value_rect)
        draw_text(str(value), BLACK, x + 300, y + 20 + i * 50)
        grid_value_rects.append(value_rect)

# Dans la fonction open_settings
def open_settings():
    global selected_value_index, grid_value_rects, grid_values, input_text, input_active
    input_active = False
    input_text = ""

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return  # Retourner au menu principal
                # Vérifie si la souris a cliqué sur une valeur spécifique
                for i, rect in enumerate(grid_value_rects):
                    if rect.collidepoint(event.pos):
                        selected_value_index = i
                        input_active = True
                        input_text = str(grid_values[selected_value_index])  # Utiliser la valeur actuelle pour l'affichage initial

            elif event.type == pg.KEYDOWN:
                if input_active:
                    if event.key == pg.K_RETURN:
                        try:
                            new_value = int(input_text)
                            grid_values[selected_value_index] = new_value
                            input_active = False
                            input_text = ""
                            selected_value_index = None
                        except ValueError:
                            print("La valeur doit être un entier.")
                            input_text = ""
                    elif event.key == pg.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.blit(background_image, (0, 0))

        # Dessiner les grilles avec transparence
        draw_transparent_grids(grid_labels, grid_values, grid_x, grid_y, 50)
        # Dessiner le bouton de retour avec transparence
        draw_transparent_button("BACK", back_button_rect, 128)

        # Si une valeur est sélectionnée, dessine un contour autour de cette valeur
        if selected_value_index is not None:
            pg.draw.rect(screen, WHITE, grid_value_rects[selected_value_index], 2)

        # Si l'entrée est active, affiche le texte saisi
        if input_active:
            # Effacer l'ancien texte avec un rectangle blanc
            pg.draw.rect(screen, WHITE, (grid_value_rects[selected_value_index].x, grid_value_rects[selected_value_index].y, 200, 40))
            input_surface = font.render(input_text, True, BLACK)  # Couleur de la police en noir
            input_rect = input_surface.get_rect(center=(grid_value_rects[selected_value_index].centerx, grid_value_rects[selected_value_index].centery))
            pg.draw.rect(screen, WHITE, (input_rect.x - 5, input_rect.y - 5, input_rect.width + 10, input_rect.height + 10), border_radius=5)  # Couleur de fond du rectangle en blanc
            screen.blit(input_surface, input_rect)

        pg.display.flip()
            


# Dans la fonction show_menu
def show_menu(screen, clock):
    global selected_value_index, grid_value_rects, grid_values, settings_open, return_to_menu

    # Déclaration des rectangles des boutons de base
    button_width, button_height = 300, 50
    play_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 200, button_width, button_height)
    settings_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 300, button_width, button_height)
    quit_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 400, button_width, button_height)
    back_button_rect = pg.Rect((screen.get_width() - button_width) // 2, 500, button_width, button_height)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if not settings_open:
                    if play_button_rect.collidepoint(event.pos):
                        return_to_menu = False  # Réinitialiser la variable
                        return  # Retourner au menu principal
                    elif settings_button_rect.collidepoint(event.pos):
                        settings_open = True
                        open_settings()  # Supprimez les arguments ici
                    elif quit_button_rect.collidepoint(event.pos):
                        pg.quit()
                        sys.exit()
                else:
                    if back_button_rect.collidepoint(event.pos):
                        settings_open = False
                        return_to_menu = False  # Réinitialiser la variable

        screen.blit(background_image, (0, 0))

        if not settings_open:
            # Center the buttons horizontally and vertically
            draw_transparent_button("PLAY", play_button_rect, 128)
            draw_transparent_button("SETTINGS", settings_button_rect, 128)
            draw_transparent_button("QUIT", quit_button_rect, 128)
        else:
            draw_transparent_grids(grid_labels, grid_values, 200, 100, 50)
            draw_transparent_button("BACK", back_button_rect, 128)

        pg.display.flip()