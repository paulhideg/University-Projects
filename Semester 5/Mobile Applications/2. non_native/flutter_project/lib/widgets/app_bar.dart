import 'package:flutter/material.dart';
import 'package:flutter_project/screens/add_recipe_screen.dart';


AppBar buildAppBar(BuildContext context, Function updateRecipes) {
  return AppBar(
    title: Text('Sous Chef App'),
    actions: [
      IconButton(
        icon: Icon(Icons.add),
        onPressed: () {
          // Navigate to the AddRecipeScreen
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => AddRecipeScreen(
                onRecipeAdded: updateRecipes(),
              ),
            ),
          );
        },
      ),
    ],
  );
}
