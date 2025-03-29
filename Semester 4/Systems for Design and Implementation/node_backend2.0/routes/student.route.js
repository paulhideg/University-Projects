const express = require("express");
const router = express.Router();
// const Student = require("../models/student.model");
const {
  getProducts,
  saveStudent,
  getStudent,
  updateStudent,
  deleteStudent,
} = require("../controllers/student.controller");

// Get all student
router.get("/get/students", getProducts);

// Create a student
router.post("/save/student", saveStudent);

// Get student by id
router.get("/get/student/:id", getStudent);

// Update student by id
router.put("/update/student/:id", updateStudent);

// Delete student by id
router.delete("/delete/student/:id", deleteStudent);

module.exports = router;
