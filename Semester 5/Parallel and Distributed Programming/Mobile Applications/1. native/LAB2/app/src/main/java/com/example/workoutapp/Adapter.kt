package com.example.workoutapp

import android.graphics.Color
import android.graphics.Paint.STRIKE_THRU_TEXT_FLAG
import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.workoutapp.databinding.ItemBinding

class RecipeAdapter(private val recipes: MutableList<Recipe>) : RecyclerView.Adapter<RecipeAdapter.RecipeViewHolder>()
{

    class RecipeViewHolder(val binding: ItemBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecipeViewHolder {
        val binding = ItemBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return RecipeViewHolder(binding)
    }

    fun addRecipe(recipe: Recipe) {
        recipes.add(recipe)
        notifyItemInserted(recipes.size - 1)
    }

    fun deleteDoneRecipes() {
        recipes.removeAll { recipe ->
            recipe.isChecked
        }
        notifyDataSetChanged()
    }

    private fun toggleStrikeThrough(tvRecipeTitle: TextView, isChecked: Boolean) {
        if(isChecked) {
            tvRecipeTitle.paintFlags = tvRecipeTitle.paintFlags or STRIKE_THRU_TEXT_FLAG
        } else {
            tvRecipeTitle.paintFlags = tvRecipeTitle.paintFlags and STRIKE_THRU_TEXT_FLAG.inv()
        }
    }

    override fun onBindViewHolder(holder: RecipeViewHolder, position: Int) {
        val curRecipe = recipes[position]
        holder.binding.apply {
            tvRecipeTitle.text = curRecipe.title
            tvRecipeIngredients.text = curRecipe.ingredients
            tvRecipeInstructions.text = curRecipe.instructions
            tvRecipeDifficulty.text = "${curRecipe.difficulty} diff"
            tvRecipeTime.text = "${curRecipe.time} mins"

            cbDone.setOnCheckedChangeListener(null)
            cbDone.isChecked = curRecipe.isChecked

            // Set the color based on whether the item is checked
            if (curRecipe.isChecked) {
                root.setBackgroundColor(Color.LTGRAY)
            } else {
                root.setBackgroundColor(Color.WHITE)
            }

            cbDone.setOnCheckedChangeListener { _, isChecked ->
                if (isChecked) {
                    for (recipe in recipes) {
                        recipe.isChecked = false
                    }
                    curRecipe.isChecked = true
                } else {
                    curRecipe.isChecked = false
                }
                holder.itemView.post {
                    notifyDataSetChanged()
                }
            }
        }
    }

    override fun getItemCount(): Int {
        return recipes.size
    }
}