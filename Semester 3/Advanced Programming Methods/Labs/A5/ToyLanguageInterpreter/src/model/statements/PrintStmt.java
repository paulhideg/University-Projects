package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import model.expressions.IExpression;
import model.programState.PrgState;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIList;
import model.value.Value;

public class PrintStmt implements IStmt{

    IExpression exp;

    public PrintStmt(IExpression exp){
        this.exp = exp;
    }

    @Override
    public String toString(){
        return "print(" + exp.toString() + ")";
    }

    @Override
    public IStmt deepCopy() {
        return new PrintStmt(exp.deepCopy());
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws ExpressionEvalException, ADTException {
        exp.typecheck(typeEnv);
        return typeEnv;
    }


    @Override
    public PrgState execute(PrgState state) throws ADTException, ExpressionEvalException {
        MyIList<Value> out = state.getOut();
        out.add(exp.eval(state.getSymTable(),state.getHeap()));
        state.setOut(out);
        return null;
    }
}
