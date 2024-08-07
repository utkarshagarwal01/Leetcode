#
# @lc app=leetcode id=2115 lang=python
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """

        r_index = {r:i for i, r in enumerate(recipes)}

        supplies = set(supplies)

        visited, visiting = set(), set()

        def dfs(recipe):
            if recipe in visited:
                return True 
            
            if recipe in supplies:
                visited.add(recipe)
                return True
            
            if recipe in visiting:
                return False

            visiting.add(recipe)

            ingredients_index = r_index.get(recipe, None)
            if ingredients_index is None:
                return dfs(recipe)

            for ingredient in ingredients[ingredients_index]:
                if not dfs(ingredient):
                    return False
                
                
            visiting.remove(recipe)
            visited.add(recipe)
            return True


        result = []
        for recipe in recipes:
            if dfs(recipe):
                result.append(recipe)

        return result 

            
# @lc code=end

