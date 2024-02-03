package Model.Statement;

import Exception.ToyLanguageInterpreterException;
import Model.State.ProgramState;

import java.io.FileNotFoundException;
import java.io.IOException;

public interface IStatement {
    ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException, FileNotFoundException, IOException;
    String toString();
}

