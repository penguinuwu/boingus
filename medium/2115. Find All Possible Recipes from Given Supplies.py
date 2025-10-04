"""
22:22.26
O(r+i+s) where r=recipes, i=ingredients, s=supplies
sO(r+s)
"""


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        supplies_set = set(supplies)
        recipes_dict = {recipes[i]: i for i in range(len(recipes))}

        def we_can_make(key):
            if key in supplies_set:
                return True
            if key not in recipes_dict:
                return False

            index = recipes_dict[key]
            del recipes_dict[key]

            for ingred in ingredients[index]:
                if not we_can_make(ingred):
                    return False

            supplies_set.add(key)
            return True

        can_make = []
        for r in recipes:
            if we_can_make(r):
                can_make.append(r)

        return can_make
