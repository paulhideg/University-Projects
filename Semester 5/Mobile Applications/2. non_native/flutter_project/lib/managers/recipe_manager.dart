import 'package:flutter_project/models/recipe_model.dart';

class RecipeManager {
  static List<Recipe> recipes = [];
  static int _lastrecipeId = 0;


  static void addRecipe(Recipe newRecipe) {
    recipes.add(newRecipe);
  }

  static void updateRecipe(Recipe updatedRecipe) {
    final index = recipes.indexWhere((recipe) => recipe.id == updatedRecipe.id);
    if (index != -1) {
      recipes[index] = updatedRecipe;
    }
  }

  static void deleteRecipe(int recipeId) {
    recipes.removeWhere((recipe) => recipe.id == recipeId);
  }

  // Function to generate a new auto-incremented recipe ID
  static int generateNewRecipeId() {
    _lastrecipeId++;
    return _lastrecipeId;
  }

  static List<Recipe> getAllRecipes() {
    // Return a copy of the recipes list to avoid direct manipulation
    return List.from(recipes);
  }
}

