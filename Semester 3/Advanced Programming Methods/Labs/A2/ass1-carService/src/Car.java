class Car extends Vehicle {

    public Car(int repairPrice, String licencePlate) {
        super(repairPrice, licencePlate);
    }

    @Override
    public String toString() {
        return "Car{" +
                "repairPrice=" + repairPrice +
                ", licencePlate='" + licencePlate + '\'' +
                '}';
    }
}