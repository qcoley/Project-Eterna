import time
import sys

from pygame import QUIT


def cutscenes_apothis_bridge(pygame, music, screen, scene_1, scene_2, scene_3, scene_4, scene_5, scene_6, cutscene_tic,
                             skip_button):

    in_cutscene = True
    first_viewed = False
    second_viewed = False
    third_viewed = False
    fourth_viewed = False
    fifth_viewed = False
    sixth_viewed = False

    pygame.mixer.music.fadeout(50)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=-1)

    while in_cutscene:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if skip_button.rect.collidepoint(pos):
                    in_cutscene = False

        cutscene_toc = time.perf_counter()
        cutscene_duration = cutscene_toc - cutscene_tic

        # --------------------------------------------------------------------------------------------------------------
        if not first_viewed:
            for alpha in range(0, 255):
                scene_1.set_alpha(alpha)
                screen.blit(scene_1, (0, 0))
                screen.blit(skip_button.surf, skip_button.rect)
                pygame.display.flip()
            first_viewed = True

        # --------------------------------------------------------------------------------------------------------------
        if cutscene_duration > 8:
            if not second_viewed:
                for alpha in range(0, 255):
                    scene_2.set_alpha(alpha)
                    screen.blit(scene_2, (0, 0))
                    screen.blit(skip_button.surf, skip_button.rect)
                    pygame.display.flip()
                second_viewed = True

        # --------------------------------------------------------------------------------------------------------------
        if cutscene_duration > 16:
            if not third_viewed:
                for alpha in range(0, 255):
                    scene_3.set_alpha(alpha)
                    screen.blit(scene_3, (0, 0))
                    screen.blit(skip_button.surf, skip_button.rect)
                    pygame.display.flip()
                third_viewed = True

        # --------------------------------------------------------------------------------------------------------------
        if cutscene_duration > 24:
            if not fourth_viewed:
                for alpha in range(0, 255):
                    scene_4.set_alpha(alpha)
                    screen.blit(scene_4, (0, 0))
                    screen.blit(skip_button.surf, skip_button.rect)
                    pygame.display.flip()
                fourth_viewed = True

        # --------------------------------------------------------------------------------------------------------------
        if cutscene_duration > 32:
            if not fifth_viewed:
                for alpha in range(0, 255):
                    scene_5.set_alpha(alpha)
                    screen.blit(scene_5, (0, 0))
                    screen.blit(skip_button.surf, skip_button.rect)
                    pygame.display.flip()
                fifth_viewed = True

        # --------------------------------------------------------------------------------------------------------------
        if cutscene_duration > 40:
            if not sixth_viewed:
                for alpha in range(0, 255):
                    scene_6.set_alpha(alpha)
                    screen.blit(scene_6, (0, 0))
                    screen.blit(skip_button.surf, skip_button.rect)
                    pygame.display.flip()
                sixth_viewed = True

        if cutscene_duration > 48:
            if sixth_viewed:
                in_cutscene = False
