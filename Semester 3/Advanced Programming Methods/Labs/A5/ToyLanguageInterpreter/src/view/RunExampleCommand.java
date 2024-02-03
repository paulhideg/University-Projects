package view;

import controller.Controller;

public class RunExampleCommand extends Command{

    private final Controller controller;

    public RunExampleCommand(String key, String description, Controller controller) {
        super(key, description);
        this.controller = controller;
    }

    @Override
    public void execute() {
        try {
            controller.setDisplayFlag(false);
            controller.allStep();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
