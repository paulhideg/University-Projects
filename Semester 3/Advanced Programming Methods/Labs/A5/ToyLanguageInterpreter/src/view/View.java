package view;

import controller.Controller;
import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.ArithmetciExpression;
import model.expressions.ValueExpression;
import model.expressions.VarExpression;
import model.programState.PrgState;
import model.statements.*;
import model.type.BooleanType;
import model.type.IntType;
import model.utils.*;
import model.value.BooleanValue;
import model.value.IntValue;
import model.value.Value;
import repo.IRepository;
import repo.Repository;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;

public class View {
    public void start(){
        boolean done = false;
        while(!done){
            try{
                printMenu();
                Scanner scanner = new Scanner(System.in);
                int option = scanner.nextInt();
                if(option==0)
                    done=true;
                else if(option==1){
                    runPrg1();
                }
                else if(option==2){
                    runPrg2();
                }
                else if(option==3){
                    runPrg3();
                }
                else{
                    System.out.println("Invalid option");
                }
            }catch (Exception e){
                System.out.println(e.getMessage());
            }
        }
    }

    private void printMenu(){
        System.out.println("MENU: ");
        System.out.println("0. Exit");
        System.out.println("1. Run program 1");
        System.out.println("2. Run program 2");
        System.out.println("3. Run program 3");
        System.out.println("Option: ");
    }

    private void runPrg1()throws StatementExecException, ExpressionEvalException, ADTException, IOException, InterruptedException {
        IStmt ex1= new CompoundStmt(new VarDeclStmt("v",new IntType()),
                new CompoundStmt(new AssignStmt("v",new ValueExpression(new IntValue(2))), new PrintStmt(new
                        VarExpression("v"))));
        runStmt(ex1);
    }

    private void runPrg2()throws StatementExecException, ExpressionEvalException, ADTException, IOException, InterruptedException {
        IStmt ex2 = new CompoundStmt( new VarDeclStmt("a",new IntType()),
                new CompoundStmt(new VarDeclStmt("b",new IntType()),
                        new CompoundStmt(new AssignStmt("a", new ArithmetciExpression('+',new ValueExpression(new IntValue(2)),new
                                ArithmetciExpression('*',new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5))))),
                                new CompoundStmt(new AssignStmt("b",new ArithmetciExpression('+',new VarExpression("a"), new ValueExpression(new
                                        IntValue(1)))), new PrintStmt(new VarExpression("b"))))));
        runStmt(ex2);
    }

    private void runPrg3()throws StatementExecException, ExpressionEvalException, ADTException, IOException, InterruptedException {
        IStmt ex3 = new CompoundStmt(new VarDeclStmt("a",new BooleanType()),
                new CompoundStmt(new VarDeclStmt("v", new IntType()),
                        new CompoundStmt(new AssignStmt("a", new ValueExpression(new BooleanValue(true))),
                                new CompoundStmt(new IfStmt(new VarExpression("a"),new AssignStmt("v",new ValueExpression(new
                                        IntValue(2))), new AssignStmt("v", new ValueExpression(new IntValue(3)))), new PrintStmt(new
                                        VarExpression("v"))))));
        runStmt(ex3);
    }

    private void runStmt(IStmt stmt)throws ADTException, ExpressionEvalException, StatementExecException, IOException, InterruptedException {
        MyIStack<IStmt> exeStack = new MyStack<>();
        MyIDict<String, Value> symTable = new MyDict<>();
        MyIList<Value> out = new MyList<>();
        MyIDict<String, BufferedReader> fileTable = new MyDict<>();
        MyIHeap heap = new MyHeap();

        PrgState prg = new PrgState(exeStack, symTable, out, stmt, fileTable, heap);

        IRepository repo=new Repository(prg, "log.txt");
        Controller ctrl=new Controller(repo);

        System.out.println("Do you want to display the steps? (y/n)");
        Scanner scanner = new Scanner(System.in);
        String option = scanner.nextLine();
        ctrl.setDisplayFlag(option.equals("y"));

        ctrl.allStep();
        System.out.println("Result: "+prg.getOut().toString());
    }
}
