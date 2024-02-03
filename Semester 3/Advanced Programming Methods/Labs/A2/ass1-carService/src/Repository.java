import java.util.Objects;

public class Repository implements IRepository {
    //IRepository repo = r;
    private final IVehicle[] vehicles;
    private int i;
    private final int dimension;
    public Repository(int dim) {
        this.vehicles = new IVehicle[dim];
        i = 0;
        dimension = dim;
    }

    @Override
    public void addVehicle(IVehicle v) throws ExceptionAdd {

        if(i<dimension) {
            //if(i!=0) {
                for (int j=0; j<i; j++) {
                    if (Objects.equals(vehicles[j].getLicencePlate(), v.getLicencePlate())) {
                        throw new ExceptionAdd("A vehicle with this licence plate already exists!");
                    }
                }
            //}
            System.out.println("1");
            vehicles[i] = v;
            i++;
        }
        else{
                throw new ExceptionAdd("Can not add object! List is full!");
        }
    }

    @Override
    public void removeVehicle(String licencePlate) throws ExceptionRemove {
        if(i==0) {
            throw new ExceptionRemove("List is empty!");
        }
        else {
            for (int j=0; j<i; j++) {
                if (Objects.equals(vehicles[j].getLicencePlate(), licencePlate)){
                    for (int k=j; k < i - 1; k++) {
                        vehicles[k] = vehicles[k + 1];
                    }
                    i--;
                    throw new ExceptionRemove("Vehicle removed!");
                }
                throw new ExceptionRemove("Item not found!");
            }
        }
    }

    @Override
    public IVehicle[] getAll() {
        IVehicle[] copyVehicles = new IVehicle[i];
        System.arraycopy(vehicles, 0, copyVehicles, 0, i);
        return copyVehicles;
    }

}
