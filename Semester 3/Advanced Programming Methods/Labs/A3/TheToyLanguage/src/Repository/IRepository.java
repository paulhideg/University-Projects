package Repository;

import Exception.ToyLanguageInterpreterException;
import Model.State.ProgramState;

import java.io.IOException;

public interface IRepository {

    ProgramState getCurrentState();

    void addProgram(ProgramState program);

    void logPrgStateExec() throws IOException;
}
