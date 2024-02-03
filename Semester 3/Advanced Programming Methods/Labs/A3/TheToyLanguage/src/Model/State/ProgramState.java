package Model.State;

import Collection.Dictionary.MyDictionary;
import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyHeap;
import Collection.Heap.MyIHeap;
import Collection.List.MyIList;
import Collection.List.MyList;
import Collection.Stack.MyIStack;
import Collection.Stack.MyStack;
import Model.Statement.IStatement;
import Model.Value.Value;

import java.io.BufferedReader;

public class ProgramState {
    private MyIStack<IStatement> executionStack;
    private MyIDictionary<String, Value> symbolTable;
    private MyIList<Value> outputList;

    private MyIDictionary<String, BufferedReader> fileTable;

    private MyIHeap<Value> heap;

    private final IStatement originalProgram;

    public ProgramState(MyIStack<IStatement> programStateMyStack, MyIDictionary<String, Value> symbolTable,
                        MyIList<Value> outputList, IStatement originalProgram, MyIHeap<Value> heap,
                        MyIDictionary<String, BufferedReader> fileTable){

        this.executionStack = programStateMyStack;
        this.symbolTable = symbolTable;
        this.outputList = outputList;
        this.originalProgram = originalProgram;
        //this.executionStack.push(originalProgram);
        this.heap = heap;
        this.fileTable = fileTable;
    }

    public ProgramState(IStatement originalProgram){

        this.executionStack = new MyStack<>();
        this.symbolTable = new MyDictionary<>();
        this.outputList = new MyList<Value>();
        this.fileTable = new MyDictionary<String, BufferedReader>();
        this.heap = new MyHeap<>();
        this.originalProgram = originalProgram;
        this.executionStack.push(originalProgram);
    }

    public MyIStack<IStatement> getExecutionStack(){
        return this.executionStack;
    }

    public void setExecutionStack(MyIStack<IStatement> executionStack){
        this.executionStack = executionStack;
    }

    public MyIDictionary<String, Value> getSymbolTable(){
        return this.symbolTable;
    }

    public void setSymbolTable(MyIDictionary<String, Value> symbolTable){
        this.symbolTable = symbolTable;
    }

    public MyIList<Value> getOutputList() {
        return this.outputList;
    }

    public void setOutputList(MyIList<Value> outputList) {
        this.outputList = outputList;
    }

    public MyIHeap<Value> getHeap() {
        return this.heap;
    }

    public void setHeap(MyIHeap<Value> heap) {
        this.heap = heap;
    }

    public MyIDictionary<String, BufferedReader> getFileTable() {
        return this.fileTable;
    }


    public void setFileTable(MyIDictionary<String, BufferedReader> fileTable){
        this.fileTable = fileTable;
    }

    @Override
    public String toString() {
        return
                "--------------------------------------------------------\n" +
                "Output List:\n" + this.outputList.toString() + "\n" +
                "Symbol Table:\n" + this.symbolTable.toString() + "\n" +
                "Execution Stack:\n" + this.executionStack.toString() + "\n" +
                "File table:\n" + this.fileTable.toString() + "\n" +
                "--------------------------------------------------------\n";
    }


}
