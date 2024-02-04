package com.example.kotlin_db_1

import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView

class RecipesAdapter(private var recipes : List<Recipe>, context: Context) :
    RecyclerView.Adapter<RecipesAdapter.RecipeViewHolder>() {

        private val db: RecipeDatabaseHelper = RecipeDatabaseHelper(context)

    class RecipeViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView){
        val titleTextView : TextView = itemView.findViewById(R.id.titleTextView)
        val ingrTextView : TextView = itemView.findViewById(R.id.ingrTextView)
        val instTextView : TextView = itemView.findViewById(R.id.instTextView)
        val diffTextView : TextView = itemView.findViewById(R.id.diffTextView)
        val timeTextView : TextView = itemView.findViewById(R.id.timeTextView)
        val updateButton : ImageView = itemView.findViewById(R.id.updateButton)
        val deleteButton : ImageView = itemView.findViewById(R.id.deleteButton)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecipeViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.recipe_item, parent, false)
        return RecipeViewHolder(view)
    }

    override fun getItemCount(): Int = recipes.size

    override fun onBindViewHolder(holder: RecipeViewHolder, position: Int) {
        val recipe = recipes[position]
        holder.titleTextView.text = recipe.title
        holder.ingrTextView.text = recipe.ingr
        holder.instTextView.text = recipe.inst
        holder.diffTextView.text = recipe.diff
        holder.timeTextView.text = recipe.time

        holder.updateButton.setOnClickListener {
            val intent = Intent(holder.itemView.context, UpdateRecipeActivity::class.java).apply {
                putExtra("recipe_id", recipe.id)
            }
            holder.itemView.context.startActivity(intent)
        }

        holder.deleteButton.setOnClickListener {
            db.deleteRecipe(recipe.id)
            refreshData(db.getAlRecipes())
            Toast.makeText(holder.itemView.context, "Recipe Deleted", Toast.LENGTH_SHORT).show()
        }

    }

    fun refreshData(newRecipes: List<Recipe>) {
        recipes = newRecipes
        notifyDataSetChanged()
    }

}