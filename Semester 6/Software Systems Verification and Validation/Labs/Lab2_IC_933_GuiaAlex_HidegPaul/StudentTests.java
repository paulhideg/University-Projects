package ssvv.example;


import domain.Student;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.function.Executable;
import repository.NotaXMLRepo;
import repository.StudentXMLRepo;
import repository.TemaXMLRepo;
import service.Service;
import validation.NotaValidator;
import validation.StudentValidator;
import validation.TemaValidator;
import validation.ValidationException;



import java.util.Random;

public class StudentTests {
    private final StudentValidator studentValidator;
    private final TemaValidator temaValidator;
    private final StudentXMLRepo studentXMLRepository;
    private final TemaXMLRepo temaXMLRepository;
    private final NotaValidator notaValidator;
    private final NotaXMLRepo notaXMLRepository;
    private final Service service;

    public StudentTests() {
        this.studentValidator = new StudentValidator();
        this.temaValidator = new TemaValidator();

        String filenameStudent = "fisiere/Studenti.xml";
        String filenameTema = "fisiere/Teme.xml";
        String filenameNota = "fisiere/Note.xml";

        this.studentXMLRepository = new StudentXMLRepo(filenameStudent);
        this.temaXMLRepository = new TemaXMLRepo(filenameTema);
        this.notaValidator = new NotaValidator(this.studentXMLRepository, this.temaXMLRepository);
        this.notaXMLRepository = new NotaXMLRepo(filenameNota);
        this.service = new Service(this.studentXMLRepository, this.studentValidator, this.temaXMLRepository, this.temaValidator, this.notaXMLRepository, this.notaValidator);
    }

    @Test
    public void testAddStudent(){
        StudentValidator studentValidator = new StudentValidator();
        TemaValidator temaValidator = new TemaValidator();
        String filenameStudent = "fisiere/Studenti.xml";
        String filenameTema = "fisiere/Teme.xml";
        String filenameNota = "fisiere/Note.xml";

        StudentXMLRepo studentXMLRepository = new StudentXMLRepo(filenameStudent);
        TemaXMLRepo temaXMLRepository = new TemaXMLRepo(filenameTema);
        NotaValidator notaValidator = new NotaValidator(studentXMLRepository, temaXMLRepository);
        NotaXMLRepo notaXMLRepository = new NotaXMLRepo(filenameNota);
        Service service = new Service(studentXMLRepository, studentValidator, temaXMLRepository, temaValidator, notaXMLRepository, notaValidator);
        Student student = new Student("1", "paul", 933, "paul@gmail.com");
        Student student1 = service.addStudent(student);
        Assertions.assertEquals(student, student1);
        Assertions.assertNotEquals(null, student1);
    }
    @Test
    public void TestValidInput(){
        // 1
        //test valid input fields
        Student hwStudent1 = new Student("1", "paul", 933, "paul@gmail.com");
        Assertions.assertEquals(hwStudent1, service.addStudent(hwStudent1));
    }
    @Test
    public void TestEmptyId(){
        // 2
        //Empty id -> it shouldn't work
        Student hwStudent2 = new Student("", "paul", 933, "paul@gmail.com");
//        Assertions.assertEquals(hwStudent4, service.addStudent(hwStudent4));
        Assertions.assertThrows(ValidationException.class, () ->{ service.addStudent(hwStudent2);});
    }
    @Test
    public void TestNullId(){
        // 3
        //try to add a student with a null id => it shouldn't work
        Student hwStudent3 = new Student(null, "paul", 933, "paul@gmail.com");
        Assertions.assertThrows(ValidationException.class, () ->{ service.addStudent(hwStudent3);});
    }

    @Test
    public void TestExistingId(){
        // 4
        //id student = 1 => it already exists => it shouldn't work, but it does => ERROR
        Student hwStudent5 = new Student("1", "paul", 933, "paul@gmail.com");
        Assertions.assertNotEquals(null, service.findStudent("1"));
        service.addStudent(hwStudent5);
        Assertions.assertNotEquals(hwStudent5, service.findStudent("1"));
    }
    @Test
    public void TestEmptyName(){
        // 5
        //try to add a student with a empty name => it shouldn't work
        Student hwStudent5 = new Student("1", "", 933, "alex@gmail.com");
        Assertions.assertThrows(ValidationException.class, () ->{ service.addStudent(hwStudent5);});
    }
    @Test
    public void TestNullName(){
        // 6
        //try to add a student with a null name => it shouldn't work
        Student hwStudent6 = new Student("1", null, 933, "alex@gmail.com");
        Assertions.assertThrows(ValidationException.class, () ->{ service.addStudent(hwStudent6);});
    }
    @Test
    public void TestNegativeGroup(){
        // 7
        //try to add a student from a group that is a negative number
        Student hwStudent7 = new Student("1", "alex", -933, "alex@gmail.com");
        Assertions.assertThrows(ValidationException.class, () ->{ service.addStudent(hwStudent7);});
    }
    @Test
    public void TestNullEmail(){
        // 8
        //try to add a student with a null email
        Student hwStudent8 = new Student("1", "alex", 933, null);
        Assertions.assertThrows(ValidationException.class, () ->{ service.addStudent(hwStudent8);});
    }
    @Test
    public void TestEmptyEmail(){
        // 9
        //try to add a student that has an email that is an empty string
        Student hwStudent9 = new Student("1", "alex", 933, "");
        Assertions.assertThrows(ValidationException.class, () ->{ service.addStudent(hwStudent9);});
    }

    @Test
    public void TestZeroGroup(){
        // 10
        //try to add a student with the group as 0
        Student hwStudent10 = new Student("1", "alex", 0, "alex@gmail.com");
        Assertions.assertEquals(hwStudent10, service.addStudent(hwStudent10));
    }
}