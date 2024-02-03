package repo;

import exceptions.ADTException;
import model.programState.PrgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepository {
    private List<PrgState> prgList;
    private int currentPos;

    private final String logFilePath;

    public Repository(PrgState prg, String logFilePath) {
        this.logFilePath = logFilePath;
        this.prgList = new ArrayList<>();
        this.currentPos=0;
        this.addPrg(prg);
    }

    public int getCurrentPos() {
        return currentPos;
    }

    public void setCurrentPos(int currentPos) {
        this.currentPos = currentPos;
    }

    @Override
    public List<PrgState> getPrgList() {
        return prgList;
    }

    @Override
    public void setPrgList(List<PrgState> prgList) {
        this.prgList = prgList;
    }

    @Override
    public void addPrg(PrgState prg) {
        prgList.add(prg);
    }

    @Override
    public void logPrgStateExec(PrgState prgState) throws IOException, ADTException {
        PrintWriter logFile;
        logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        logFile.println(prgState.toString());
        logFile.close();
    }
}

