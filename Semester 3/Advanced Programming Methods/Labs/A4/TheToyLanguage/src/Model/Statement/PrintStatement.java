package Model.Statement;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Collection.List.MyIList;
import Exception.ToyLanguageInterpreterException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Model.Value.Value;

public class PrintStatement implements IStatement{
    private final IExpression expression;

    public PrintStatement(IExpression expression){
        this.expression=expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException{

        MyIDictionary<String, Value> symbolTable = state.getSymbolTable();
        MyIHeap<Value> heapTable = state.getHeap();

        MyIList<Value> out = state.getOutputList();
        out.add(this.expression.evaluate(symbolTable, heapTable));
        state.setOutputList(out);
        return null;
    }

    @Override
    public String toString(){
        return String.format("Print(%s)", this.expression.toString());
    }
}
