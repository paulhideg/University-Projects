package com.example.kotlin_db_1

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class RecipeDatabaseHelper(context: Context) : SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {

    companion object{
        private const val DATABASE_NAME = "recipesapp.db"
        private const val DATABASE_VERSION = 1
        private const val TABLE_NAME = "allrecipes"
        private const val COLUMN_ID = "id"
        private const val COLUMN_TITLE = "title"
        private const val COLUMN_INGR = "ingr"
        private const val COLUMN_INST = "inst"
        private const val COLUMN_DIFF = "diff"
        private const val COLUMN_TIME = "time"
    }

    override fun onCreate(db: SQLiteDatabase?) {
        val createTableQuery = "CREATE TABLE $TABLE_NAME ($COLUMN_ID INTEGER PRIMARY KEY, $COLUMN_TITLE TEXT, $COLUMN_INGR TEXT, $COLUMN_INST TEXT, $COLUMN_DIFF TEXT, $COLUMN_TIME TEXT)"
        db?.execSQL(createTableQuery)
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        val dropTableQuery = "DROP TABLE IF EXISTS $TABLE_NAME"
        db?.execSQL(dropTableQuery)
        onCreate(db)
    }

    fun insertRecipe(recipe: Recipe) {
        val db = writableDatabase
        val values = ContentValues().apply {
            put(COLUMN_TITLE, recipe.title)
            put(COLUMN_INGR, recipe.ingr)
            put(COLUMN_INST, recipe.inst)
            put(COLUMN_DIFF, recipe.diff)
            put(COLUMN_TIME, recipe.time)
        }
        db.insert(TABLE_NAME, null, values)
        db.close()
    }

    fun getAlRecipes(): List<Recipe> {
        val recipesList = mutableListOf<Recipe>()
        val db = readableDatabase
        val query = "SELECT * FROM $TABLE_NAME"
        val cursor = db.rawQuery(query, null)

        while (cursor.moveToNext()){
            val id = cursor.getInt(cursor.getColumnIndexOrThrow(COLUMN_ID))
            val title = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_TITLE))
            val ingr = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_INGR))
            val inst = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_INST))
            val diff = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_DIFF))
            val time = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_TIME))

            val recipe = Recipe(id, title, ingr, inst, diff, time)
            recipesList.add(recipe)
        }
        cursor.close()
        db.close()
        return recipesList
    }

    fun updateRecipe(recipe: Recipe) {
        val db = writableDatabase
        val values = ContentValues().apply {
            put(COLUMN_TITLE, recipe.title)
            put(COLUMN_INGR, recipe.ingr)
            put(COLUMN_INST, recipe.inst)
            put(COLUMN_DIFF, recipe.diff)
            put(COLUMN_TIME, recipe.time)
        }
        val whereClause = "$COLUMN_ID = ?"
        val whereArgs = arrayOf(recipe.id.toString())
        db.update(TABLE_NAME, values, whereClause, whereArgs)
        db.close()
    }

    fun getRecipeByID(recipeID: Int): Recipe {
        val db = readableDatabase
        val query = "SELECT * FROM $TABLE_NAME WHERE $COLUMN_ID = $recipeID"
        val cursor = db.rawQuery(query, null)
        cursor.moveToFirst()

        val id = cursor.getInt(cursor.getColumnIndexOrThrow(COLUMN_ID))
        val title = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_TITLE))
        val ingr = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_INGR))
        val inst = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_INST))
        val diff = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_DIFF))
        val time = cursor.getString(cursor.getColumnIndexOrThrow(COLUMN_TIME))

        cursor.close()
        db.close()
        return Recipe(id, title, ingr, inst, diff, time)
    }

    fun deleteRecipe(recipeID: Int) {
        val db = writableDatabase
        val whereClause = "$COLUMN_ID = ?"
        val whereArgs = arrayOf(recipeID.toString())
        db.delete(TABLE_NAME, whereClause, whereArgs)
        db.close()
    }

}