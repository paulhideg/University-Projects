package com.example.workoutapp

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.workoutapp.databinding.ActivityEditBinding

class EditActivity : AppCompatActivity() {

    private lateinit var binding: ActivityEditBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityEditBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Get the current todo details from the intent
        val recipeTitle = intent.getStringExtra("RECIPE_TITLE")
        val recipeIngredients = intent.getStringExtra("RECIPE_INGREDIENTS")
        val recipeInstructions = intent.getStringExtra("RECIPE_INSTRUCTIONS")
        val recipeDifficulty = intent.getIntExtra("RECIPE_DIFFICULTY", 0)
        val recipeTime = intent.getIntExtra("RECIPE_TIME", 0)

        // Set the current todo details in the EditText fields
        binding.etRecipeTitle.setText(recipeTitle)
        binding.etRecipeIngredients.setText(recipeIngredients)
        binding.etRecipeInstructions.setText(recipeInstructions)
        binding.etRecipeDifficulty.setText(recipeDifficulty.toString())
        binding.etRecipeTime.setText(recipeTime.toString())

        binding.btnEditRecipe.setOnClickListener {
            val newRecipeTitle = binding.etRecipeTitle.text.toString()
            val newRecipeIngredients = binding.etRecipeIngredients.text.toString()
            val newRecipeInstructions = binding.etRecipeInstructions.text.toString()
            val newRecipeDifficulty = binding.etRecipeDifficulty.text.toString().toInt()
            val newRecipeTime = binding.etRecipeTime.text.toString().toInt()

            if(newRecipeTitle.isNotEmpty() && newRecipeIngredients.isNotEmpty()  && newRecipeInstructions.isNotEmpty() && newRecipeDifficulty > 0 && newRecipeTime > 0) {
                val intent = Intent()
                intent.putExtra("RECIPE_TITLE", newRecipeTitle)
                intent.putExtra("RECIPE_INGREDIENTS", newRecipeIngredients)
                intent.putExtra("RECIPE_INSTRUCTIONS", newRecipeInstructions)
                intent.putExtra("RECIPE_DIFFICULTY", newRecipeDifficulty)
                intent.putExtra("RECIPE_TIME", newRecipeTime)
                setResult(Activity.RESULT_OK, intent)
                finish()
            }
        }
    }
}