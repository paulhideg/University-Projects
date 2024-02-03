
public class Controller {
    IRepository repository;
    public Controller(IRepository repository) {
        this.repository = repository;
    }

    void addVehicle(IVehicle vehicle) throws ExceptionAdd {
        repository.addVehicle(vehicle);
    }

    void removeVehicle(String licencePlate) throws ExceptionRemove{
        repository.removeVehicle(licencePlate);
    }

    IVehicle[] getAll(){
        return repository.getAll();
    }

}
