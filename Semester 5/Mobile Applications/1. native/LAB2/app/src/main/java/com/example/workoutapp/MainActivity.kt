package com.example.workoutapp

import android.app.Activity
import android.app.AlertDialog
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.appcompat.widget.Toolbar
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.workoutapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var recipeAdapter: RecipeAdapter
    private val recipes = mutableListOf<Recipe>()

    companion object {
        const val ADD_RECIPE_REQUEST_CODE = 1
        const val EDIT_RECIPE_REQUEST_CODE = 2
    }

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //edited import
        val toolbar: Toolbar = findViewById(R.id.toolbar)
        setSupportActionBar(toolbar)
        supportActionBar?.setDisplayShowTitleEnabled(false)

        recipeAdapter = RecipeAdapter(recipes)

        binding.rvRecipeItems.adapter = recipeAdapter
        binding.rvRecipeItems.layoutManager = LinearLayoutManager(this)


        binding.btnAddRecipe.setOnClickListener {
            val intent = Intent(this, AddActivity::class.java)
            startActivityForResult(intent, ADD_RECIPE_REQUEST_CODE)
        }

        binding.btnEditRecipe.setOnClickListener {
            val checkedRecipe = recipes.find { it.isChecked }
            if (checkedRecipe != null) {
                val intent = Intent(this, EditActivity::class.java)
                intent.putExtra("RECIPE_TITLE", checkedRecipe.title)
                intent.putExtra("RECIPE_INGREDIENTS", checkedRecipe.ingredients)
                intent.putExtra("RECIPE_INSTRUCTIONS", checkedRecipe.instructions)
                intent.putExtra("RECIPE_DIFFICULTY", checkedRecipe.difficulty)
                intent.putExtra("RECIPE_TIME", checkedRecipe.time)
                startActivityForResult(intent, EDIT_RECIPE_REQUEST_CODE)
            }
        }

        binding.btnDeleteDoneRecipes.setOnClickListener {
            AlertDialog.Builder(this)
                .setTitle("Delete recipe")
                .setMessage("Are you sure you want to delete this recipe?")
                .setPositiveButton("Yes") { _, _ ->
                    recipeAdapter.deleteDoneRecipes()
                }
                .setNegativeButton("No", null)
                .show()
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode == ADD_RECIPE_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            data?.let { intent ->
                val recipeTitle = intent.getStringExtra("RECIPE_TITLE")
                val recipeIngredients = intent.getStringExtra("RECIPE_INGREDIENTS")
                val recipeInstructions = intent.getStringExtra("RECIPE_INSTRUCTIONS")
                val recipeDifficulty = intent.getIntExtra("RECIPE_DIFFICULTY", 0)
                val recipeTime = intent.getIntExtra("RECIPE_TIME", 0)

                if (recipeTitle != null && recipeIngredients != null && recipeInstructions != null) {
                    val recipe = Recipe(recipeTitle, recipeIngredients, recipeInstructions, recipeDifficulty,recipeTime)
                    recipeAdapter.addRecipe(recipe)
                }
            }
        }

        if (requestCode == EDIT_RECIPE_REQUEST_CODE && resultCode == Activity.RESULT_OK) {
            data?.let { intent ->
                val recipeTitle = intent.getStringExtra("RECIPE_TITLE")
                val recipeIngredients = intent.getStringExtra("RECIPE_INGREDIENTS")
                val recipeInstructions = intent.getStringExtra("RECIPE_INSTRUCTIONS")
                val recipeDifficulty = intent.getIntExtra("RECIPE_DIFFICULTY", 0)
                val recipeTime = intent.getIntExtra("RECIPE_TIME", 0)

                if (recipeTitle != null && recipeIngredients != null && recipeInstructions != null) {
                    val recipe = recipes.find { it.isChecked }
                    if (recipe != null) {
                        recipe.title = recipeTitle
                        recipe.ingredients = recipeIngredients
                        recipe.instructions = recipeInstructions
                        recipe.difficulty = recipeDifficulty
                        recipe.time = recipeTime
                        recipeAdapter.notifyDataSetChanged()
                    }
                }
            }
        }
    }
}