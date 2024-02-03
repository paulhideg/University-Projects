class Motorcycle extends Vehicle {

    public Motorcycle(int repairPrice, String licencePlate) {
        super(repairPrice, licencePlate);
    }

    public int getRepairPrice(){
        return repairPrice;
    }

    @Override
    public String toString() {
        return "Motorcycle{" +
                "repairPrice=" + repairPrice +
                ", licencePlate='" + licencePlate + '\'' +
                '}';
    }
}