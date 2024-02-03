package UserInterface;

import Controller.Controller;

import Exception.ToyLanguageInterpreterException;
import java.io.IOException;

public class RunExample extends Command{

    private final Controller service;

    public RunExample(String key, String desc, Controller service){
        super(key, desc);
        this.service = service;
    }

    @Override
    public void execute() {
        try{
            this.service.allSteps();
        } catch (ToyLanguageInterpreterException | IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
