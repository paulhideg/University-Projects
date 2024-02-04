package com.example.workoutapp

data class Recipe(
    var title: String,
    var ingredients: String,
    var instructions: String,
    var difficulty: Int,
    var time: Int,
    var isChecked: Boolean = false
)