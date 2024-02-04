package com.example.kotlin_db_1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.kotlin_db_1.databinding.ActivityUpdateBinding

class UpdateRecipeActivity : AppCompatActivity() {

    private lateinit var binding : ActivityUpdateBinding
    private lateinit var db: RecipeDatabaseHelper
    private var recipeId: Int = -1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityUpdateBinding.inflate(layoutInflater)
        setContentView(binding.root)

        db = RecipeDatabaseHelper(this)

        recipeId = intent.getIntExtra("recipe_id", -1)
        if (recipeId == -1){
            finish()
            return
        }

        val recipe = db.getRecipeByID(recipeId)
        binding.updateTitleEditText.setText(recipe.title)
        binding.updateIngrEditText.setText(recipe.ingr)
        binding.updateInstEditText.setText(recipe.inst)
        binding.updateDiffEditText.setText(recipe.diff)
        binding.updateTimeEditText.setText(recipe.time)

        binding.updateSaveButton.setOnClickListener {
            val newTitle = binding.updateTitleEditText.text.toString()
            val newIngr = binding.updateIngrEditText.text.toString()
            val newInst = binding.updateInstEditText.text.toString()
            val newDiff = binding.updateDiffEditText.text.toString()
            val newTime = binding.updateTimeEditText.text.toString()
            val updatedRecipe = Recipe(recipeId, newTitle, newIngr, newInst, newDiff, newTime)
            db.updateRecipe(updatedRecipe)
            finish()
            Toast.makeText(this, "Changes Saved", Toast.LENGTH_SHORT).show()
        }

    }
}