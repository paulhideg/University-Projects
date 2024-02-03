class Vehicle implements IVehicle {
    int repairPrice;
    String licencePlate;

    public Vehicle(int repairPrice, String licencePlate) {
        this.repairPrice = repairPrice;
        this.licencePlate = licencePlate;
    }
    @Override
    public int getRepairPrice() {
        return repairPrice;
    }

    @Override
    public String getLicencePlate(){
        return licencePlate;
    }
}