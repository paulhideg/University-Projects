import 'package:flutter/material.dart';

Card buildMembershipCard({
  required String title,
  required String ingr,
  required String id,
  required String inst,
  required String level,
  required String time,

  required Function onUpdate,
  required Function onDelete,
}) {
  return Card(
    elevation: 4.0,
    margin: EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(16.0), // Adjust the radius as needed
    ),
    child: ClipRRect(
      borderRadius: BorderRadius.circular(16.0),
      child: ListTile(
        title: Text('$id $title'),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Ingredients: $ingr'),
            Text('Instructions: $inst'),
            Text('Difficulty Level: $level'),
            Text('Cooking Time: $time'),
            // Add other details as needed
          ],
        ),
        trailing: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            IconButton(
              icon: Icon(Icons.edit),
              onPressed: onUpdate(),
            ),
            IconButton(
              icon: Icon(Icons.delete),
              onPressed: onDelete(),
            ),
          ],
        ),
      ),
    ),
  );
}
