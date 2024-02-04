package com.example.workoutapp

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.workoutapp.databinding.ActivityAddBinding

class AddActivity : AppCompatActivity() {

    private lateinit var binding: ActivityAddBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAddBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnAddRecipe.setOnClickListener {
            val recipeTitle = binding.etRecipeTitle.text.toString()
            val recipeIngredients = binding.etRecipeIngredients.text.toString()
            val recipeInstructions = binding.etRecipeInstructions.text.toString()
            val recipeDifficulty = binding.etRecipeDifficulty.text.toString().toInt()
            val recipeTime = binding.etRecipeTime.text.toString().toInt()

            if(recipeTitle.isNotEmpty() && recipeIngredients.isNotEmpty() && recipeInstructions.isNotEmpty() && recipeDifficulty > 0 && recipeTime > 0) {
                val intent = Intent()
                intent.putExtra("RECIPE_TITLE", recipeTitle)
                intent.putExtra("RECIPE_INGREDIENTS", recipeIngredients)
                intent.putExtra("RECIPE_INSTRUCTIONS", recipeInstructions)
                intent.putExtra("RECIPE_DIFFICULTY", recipeDifficulty)
                intent.putExtra("RECIPE_TIME", recipeTime)
                setResult(Activity.RESULT_OK, intent)
                finish()
            }
        }
    }
}