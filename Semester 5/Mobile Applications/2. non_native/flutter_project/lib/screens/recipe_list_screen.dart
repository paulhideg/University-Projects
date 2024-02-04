import 'package:flutter/material.dart';
import 'package:flutter_project/managers/recipe_manager.dart';
import 'package:flutter_project/models/recipe_model.dart';
import 'package:flutter_project/screens/update_recipe_screen.dart';
import 'package:flutter_project/screens/add_recipe_screen.dart';
import 'package:flutter_project/widgets/app_bar.dart';


class RecipeScreen extends StatefulWidget {
  @override
  _RecipeScreenState createState() => _RecipeScreenState();
}

class _RecipeScreenState extends State<RecipeScreen> {
  late List<Recipe> recipes;

  @override
  void initState() {
    super.initState();
    recipes = RecipeManager.getAllRecipes();
  }

  void updateRecipes() {
    setState(() {
      recipes = RecipeManager.getAllRecipes();
    });
  }


  Future<void> _showDeleteConfirmationDialog(int recipeId) async {
    return showDialog<void>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Delete Recipe'),
          content: Text('Are you sure you want to delete this recipe?'),
          actions: <Widget>[
            TextButton(
              onPressed: () {
                Navigator.of(context).pop(); // Close the dialog
              },
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                // Call deleteRecipe function and update the UI
                RecipeManager.deleteRecipe(recipeId);
                updateRecipes();
                Navigator.of(context).pop(); // Close the dialog
              },
              child: Text('Yes'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: buildAppBar(context, updateRecipes),
      body: recipes.isEmpty
          ? Center(
        child: Text('No recipes available.'),
      )
          : ListView.builder(
        itemCount: recipes.length,
        itemBuilder: (context, index) {
          return RecipeItem(
            recipe: recipes[index],
            onUpdate: () {
              _navigateToUpdateScreen(context, recipes[index]);
            },
            onDelete: () {
              _showDeleteConfirmationDialog(recipes[index].id);
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Navigate to the AddMembershipScreen
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => AddRecipeScreen(
                onRecipeAdded: updateRecipes,
              ),
            ),
          );
        },
        child: Text('+'),
      ),
    );
  }



  void _navigateToUpdateScreen(BuildContext context, Recipe recipe) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => UpdateRecipeScreen(
          recipe: recipe,
          onUpdate: () {
            // Update the UI after the recipe is updated
            updateRecipes();
          },
        ),
      ),
    );
  }

}

class RecipeItem extends StatelessWidget {
  final Recipe recipe;
  final VoidCallback onUpdate;
  final VoidCallback onDelete;

  const RecipeItem({
    Key? key,
    required this.recipe,
    required this.onUpdate,
    required this.onDelete,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text('${recipe.id} ${recipe.title}'),
      subtitle: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('Ingredients: ${recipe.ingr}'),
          Text('Instructions: ${recipe.inst}'),
          Text('Difficulty Level: ${recipe.level}'),
          Text('Cooking Time: ${recipe.time}')
        ],
      ),
      trailing: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          IconButton(
            icon: Icon(Icons.edit),
            onPressed: onUpdate,
          ),
          IconButton(
            icon: Icon(Icons.delete),
            onPressed: onDelete,
          ),
        ],
      ),
    );
  }
}


