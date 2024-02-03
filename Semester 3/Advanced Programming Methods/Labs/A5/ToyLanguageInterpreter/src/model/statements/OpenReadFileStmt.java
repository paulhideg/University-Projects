package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.IExpression;
import model.programState.PrgState;
import model.type.StringType;
import model.type.Type;
import model.utils.MyIDict;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFileStmt implements IStmt {

    private final IExpression exp;

    public OpenReadFileStmt(IExpression exp) {
        this.exp = exp;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        Type type = exp.typecheck(typeEnv);
        if (type.equals(new StringType())) {
            return typeEnv;
        } else {
            throw new StatementExecException("OpenReadFileStmt: expression is not a string");
        }
    }

    @Override
    public PrgState execute(PrgState state) throws ADTException, ExpressionEvalException, StatementExecException {
        Value value = exp.eval(state.getSymTable(), state.getHeap());
        if (value.getType().equals(new StringType())) {
            StringValue filename = (StringValue) value;
            MyIDict<String, BufferedReader> fileTable = state.getFileTable();
            if (!fileTable.isDefined(filename.getValue())) {
                BufferedReader br;
                try {
                    br = new BufferedReader(new FileReader(filename.getValue()));
                } catch (FileNotFoundException e) {
                    throw new StatementExecException("File not found");
                }
                fileTable.put(filename.getValue(), br);
                state.setFileTable(fileTable);
            } else
                throw new StatementExecException("File already open");
        } else
            throw new StatementExecException("Expression is not a string");
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new OpenReadFileStmt(exp.deepCopy());
    }

    @Override
    public String toString() {
        return "openReadFile(" + exp.toString() + ")";
    }
}


