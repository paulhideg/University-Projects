package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.IExpression;
import model.programState.PrgState;
import model.type.IntType;
import model.type.StringType;
import model.type.Type;
import model.utils.MyDict;
import model.utils.MyIDict;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.Buffer;

public class ReadFileStmt implements IStmt {
    private final IExpression exp;

    private final String varName;

    public ReadFileStmt(IExpression exp, String varName) {
        this.exp = exp;
        this.varName = varName;
    }

    @Override
    public PrgState execute(PrgState state)throws ADTException, ExpressionEvalException, StatementExecException {
        MyIDict<String, Value> symTable = state.getSymTable();
        MyIDict<String, BufferedReader> fileTable = state.getFileTable();

        if (symTable.isDefined(varName)) {
            Value value = symTable.lookup(varName);
            if (value.getType().equals(new IntType())) {
                value = exp.eval(symTable, state.getHeap());
                if (value.getType().equals(new StringType())) {
                    StringValue castValue = (StringValue) value;
                    if (fileTable.isDefined(castValue.getValue())) {
                        BufferedReader br = fileTable.lookup(castValue.getValue());
                        try {
                            String line = br.readLine();
                            if (line == null)
                                line = "0";
                            symTable.put(varName, new IntValue(Integer.parseInt(line)));
                        } catch (IOException e) {
                            throw new StatementExecException(String.format("Could not read from file %s", castValue));
                        }
                    } else {
                        throw new StatementExecException(String.format("The file table does not contain %s", castValue));
                    }
                } else {
                    throw new StatementExecException(String.format("%s does not evaluate to StringType", value));
                }
            } else {
                throw new StatementExecException(String.format("%s is not of type IntType", value));
            }
        } else {
            throw new StatementExecException(String.format("%s is not present in the symTable.", varName));
        }
        return null;

    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        Type type = exp.typecheck(typeEnv);
        if (type.equals(new StringType())) {
            if (typeEnv.isDefined(varName)) {
                Type varType = typeEnv.lookup(varName);
                if (varType.equals(new IntType())) {
                    return typeEnv;
                } else {
                    throw new StatementExecException(String.format("%s is not of type IntType", varName));
                }
            } else {
                throw new StatementExecException(String.format("%s is not defined in the typeEnv", varName));
            }
        } else {
            throw new StatementExecException(String.format("%s does not evaluate to StringType", exp));
        }
    }

    @Override
    public IStmt deepCopy() {
        return new ReadFileStmt(exp.deepCopy(), varName);
    }

    @Override
    public String toString() {
        return String.format("readFile(%s, %s)", exp.toString(), varName);
    }

}



