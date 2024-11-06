import pygame
import requests

class Symbol():
    def __init__(self):  
        self.image = pygame.image.load('weather_sym.png')     
        self.endimage = self.image.subsurface(pygame.Rect(116, 162, 144, 144)) 

    def draw(self):
        if weather == "Clear":
           self.endimage = self.image.subsurface(pygame.Rect(116, 162, 144, 144)) 
           self.endimage.set_colorkey((38,45,67))
        if weather == "Clouds":
           self.endimage = self.image.subsurface(pygame.Rect(724, 200, 172, 102)) 
           self.endimage.set_colorkey((38,45,67))
        if weather == "Mist" or weather == "Haze" or weather == "Pug":
           self.endimage = self.image.subsurface(pygame.Rect(424, 894, 150, 122)) 
           self.endimage.set_colorkey((38,45,67))
        if weather == "Snow":
           self.endimage = self.image.subsurface(pygame.Rect(1042, 566, 122, 132)) 
           self.endimage.set_colorkey((38,45,67))
        if weather == "Rain":
           self.endimage = self.image.subsurface(pygame.Rect(720, 550, 154, 164)) 
           self.endimage.set_colorkey((38,45,67))
        ekran.blit(self.endimage,(35,130))
        self.endimage.set_colorkey((38,45,67))

api_key = "8dc374c04930a9456fa30c6182ca7961"

pygame.init()

width = 535
height = 380

ekran = pygame.display.set_mode((width, height))
pygame.display.set_caption('Weather App')
pygame.display.set_icon(pygame.image.load('icon.png'))
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 43)
bg = pygame.image.load("backg.png")

input_text = ""
weather = ""
temp = ""
temp_c = ""
city_name = ""

symbol = Symbol()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
              if len(input_text) < 22:
                if input_text: 
                    weather_data = requests.get(
                        f"https://api.openweathermap.org/data/2.5/weather?q={input_text.lower()}&units=imperial&APPID={api_key}")
                    if weather_data.status_code == 200:
                        data = weather_data.json()
                        weather = data["weather"][0]["main"]
                        temp = data["main"]["temp"]
                        temp_c = round((temp - 32) * 5 / 9, 2)
                        city_name = data["name"]
                    else:
                        weather = "City not found"
                        temp = ""
                        temp_c = ""
                        weather = ""
                        city_name = ""
                input_text = "" 
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode 

    ekran.fill((38,45,67))
    ekran.blit(bg,(-50,-50))
    if weather != "":
      symbol.draw()
    pygame.draw.rect(ekran, (0, 0, 0), (115, 43, 300, 40), 2)
    pygame.draw.rect(ekran, (255, 255, 255), (117, 45, 296, 36))
    text_input = font.render(input_text, True, (0, 0, 0))
    ekran.blit(text_input, (120, 50))
    if weather != "":
      text_output = font2.render(f"Weather: {weather}", True, (0, 0, 0))
      ekran.blit(text_output, (200, 145))
    temp_output = font2.render(f"Temperature: {temp}°F", True, (0, 0, 0)) if temp else font.render("", True, (0, 0, 0))
    temp_output2 = font2.render(f"Temperature: {temp_c}°C", True, (0, 0, 0)) if temp_c else font.render("", True, (0, 0, 0))
    temp_output3 = font2.render(f"City: {city_name}", True, (0, 0, 0)) 
    ekran.blit(temp_output, (200, 190))
    ekran.blit(temp_output2, (200, 235))
    if city_name != "":
      ekran.blit(temp_output3, (170, 295))

    pygame.display.flip()

pygame.quit()