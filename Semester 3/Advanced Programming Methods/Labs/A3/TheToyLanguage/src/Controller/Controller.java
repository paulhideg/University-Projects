package Controller;

import Collection.Stack.MyIStack;
import Exception.ToyLanguageInterpreterException;
import Model.State.ProgramState;
import Model.Statement.IStatement;
import Repository.IRepository;

import java.io.IOException;

public class Controller {

    private final IRepository repo;
    public Controller(IRepository repo){
        this.repo = repo;
    }
    public ProgramState oneStep(ProgramState state) throws ToyLanguageInterpreterException, IOException {

        MyIStack<IStatement> stack = state.getExecutionStack();

        if (stack.isEmpty())
            throw new ToyLanguageInterpreterException("Program state stack is empty.");

        IStatement currentStatement = stack.pop();
        state.setExecutionStack(stack);
        return currentStatement.execute(state);

    }

    public void addProgram(ProgramState state){
        this.repo.addProgram(state);
    }

    public void allSteps() throws ToyLanguageInterpreterException, IOException {

        ProgramState program = this.repo.getCurrentState();
        //this.display();
        this.repo.logPrgStateExec();

        while(!program.getExecutionStack().isEmpty())
        {
            this.oneStep(program);
            //this.display();
            this.repo.logPrgStateExec();
        }
    }

    private void display(){
        System.out.println(this.repo.getCurrentState().toString());
        ProgramState program = this.repo.getCurrentState();

        if (program.getExecutionStack().size() == 0)
            System.out.println(this.repo.getCurrentState().toString());
    }
}
