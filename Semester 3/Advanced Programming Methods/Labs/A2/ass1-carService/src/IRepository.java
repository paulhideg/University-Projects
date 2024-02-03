
public interface IRepository {
    void addVehicle(IVehicle v) throws ExceptionAdd;

    void removeVehicle(String licencePlate) throws ExceptionRemove;
    IVehicle[] getAll();
}
