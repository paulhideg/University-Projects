package ssvv.example;

import exam.Animals;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertThrows;

public class AnimalsTest extends TestCase {

    private Animals a = new Animals();

    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AnimalsTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AnimalsTest.class );
    }

    /**
     * Rigourous Test :-)
     */


    // black-box testing for FindPair method
    public void testFindPair1() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 2, 3));
        assertEquals(Arrays.asList(0, 1), a.findPair(animals, 0));
    }

    public void testFindPair2() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(3, 2, 1));
        List<Integer> pair =  a.findPair(animals, 1);
        int firstAnimal = pair.get(0);
        int secondAnimal = pair.get(1);
        assertEquals(firstAnimal, 1);
        assertEquals(secondAnimal, 2);
    }

    public void testFindPair3() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 3, 3, 1));
        assertNull(a.findPair(animals, 0));
    }

    public void testFindPair4() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 1, 2, 2, 3, 3));
        assertEquals(Arrays.asList(3, 4), a.findPair(animals, 2));
    }

    public void testFindPair5() {
        List<Integer> animals = new ArrayList<>();
        assertEquals(null, a.findPair(animals, 1));
    }

    public void testFindPair6() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 2, 4));
        assertEquals(null, a.findPair(animals, 6));
    }


    // white-box testing for InsertCow method
    public void testInsertCow1() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 1, 2));
        assertThrows(IllegalArgumentException.class, () -> a.insertCow(animals, -5));
    }

    public void testInsertCow2() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 2, 3));
        try {
            a.insertCow(animals, 5);
        } catch (IllegalArgumentException e) {
            assertEquals("Index out of bounds", e.getMessage());
        }
    }

    public void testInsertCow3() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 2, 3));
        assertEquals(animals.size(), 3);
        a.insertCow(animals, 1);
        assertEquals(animals.size(), 4);
        assertEquals(Arrays.asList(1, 2, 4, 3), animals);
    }

    // integration testing for BeFriends method
    public void testBeFriends1() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 2, 3, 2, 1, 3));
        assertEquals(Arrays.asList(1, 4, 2, 4, 3, 4, 2, 4, 1, 3), a.beFriends(animals));
    }

    public void testBeFriends2() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 3, 1, 2));
        assertEquals(Arrays.asList(1, 3, 1, 4, 2), a.beFriends(animals));
    }

    public void testBeFriends3() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(3, 2, 1, 2, 3, 2));
        assertEquals(Arrays.asList(3, 4, 2, 4, 1, 4, 2, 4, 3, 4, 2), a.beFriends(animals));
    }

    public void testBeFriends4() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(4, 4, 4, 4));
        assertEquals(Arrays.asList(4, 4, 4, 4), a.beFriends(animals));
    }

    public void testBeFriends5() {
        List<Integer> animals = new ArrayList<>();
        assertEquals(a.beFriends(animals).size(), 0);
    }

    public void testBeFriends6() {
        List<Integer> animals = new ArrayList<>(Arrays.asList(1, 2));
        assertEquals(Arrays.asList(1, 4, 2), a.beFriends(animals));
    }
}
