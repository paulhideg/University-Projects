const express = require("express");
const mongoose = require("mongoose");
const Student = require("./models/student.model");
const studentRoute = require("./routes/student.route");
const Course = require("./models/course.model");

const { faker } = require("@faker-js/faker");

const serv = 9090;
const app = express();

//middleware
app.use(express.json());

// Curb Chrome CORS Error by adding a header here
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content, Accept, Content-Type, Authorization"
  );
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, PUT, DELETE, PATCH, OPTIONS"
  );
  next();
});

mongoose
  .connect(
    "mongodb+srv://admin:admin@nodebackend.qbovm6i.mongodb.net/Node-API?retryWrites=true&w=majority&appName=NodeBackend"
  )
  .then(() => {
    console.log("Connected to database!");
    app.listen(serv, () => {
      console.log(`Server is running on port ${serv}`);
    });
  })
  .catch((err) => console.log(err));

// routes
app.use("/", studentRoute);
// app.use("/course", courseRoute)

//default
app.get("/", (req, res) => {
  res.send("Hello from API");
});

// Get all courses
app.get("/courses", async (req, res) => {
  try {
    const courses = await Course.find().populate("student");
    res.json(courses);
  } catch (err) {
    res.status(500).json({
      message: err.message,
    });
  }
});

// Add 5 students with 3 courses each
app.post("/add/sample", async (req, res) => {
  try {
    for (let i = 0; i < 5; i++) {
      const student1 = await Student.create({
        studentName: `Student ${i + 1}`,
        studentYear: i + 1,
        studentAverage: i + 1,
      });
      const course1 = await Course.create({
        courseName: `Course ${i + 1}`,
        courseDifficulty: i,
        student: student1._id,
      });
      const course2 = await Course.create({
        courseName: `Course ${i + 2}`,
        courseDifficulty: i,
        student: student1._id,
      });
      const course3 = await Course.create({
        courseName: `Course ${i + 3}`,
        courseDifficulty: i,
        student: student1._id,
      });
      student1.courses.push(course1._id, course2._id, course3._id);
      await student1.save();
    }
    res.status(200).json({
      success: true,
    });
  } catch (err) {
    res.status(500).json({
      message: err.message,
    });
  }
});

// Add students with courses using faker
app.post("/add/sample/faker", async (req, res) => {
  try {
    for (let i = 0; i < 5; i++) {
      const student1 = await Student.create({
        studentName: faker.person.fullName(),
        studentYear: faker.number.int({ min: 1, max: 5 }),
        studentAverage: faker.number.float({
          min: 1,
          max: 10,
          fractionDigits: 2,
        }),
      });
      for (let j = 0; j < 3; j++) {
        const course1 = await Course.create({
          courseName: faker.word.noun(),
          courseDifficulty: faker.number.int({ min: 1, max: 5 }),
          student: student1._id,
        });
        student1.courses.push(course1._id);
      }
      await student1.save();
    }
    res.status(200).json({
      success: true,
    });
  } catch (err) {
    res.status(500).json({
      message: err.message,
    });
  }
});

// Get number of cpurses of a student
app.get("/get/student/:id/nrcourses", async (req, res) => {
  try {
    const { id } = req.params;
    const student = await Student.findById(id);
    res.json(student.courses.length);
  } catch (err) {
    res.status(500).json({
      message: err.message,
    });
  }
});
