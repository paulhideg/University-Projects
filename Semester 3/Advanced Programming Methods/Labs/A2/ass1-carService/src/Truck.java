class Truck extends Vehicle {

    public Truck(int repairPrice, String licencePlate) {
        super(repairPrice, licencePlate);
    }

    @Override
    public String toString() {
        return "Truck{" +
                "repairPrice=" + repairPrice +
                ", licencePlate='" + licencePlate + '\'' +
                '}';
    }
}