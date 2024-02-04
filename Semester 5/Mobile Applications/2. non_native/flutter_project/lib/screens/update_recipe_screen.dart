import 'package:flutter/material.dart';
import 'package:flutter_project/managers/recipe_manager.dart';
import 'package:flutter_project/models/recipe_model.dart';

class UpdateRecipeScreen extends StatefulWidget {
  final Recipe recipe;
  final VoidCallback onUpdate;

  UpdateRecipeScreen({required this.recipe, required this.onUpdate});

  @override
  _UpdateRecipeScreenState createState() => _UpdateRecipeScreenState();
}

class _UpdateRecipeScreenState extends State<UpdateRecipeScreen> {
  late TextEditingController titleController;
  late TextEditingController ingrController;
  late TextEditingController instController;
  late TextEditingController levelController;
  late TextEditingController timeController;

  @override
  void initState() {
    super.initState();
    titleController = TextEditingController(text: widget.recipe.title);
    ingrController = TextEditingController(text: widget.recipe.ingr);
    instController = TextEditingController(text: widget.recipe.inst);
    levelController = TextEditingController(text: widget.recipe.level);
    timeController = TextEditingController(text: widget.recipe.time);
  }

  @override
  void dispose() {
    // Ensure that there are no lingering references or resources
    // Tied to the text input fields after the widget is no longer needed.
    titleController.dispose();
    ingrController.dispose();
    instController.dispose();
    levelController.dispose();
    timeController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Update Recipe'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              TextField(
                controller: titleController,
                decoration: InputDecoration(labelText: 'Title'),
              ),
              TextField(
                controller: ingrController,
                decoration: InputDecoration(labelText: 'Ingredients'),
              ),
              TextField(
                controller: instController,
                decoration: InputDecoration(labelText: 'Instructions'),
              ),
              TextField(
                controller: levelController,
                decoration: InputDecoration(labelText: 'Difficulty Level'),
              ),
              TextField(
                controller: timeController,
                decoration: InputDecoration(labelText: 'Cooking Time'),
              ),

              SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  // Validate and update recipe
                  _updateRecipe();
                },
                child: Text('Submit'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showErrorDialog(String errorMessage) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('Error'),
          content: Text(errorMessage),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }


  void _updateRecipe() {
    // Perform validation and update membership in the list
    // Removes any leading or trailing whitespace
    final title = titleController.text.trim();
    final ingr = ingrController.text.trim();
    final inst = instController.text.trim();
    final level = levelController.text.trim();
    final time = timeController.text.trim();


    if (title.isNotEmpty && ingr.isNotEmpty && inst.isNotEmpty && level.isNotEmpty && time.isNotEmpty) {
      final updatedRecipe = widget.recipe.copyWith(
        title: title,
        ingr: ingr,
        inst: inst,
        level: level,
        time: time,
      );

      RecipeManager.updateRecipe(updatedRecipe);

      // Notify the parent screen about the update
      widget.onUpdate();

      // Navigate back to the recipe list screen
      Navigator.pop(context);
    } else {
      // Display an error message or handle invalid input
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Error'),
            content: Text('Please fill in all required fields.'),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: Text('OK'),
              ),
            ],
          );
        },
      );
    }
  }
}
