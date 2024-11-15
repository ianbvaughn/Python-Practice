class CookingBot:
    def __init__(self,cuisine_mode):
        self._currently_cooking=None
        self._cuisine_mode=cuisine_mode
        print(cuisine_mode)

class Recipe:
    def __init__(self,recipe_id,recipe_name,ingredients):
        self._recipe_id=recipe_id
        self._recipe_name=recipe_name
        self._ingredients=ingredients

cb = CookingBot("Canadian") #should create a CookingBot object that cuisine_mode set to "Italian" and currently_cooking set to None.
r1 = Recipe(42, "Poutine", {"water" : "2tbsp", "beef broth" : "20z", "unsalted butter": "6 tbsp", "Russet potatoes":" 2 pounds", "Frying oil":"Sufficient quantity", "pepper":"to taste"}) #should create a Recipe object with the given values for the parameters recipe_id, recipe_name and ingredients respectively.
r2 = Recipe(43, "Chicken tikka masala", None) #should create a Recipe object with the given values for the parameters recipe_id, recipe_name and ingredients respectively.