package controller;

import model.programState.PrgState;
import model.statements.IStmt;
import model.value.RefValue;
import model.value.Value;
import repo.IRepository;
import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.utils.MyIStack;

import java.io.IOException;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Controller {

    IRepository repo;
    boolean displayFlag=false;
    ExecutorService executor;

    public Controller(IRepository repo) {
        this.repo = repo;
    }

    public void setDisplayFlag(boolean displayFlag) {
        this.displayFlag = displayFlag;
    }

    public List<Integer> getAddrFromSymTable(Collection<Value> symTableValues) {
        return symTableValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    public List<Integer> getAddrFromHeap(Collection<Value> heapValues) {
        return heapValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    public Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddr, List<Integer> heapAddr, Map<Integer, Value> heap) {
        return heap.entrySet().stream()
                .filter(e -> ( symTableAddr.contains(e.getKey()) || heapAddr.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public void oneStepForAllPrograms(List<PrgState> states) throws ADTException, StatementExecException, ExpressionEvalException, IOException, InterruptedException {
        states.forEach(prg-> {
            try {
                repo.logPrgStateExec(prg);
                display(prg);
            } catch (IOException | ADTException e) {
                System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
            }
        });

        List<Callable<PrgState>> callList = states.stream()
                .map((PrgState p) -> (Callable<PrgState>)(p::oneStep))
                .collect(Collectors.toList());

        List<PrgState> newPrgList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (Exception e) {
                        System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
                    }
                    return null;
                })
                .filter(Objects::nonNull)
                .collect(Collectors.toList());

        states.addAll(newPrgList);

        states.forEach(prg -> {
            try {
                repo.logPrgStateExec(prg);
            } catch (IOException | ADTException e) {
                System.out.println("\u001B[31m" + e.getMessage() + "\u001B[0m");
            }
        });

        repo.setPrgList(states);
    }

    public void allStep() throws ADTException, StatementExecException, ExpressionEvalException, IOException, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        List<PrgState> prgList = removeCompletedPrg(repo.getPrgList());
        while (prgList.size() > 0) {
            conservativeGarbageCollector(prgList);
            oneStepForAllPrograms(prgList);
            prgList = removeCompletedPrg(repo.getPrgList());
        }
        executor.shutdownNow();
        repo.setPrgList(prgList);
    }

    public void conservativeGarbageCollector(List<PrgState> prgList) {
        List<Integer> symTableAddresses = Objects.requireNonNull(prgList.stream()
                        .map(p -> getAddrFromSymTable(p.getSymTable().values()))
                        .map(Collection::stream)
                        .reduce(Stream::concat).orElse(null))
                .collect(Collectors.toList());
        prgList.forEach(p -> {
            p.getHeap().setContent((HashMap<Integer, Value>) safeGarbageCollector(symTableAddresses, getAddrFromHeap(p.getHeap().getContent().values()), p.getHeap().getContent()));
        });
    }

    private void display(PrgState state) {
        if(displayFlag){
            System.out.println(state.toString());
        }
    }

    public List<PrgState> removeCompletedPrg(List<PrgState> inPrgList) {
        return inPrgList.stream()
                .filter(PrgState::isNotCompleted)
                .collect(Collectors.toList());
    }

}
