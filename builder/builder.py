import pygame
import sys
from abc import ABC, abstractmethod

# Define the product class
class Sandwich:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def display(self):
        print(self.ingredients)

# Define the abstract builder class
class SandwichBuilder(ABC):
    def __init__(self):
        self.sandwich = None

    def create_new_sandwich(self):
        self.sandwich = Sandwich()

    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_filling(self):
        pass

    def get_result(self):
        return self.sandwich

# Define concrete builders
class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredient("Wheat Bread")

    def add_filling(self):
        self.sandwich.add_ingredient("Lettuce")
        self.sandwich.add_ingredient("Tomato")
        self.sandwich.add_ingredient("Cucumber")


class HamSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredient("White Bread")

    def add_filling(self):
        self.sandwich.add_ingredient("Lettuce")
        self.sandwich.add_ingredient("Tomato")
        self.sandwich.add_ingredient("Ham")

# Define the director class
class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_result()

# Helper method
def draw_text(screen, text, x, y, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sandwich Builder")
font = pygame.font.Font(pygame.font.get_default_font(), 18)

# Client code
veggie_builder = VeggieSandwichBuilder()
director = SandwichDirector(veggie_builder)
veggie_sandwich = director.build_sandwich()

ham_builder = HamSandwichBuilder()
director.builder = ham_builder
ham_sandwich = director.build_sandwich()

# Main loop
while True:
    screen.fill((255,255,255))

    draw_text(screen, "Veggie Sandwich:", 10, 10, font, (0, 0, 0))
    for index, ingredient in enumerate(veggie_sandwich.ingredients):
        draw_text(screen, f"{index}: {ingredient}", 10, 40 + index * 30, font, (0, 0, 0))

    draw_text(screen, "Ham Sandwich:", 300, 10, font, (0, 0, 0))
    for index, ingredient in enumerate(veggie_sandwich.ingredients):
        draw_text(screen, f"{index}: {ingredient}", 300, 40 + index * 30, font, (0, 0, 0))

    # Update display
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()