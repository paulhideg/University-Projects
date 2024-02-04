package com.example.kotlin_db_1

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.kotlin_db_1.databinding.ActivityAddRecipeBinding

class AddRecipeActivity : AppCompatActivity() {

    private lateinit var binding: ActivityAddRecipeBinding
    private lateinit var db: RecipeDatabaseHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAddRecipeBinding.inflate(layoutInflater)
        setContentView(binding.root)

        db = RecipeDatabaseHelper(this)

        binding.saveButton.setOnClickListener {
            val title = binding.titleEditText.text.toString()
            val ingr = binding.ingrEditText.text.toString()
            val inst = binding.instEditText.text.toString()
            val diff = binding.diffEditText.text.toString()
            val time = binding.timeEditText.text.toString()
            val recipe = Recipe(0, title, ingr, inst, diff, time)
            db.insertRecipe(recipe)
            finish()
            Toast.makeText(this, "Recipe Saved", Toast.LENGTH_SHORT).show()

        }
    }
}