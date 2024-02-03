package view;

import controller.Controller;
import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.*;
import model.programState.PrgState;
import model.statements.*;
import model.type.BooleanType;
import model.type.IntType;
import model.type.RefType;
import model.type.StringType;
import model.utils.MyHeap;
import model.value.RefValue;
import model.value.StringValue;
import model.utils.MyDict;
import model.utils.MyList;
import model.utils.MyStack;
import model.value.BooleanValue;
import model.value.IntValue;
import repo.IRepository;
import repo.Repository;

public class Interpreter {
    public static void main(String[] args) {

        TextMenu menu = new TextMenu();

        IStmt ex1= new CompoundStmt(new VarDeclStmt("v",new IntType()),
                new CompoundStmt(new AssignStmt("v",new ValueExpression(new IntValue(2))), new PrintStmt(new
                        VarExpression("v"))));
        try {
            ex1.typecheck(new MyDict<>());
            PrgState prg1 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex1, new MyDict<>(), new MyHeap());
            IRepository repo1 = new Repository(prg1, "log1.txt");
            Controller controller1 = new Controller(repo1);
            menu.addCommand(new RunExampleCommand("1", ex1.toString(), controller1));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        IStmt ex2 = new CompoundStmt( new VarDeclStmt("a",new IntType()),
                new CompoundStmt(new VarDeclStmt("b",new IntType()),
                        new CompoundStmt(new AssignStmt("a", new ArithmetciExpression('+',new ValueExpression(new IntValue(2)),new
                                ArithmetciExpression('*',new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5))))),
                                new CompoundStmt(new AssignStmt("b",new ArithmetciExpression('+',new VarExpression("a"), new ValueExpression(new
                                        IntValue(1)))), new PrintStmt(new VarExpression("b"))))));
       try {
           ex2.typecheck(new MyDict<>());
           PrgState prg2 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex2, new MyDict<>(), new MyHeap());
           IRepository repo2 = new Repository(prg2, "log2.txt");
           Controller controller2 = new Controller(repo2);
           menu.addCommand(new RunExampleCommand("2", ex2.toString(), controller2));
       } catch (Exception e) {
           System.out.println(e.getMessage());}


        IStmt ex3 = new CompoundStmt(new VarDeclStmt("a",new StringType()),
                new CompoundStmt(new VarDeclStmt("v", new IntType()),
                        new CompoundStmt(new AssignStmt("a", new ValueExpression(new IntValue(2))),
                                new CompoundStmt(new IfStmt(new VarExpression("a"),new AssignStmt("v",new ValueExpression(new
                                        IntValue(2))), new AssignStmt("v", new ValueExpression(new IntValue(3)))), new PrintStmt(new
                                        VarExpression("v"))))));
        try {
            ex3.typecheck(new MyDict<>());
            PrgState prg3 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex3, new MyDict<>(), new MyHeap());
            IRepository repo3 = new Repository(prg3, "log3.txt");
            Controller controller3 = new Controller(repo3);
            menu.addCommand(new RunExampleCommand("3", ex3.toString(), controller3));
        } catch (StatementExecException | ExpressionEvalException | ADTException e) {
            System.out.println(e.getMessage());
        }

        IStmt ex4 = new CompoundStmt(new VarDeclStmt("varf", new StringType()),
                new CompoundStmt(new AssignStmt("varf", new ValueExpression(new StringValue("test.in"))),
                        new CompoundStmt(new OpenReadFileStmt(new VarExpression("varf")),
                                new CompoundStmt(new VarDeclStmt("varc", new IntType()),
                                        new CompoundStmt(new ReadFileStmt(new VarExpression("varf"), "varc"),
                                                new CompoundStmt(new PrintStmt(new VarExpression("varc")),
                                                        new CompoundStmt(new ReadFileStmt(new VarExpression("varf"), "varc"),
                                                                new CompoundStmt(new PrintStmt(new VarExpression("varc")),
                                                                        new CloseReadFileStmt(new VarExpression("varf"))))))))));
        try {
            ex4.typecheck(new MyDict<>());
            PrgState prg4 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex4, new MyDict<>(), new MyHeap());
            IRepository repo4 = new Repository(prg4, "log4.txt");
            Controller controller4 = new Controller(repo4);
            menu.addCommand(new RunExampleCommand("4", ex4.toString(), controller4));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        IStmt ex5 = new CompoundStmt(new VarDeclStmt("v", new IntType()),
                new CompoundStmt(new AssignStmt("v", new ValueExpression(new IntValue(10))),
                        new CompoundStmt(new NewStmt("v", new ValueExpression(new IntValue(20))),
                                new CompoundStmt(new NewStmt("a", new ValueExpression(new IntValue(22))),
                                        new CompoundStmt(new PrintStmt(new VarExpression("v")),
                                                new PrintStmt(new ArithmetciExpression('+', new ValueExpression(new IntValue(100)), new
                                                        ReadHeapExpression(new VarExpression("v")))))))));
        try {
            ex5.typecheck(new MyDict<>());
            PrgState prg5 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex5, new MyDict<>(), new MyHeap());
            IRepository repo5 = new Repository(prg5, "log5.txt");
            Controller controller5 = new Controller(repo5);
            menu.addCommand(new RunExampleCommand("5", ex5.toString(), controller5));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        IStmt ex6 = new CompoundStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompoundStmt(new NewStmt("v", new ValueExpression(new IntValue(20))),
                        new CompoundStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompoundStmt(new NewStmt("a", new VarExpression("v")),
                                        new CompoundStmt(new PrintStmt(new VarExpression("v")), new PrintStmt(new VarExpression("a")))))));
        try {
            ex6.typecheck(new MyDict<>());
            PrgState prg6 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex6, new MyDict<>(), new MyHeap());
            IRepository repo6 = new Repository(prg6, "log6.txt");
            Controller controller6 = new Controller(repo6);
            menu.addCommand(new RunExampleCommand("6", ex6.toString(), controller6));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        IStmt ex7 = new CompoundStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompoundStmt(new NewStmt("v", new ValueExpression(new IntValue(20))),
                        new CompoundStmt(new PrintStmt(new ReadHeapExpression(new VarExpression("v"))),
                                new CompoundStmt(new WriteHeapStmt("v", new ValueExpression(new IntValue(30))),
                                        new PrintStmt(new ArithmetciExpression('+', new ReadHeapExpression(new VarExpression("v")), new
                                                ValueExpression(new IntValue(5))))))));
        try {
            ex7.typecheck(new MyDict<>());
            PrgState prg7 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex7, new MyDict<>(), new MyHeap());
            IRepository repo7 = new Repository(prg7, "log7.txt");
            Controller controller7 = new Controller(repo7);
            menu.addCommand(new RunExampleCommand("7", ex7.toString(), controller7));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        IStmt ex8 = new CompoundStmt(new VarDeclStmt("v", new IntType()),
                new CompoundStmt(new AssignStmt("v", new ValueExpression(new IntValue(4))),
                        new CompoundStmt(new WhileStmt(new RelationalExpression(">", new VarExpression("v"), new ValueExpression(new IntValue(0))),
                                new CompoundStmt(new PrintStmt(new VarExpression("v")),
                                        new AssignStmt("v", new ArithmetciExpression('-', new VarExpression("v"), new ValueExpression(new IntValue(1)))))),
                                new PrintStmt(new VarExpression("v")))));
        try {
            ex8.typecheck(new MyDict<>());
            PrgState prg8 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex8, new MyDict<>(), new MyHeap());
            IRepository repo8 = new Repository(prg8, "log8.txt");
            Controller controller8 = new Controller(repo8);
            menu.addCommand(new RunExampleCommand("8", ex8.toString(), controller8));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        IStmt ex9 = new CompoundStmt(new VarDeclStmt("v", new IntType()),
                new CompoundStmt(new  VarDeclStmt("a", new RefType(new IntType())),
                        new CompoundStmt(new AssignStmt("v", new ValueExpression(new IntValue(10))),
                                new CompoundStmt(new NewStmt("a", new ValueExpression(new IntValue(22))),
                                        new CompoundStmt(new ForkStmt(new CompoundStmt(new WriteHeapStmt("a", new ValueExpression(new IntValue(30))),
                                                new CompoundStmt(new AssignStmt("v", new ValueExpression(new IntValue(32))),
                                                        new CompoundStmt(new PrintStmt(new VarExpression("v")), new PrintStmt(new ReadHeapExpression(new VarExpression("a"))))))),
                                                new CompoundStmt(new PrintStmt(new VarExpression("v")), new PrintStmt(new ReadHeapExpression(new VarExpression("a")))))))));
        try {
            ex9.typecheck(new MyDict<>());
            PrgState prg9 = new PrgState(new MyStack<>(), new MyDict<>(), new MyList<>(), ex9, new MyDict<>(), new MyHeap());
            IRepository repo9 = new Repository(prg9, "log9.txt");
            Controller controller9 = new Controller(repo9);
            menu.addCommand(new RunExampleCommand("9", ex9.toString(), controller9));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }



        menu.addCommand(new ExitCommand("0", "exit"));
        menu.show();
    }
}
