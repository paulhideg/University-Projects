package model.programState;

import model.statements.IStmt;
import model.utils.MyIList;
import model.utils.MyIStack;
import model.utils.MyIDict;
import model.value.Value;
import model.utils.MyIHeap;

import java.io.BufferedReader;

public class PrgState {

    private MyIStack<IStmt> exeStack;
    private MyIDict<String, Value> symTable;
    private MyIList<Value> out;
    private MyIHeap heap;
    private MyIDict<String, BufferedReader> fileTable;
    private IStmt originalProgram;
    private int id;
    private static int idGenerator = 0;

    public PrgState(MyIStack<IStmt> exeStack, MyIDict<String, Value> symTable, MyIList<Value> out, IStmt originalProgram, MyIDict<String, BufferedReader> fileTable, MyIHeap heap) {
        this.exeStack = exeStack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap=heap;
        this.originalProgram = originalProgram.deepCopy();
        this.exeStack.push(originalProgram);
        this.id = generateId();
    }

    public PrgState(MyIStack<IStmt> stack, MyIDict<String, Value> symTable, MyIList<Value> out, MyIDict<String, BufferedReader> fileTable, MyIHeap heap) {
        this.exeStack = stack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap=heap;
        this.id = generateId();
    }


    public synchronized static int generateId(){
        return idGenerator++;
    }

    public MyIStack<IStmt> getExeStack() {
        return exeStack;
    }

    public MyIDict<String, Value> getSymTable() {
        return symTable;
    }

    public MyIList<Value> getOut() {
        return out;
    }

    public MyIHeap getHeap(){return heap;}

    public void setExeStack(MyIStack<IStmt> exeStack) {
        this.exeStack = exeStack;
    }

    public void setSymTable(MyIDict<String, Value> symTable) {
        this.symTable = symTable;
    }

    public void setOut(MyIList<Value> out) {
        this.out = out;
    }

    public void setHeap(MyIHeap heap) {this.heap = heap;}

    public void setFileTable(MyIDict<String, BufferedReader> fileTable) {
        this.fileTable = fileTable;
    }

    public MyIDict<String, BufferedReader> getFileTable() {
        return fileTable;
    }

    public boolean isNotCompleted() {
        return !exeStack.isEmpty();
    }

    public PrgState oneStep() throws Exception {
        if (exeStack.isEmpty())
            throw new Exception("PrgState stack is empty");
        IStmt crtStmt = exeStack.pop();
        return crtStmt.execute(this);
    }

    @Override
    public String toString() {
        return  "\nID: " + id +
                "\nExeStack\n" + exeStack + "\n" +
                "\nSymTable\n" + symTable + "\n" +
                "\nOut\n" + out + "\n" +
                "\nFileTable\n" + fileTable + "\n"+
                "\nHeap\n" + heap + "\n" +
                "\nOriginalProgram\n" + originalProgram + "\n------------------------------------------------------------------"
                ;
    }
}
