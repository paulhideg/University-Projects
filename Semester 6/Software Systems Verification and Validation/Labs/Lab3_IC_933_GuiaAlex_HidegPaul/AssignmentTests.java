
package ssvv.example;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import domain.Tema;
import repository.NotaXMLRepo;
import repository.StudentXMLRepo;
import repository.TemaXMLRepo;
import service.Service;
import validation.NotaValidator;
import validation.StudentValidator;
import validation.TemaValidator;
import validation.ValidationException;

public class AssignmentTests {
    private final StudentValidator studentValidator;
    private final TemaValidator temaValidator;
    private final StudentXMLRepo studentXMLRepository;
    private final TemaXMLRepo temaXMLRepository;
    private final NotaValidator notaValidator;
    private final NotaXMLRepo notaXMLRepository;
    private final Service service;

    public AssignmentTests() {
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
    public void testAddAssignment(){

        Tema assignment = new Tema("1", "Nice job", 10, 1);
        Tema assignment1 = service.addTema(assignment);
        //assert that the assignment is added
        Assertions.assertEquals(assignment, assignment1);

    }
    @Test
    public void testAddAssignmentNullNr(){

        Tema assignment = new Tema(null, "Nice job", 10, 1);
        //assert that the an exception is thrown
        Assertions.assertThrows(ValidationException.class, () -> {
            service.addTema(assignment);
        });

    }


}
