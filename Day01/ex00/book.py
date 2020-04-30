import datetime

from recipe import Recipe


class Book:
    def __init__(self, name, last_updat):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for value in self.recipes_list.values():
            if value.name == name:
                print(value)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key in self.recipes_list.keys():
            if key == recipe_type:
                print(self.recipes_list[key])

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe type must be class Recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
