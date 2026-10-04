import pygame
from local import *
from music import Playmusic

class OpeningScene:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        self.bg_image = pygame.image.load("assets/start_background.png")  # Tải ảnh nền
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Thay đổi kích thước ảnh nền

        # Trạng thái play hiện tại
        self.selected_play = None  # Chưa chọn play
        self.is_clicked = False  # Chưa click

        # Tải ảnh nút
        self.button_play = pygame.image.load("assets/play_icon.png")
        self.button_play_hover = pygame.image.load("assets/play_icon_hover.png")  # Nút play khi rê chuột qua
        self.button_play_clicked = pygame.image.load("assets/play_icon_clicked.png")  # Nút play khi đã click
        self.button_settings = pygame.image.load("assets/setting_icon.png")
        self.button_sound_on = pygame.image.load("assets/sound_icon.png")
        self.button_sound_off = pygame.image.load("assets/mute_icon.png")

        # Thay đổi kích thước các nút
        self.button_play = pygame.transform.scale(self.button_play, (500, 175))
        self.button_play_hover = pygame.transform.scale(self.button_play_hover, (500, 175))  # Cùng kích thước
        self.button_play_clicked = pygame.transform.scale(self.button_play_clicked, (500, 175))  # Cùng kích thước
        self.button_settings = pygame.transform.scale(self.button_settings, (80, 80))
        self.button_sound_on = pygame.transform.scale(self.button_sound_on, (80, 80))
        self.button_sound_off = pygame.transform.scale(self.button_sound_off, (80, 80))

        self.buttons = {
            "play": self.button_play.get_rect(center =(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)),
            "settings": self.button_settings.get_rect(topright=(SCREEN_WIDTH - 10, 10)),
            "sound": self.button_sound_on.get_rect(topright=(SCREEN_WIDTH - 100, 10)),
        }

        self.sound_on = True

        self.music_player = Playmusic()
        self.music_player.play_open_sound()

        self.play_clicked = False  # Biến trạng thái để xác định nút "play" đã click hay chưa
        self.play_hover = False  # Biến trạng thái để xác định chuột có đang rê qua nút "play" không

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()  # Lấy vị trí chuột hiện tại

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Nhấn ESC để thoát
                    pygame.quit()
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Xử lý chỉ khi người dùng click chuột trái
                    if self.buttons["play"].collidepoint(mouse_pos):
                        self.play_clicked = True  # Đánh dấu nút play đã click
                        self.manager.change_scene("play")  # Chuyển cảnh khi nhấn nút play
                    elif self.buttons["settings"].collidepoint(mouse_pos):
                        self.manager.change_scene("settings_open")
                    elif self.buttons["sound"].collidepoint(mouse_pos):
                        self.sound_on = not self.sound_on
                        self.music_player.toggle_sound()

        # Kiểm tra chuột có đang rê qua nút "play" không
        if self.buttons["play"].collidepoint(mouse_pos):
            self.play_hover = True
        else:
            self.play_hover = False

        return True

    def update(self):
        pass

    def render(self):
        # Vẽ ảnh nền
        self.screen.blit(self.bg_image, (0, 0))

        # Vẽ các nút
        if self.play_clicked:
            self.screen.blit(self.button_play_clicked, self.buttons["play"])  # Hiển thị ảnh play khi đã click
        elif self.play_hover:
            self.screen.blit(self.button_play_hover, self.buttons["play"])  # Hiển thị ảnh play khi rê chuột qua
        else:
            self.screen.blit(self.button_play, self.buttons["play"])  # Hiển thị ảnh play bình thường
        
        self.screen.blit(self.button_settings, self.buttons["settings"])
        if self.sound_on:
            self.screen.blit(self.button_sound_on, self.buttons["sound"])
        else:
            self.screen.blit(self.button_sound_off, self.buttons["sound"])
