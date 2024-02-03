class Car {
    protected String Make;
    protected int Year;
    static int nrOfCars = 0;


    public Car() {
        Make = "";
        Year = 0;
    }
    public Car(String _Make, int _Year) {
        Make = _Make;
        Year = _Year;
    }

    public int getYear() {
        return Year;
    }

    public String getMake() {
        return Make;
    }

    public void setYear(int new_year) {
        if (new_year < 1850)
            throw new ArithmeticException("Invalid year!");
        Year = new_year;
    }

    public double computeMaxWeight() {
        return 0;
    }

    public int getNrWheels() {
        return 0;
    }

    public static int getNrOfCars() {
        return nrOfCars;
    }
}

class Truck extends Car {

    private int Wheels;

    public Truck(String _Make, int _Year, int _Wheels) {
        Make = _Make;
        Year = _Year;
        Wheels = _Wheels;
    }

    @Override
    public int getNrWheels() {
        return Wheels;
    }

    public void setWheels(int new_Wheels) {
        Wheels = new_Wheels;
    }

    @Override
    public double computeMaxWeight() {
        return 1.2 * Wheels; //tons
    }
}

public class MyClass {
    public static void main(String[] args) {
        System.out.println("We have " + Car.nrOfCars + " cars");
        Car c1 = new Car("Mercedes", 2020);
        Car c2 = new Car("Audi", 2015);
        Car c3 = new Car("Jeep", 2017);
        Car c4 = new Car("VW", 2018);
        Car c5 = new Car("Porsche", 2019);
        Car.nrOfCars += 5;

        System.out.println("We have " + Car.getNrOfCars() + " cars");
        System.out.println("First Car's make is " + c1.getMake());
        c1.setYear(2021);
        System.out.println("First Car year is " + c1.getYear() + " Max weight: " + c1.computeMaxWeight());

        Car trucky = new Truck("TIR", 1995, 8);
        Car.nrOfCars++;
        System.out.println("We have " + Car.nrOfCars + " cars");
        System.out.println("Truck " + trucky.getMake() + " with " + trucky.getNrWheels() + " wheels has max weight: " + trucky.computeMaxWeight());

        try {
            c1.setYear(1000);
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}