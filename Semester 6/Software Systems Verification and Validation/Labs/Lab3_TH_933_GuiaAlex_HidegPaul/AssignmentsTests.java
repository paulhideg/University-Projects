package ssvv.example;

import domain.Tema;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeAll;
import repository.NotaXMLRepo;
import repository.StudentXMLRepo;
import repository.TemaXMLRepo;
import service.Service;
import validation.NotaValidator;
import validation.StudentValidator;
import validation.TemaValidator;
import validation.ValidationException;

public class AssignmentsTests {

    public static Service service;

    @BeforeAll
    public static void setup() {
        StudentValidator studentValidator = new StudentValidator();
        TemaValidator temaValidator = new TemaValidator();
        String filenameStudent = "fisiere/Studenti.xml";
        String filenameTema = "fisiere/Teme.xml";
        String filenameNota = "fisiere/Note.xml";

        StudentXMLRepo studentXMLRepository = new StudentXMLRepo(filenameStudent);
        TemaXMLRepo temaXMLRepository = new TemaXMLRepo(filenameTema);
        NotaValidator notaValidator = new NotaValidator(studentXMLRepository, temaXMLRepository);
        NotaXMLRepo notaXMLRepository = new NotaXMLRepo(filenameNota);
        AssignmentsTests.service = new Service(studentXMLRepository, studentValidator, temaXMLRepository, temaValidator, notaXMLRepository, notaValidator);
    }

    // White box testing
    @Test
    public void addTema_ValidData_CreateSuccessfully() {
        String nrTema = "100";
        String descriere = "desc";
        int deadline = 12;
        int primire = 1;
        Tema tema = new Tema(nrTema, descriere, deadline, primire);
        try {
            service.addTema(tema);
            assert(true);
        } catch (ValidationException exception) {
            assert(false);
        }
    }

    @Test
    public void addTema_Invalid_nrTema_duplicate_ThrowsError() {
        String nrTema = "100";
        String descriere = "desc";
        int deadline = 12;
        int primire = 1;
        Tema tema = new Tema(nrTema, descriere, deadline, primire);
        try {
            Tema response = service.addTema(tema);
            assert(tema == response);
        } catch (ValidationException exception) {
            assert(true);
        }
    }

    @Test
    public void addTema_Invalid_nrTema_emptyString_ThrowsError() {
        String nrTema = "";
        String descriere = "desc";
        int deadline = 12;
        int primire = 2;
        Tema tema = new Tema(nrTema, descriere, deadline, primire);
        try {
            service.addTema(tema);
            assert(false);
        } catch (ValidationException exception) {
            assert(true);
        }
    }

    @Test
    public void addTema_Invalid_nrTema_null_ThrowsError() {
        String nrTema = null;
        String descriere = "desc";
        int deadline = 12;
        int primire = 2;
        Tema tema = new Tema(nrTema, descriere, deadline, primire);
        try {
            service.addTema(tema);
            assert(false);
        } catch (ValidationException exception) {
            assert(true);
        }
    }

    @Test
    public void addTema_Invalid_descriere_emptyString_ThrowsError() {

        String nrTema = "101";
        String descriere = "";
        int deadline = 12;
        int primire = 2;

        Tema tema = new Tema(nrTema, descriere, deadline, primire );

        try{
            service.addTema(tema);
            assert(false);

        }catch (ValidationException ve){
            assert(true);

        }

    }


    @Test
    public void addTema_Invalid_deadline_smallerThan1_ThrowsError() {

        String nrTema = "102";
        String descriere = "desc";
        int deadline = 0;
        int primire = 11;

        Tema tema = new Tema(nrTema, descriere, deadline, primire );

        try{
            service.addTema(tema);
            assert(false);

        }catch (ValidationException ve){
            assert(true);

        }

    }

    @Test
    public void addTema_Invalid_deadline_smallerThan1_ThrowsError1() {

        String nrTema = "102";
        String descriere = "desc";
        int deadline = 0;
        int primire = 11;

        Tema tema = new Tema(nrTema, descriere, deadline, primire );

        try{
            service.addTema(tema);
            assert(false);

        }catch (ValidationException ve){
            assert(true);

        }

    }

    @Test
    public void addTema_Invalid_deadline_greaterThan14_ThrowsError() {

        String nrTema = "102";
        String descriere = "desc";
        int deadline = 15;
        int primire = 11;

        Tema tema = new Tema(nrTema, descriere, deadline, primire );

        try{
            service.addTema(tema);
            assert(false);

        }catch (ValidationException ve){
            assert(true);

        }

    }

    @Test
    public void addTema_Invalid_primire_smallerThan1_ThrowsError() {

        String nrTema = "103";
        String descriere = "desc";
        int deadline = 12;
        int primire = 0;

        Tema tema = new Tema(nrTema, descriere, deadline, primire );

        try{
            service.addTema(tema);
            assert(false);

        }catch (ValidationException ve){
            assert(true);

        }

    }

    @Test
    public void addTema_Invalid_primire_greaterThan14_ThrowsError() {

        String nrTema = "103";
        String descriere = "desc";
        int deadline = 12;
        int primire = 15;

        Tema tema = new Tema(nrTema, descriere, deadline, primire );

        try{
            service.addTema(tema);
            assert(false);

        }catch (ValidationException ve){
            assert(true);

        }

    }
}
