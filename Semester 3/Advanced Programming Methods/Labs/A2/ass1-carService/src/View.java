import java.util.Scanner;

public class View {
    static String chooseVehicleType = "Choose the type of the vehicle:\n 1. Car\n 2. Motorcycle\n 3. Truck\n";
       static IRepository repo ;
        static Controller ctrl;

    public static void main(String[] args) throws ExceptionAdd {

         repo = new Repository(3);
         ctrl = new Controller(repo);

        init();
        start();
    }

    static void start()  {
        while(true) {
            System.out.println("1. Add vehicle\n2. Show repair price > 1000\n3. Remove vehicle \n4. Exit");

            Scanner in = new Scanner(System.in);
            int input = Integer.parseInt(in.nextLine());

            if (input == 1) {
                addVehicle();
            } else if (input == 2) {
                print();
            } else if (input == 3){
                removeVehicle();
            } else if (input == 4) {
                break;
            } else {
                System.out.println("(start) Index out of range!");
            }
        }
    }

    static void init() throws ExceptionAdd {
        Car c = new Car(1500, "a");
        ctrl.addVehicle(c);

        Truck t = new Truck(1200, "b");
        ctrl.addVehicle(t);

        Motorcycle m = new Motorcycle(100, "c");
        ctrl.addVehicle(m);
    }

    static void addVehicle() {

        System.out.println(chooseVehicleType);

        Scanner in = new Scanner(System.in);
        int type = Integer.parseInt(in.nextLine());

        System.out.println("Licence plate: ");
        String licencePlate = in.nextLine();

        System.out.println("Repair price: ");
        int price = Integer.parseInt(in.nextLine());

        try {
            if (type == 1) {
                ctrl.addVehicle(new Car(price, licencePlate));
            }
            else if (type == 2){
                ctrl.addVehicle(new Motorcycle(price, licencePlate));
            }
            else if (type == 3){
                ctrl.addVehicle(new Truck(price, licencePlate));
            }
            else{
                System.out.println("(add) Index out of range.");
            }
        }
        catch (ExceptionAdd ex){
            System.out.println(ex.getMessage());
        }
    }

    static void removeVehicle(){

        Scanner in = new Scanner(System.in);

        System.out.println("Licence plate: ");
        String licencePlate = in.nextLine();

        try {
            ctrl.removeVehicle(licencePlate);
        }
        catch (ExceptionRemove ex){
            System.out.println(ex.getMessage());
        }

    }

    static void print(){
        for (IVehicle vehicle : ctrl.getAll()) {
            if (vehicle.getRepairPrice() > 1000) {
                System.out.println(vehicle);
            }
        }
    }
}
