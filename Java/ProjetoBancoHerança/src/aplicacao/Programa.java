
import entidades.*;

public class Programa {

    public static void main(String[] args) {
        

    Conta acc = new Conta(1001, "Alex", 0.0);
    Empresa eacc = new Empresa(1002, "Maria", 0.0, 500.0);

    // UPCASTING

    Conta acc1 = eacc;
    Conta acc2 = new Empresa(1003, "Bob", 0.0, 200.0);
    Conta acc3 = new ContaPoupanca(1004, "Anna", 0.0, 0.01);

    // DOWNCASTING
    
    Empresa acc4 = (Empresa)acc2;
    acc4.emprestimo(100.0);

    if (acc3 instanceof Empresa) {
        Empresa acc5 = (Empresa)acc3;
        acc5.emprestimo(200.0);
        System.out.println("Emprestimo");
    }
    if (acc3 instanceof ContaPoupanca) {
        ContaPoupanca acc5 = (ContaPoupanca)acc3;
        acc5.alterarSaldo();
        System.out.println("Alterado");
    }
}


}
