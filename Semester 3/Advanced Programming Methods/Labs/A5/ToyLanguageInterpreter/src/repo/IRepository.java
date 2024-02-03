package repo;

import exceptions.ADTException;
import model.programState.PrgState;

import java.io.IOException;
import java.util.List;


public interface IRepository {
    List<PrgState> getPrgList();
    void setPrgList(List<PrgState> prgList);
    void addPrg(PrgState prg);

    void logPrgStateExec(PrgState prgState) throws IOException, ADTException;

}
