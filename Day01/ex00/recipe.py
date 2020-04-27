class Recipe:
    def __init__(
        self,
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingr: list,
        description,
        recipe_type: str,
    ):
        if not 1 <= cooking_lvl <= 5:
            raise ValueError("cooking_lvl should be in range 0, 5")
        if not cooking_time >= 0:
            raise ValueError("cooking time should not be negative")
        if recipe_type != "starter" and "lunch" and "dessert":
            raise ValueError("wrong recipte type")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingr = ingr
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = """this class takes parameters as follows:
     name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description,recipe_type: str """
        return txt


# def main():
#     while True:
#         raw = input()
#         try:
#             cooking_lvl = int(raw)
#             break
#         except TypeError as exc:
#             print(str(exc))

#     try:
#         r = Recipe("test", 4)
#     except ValueError as exc:
#         pass

#     print(r.name)
#     print(r.cooking_lvl)


# main()
