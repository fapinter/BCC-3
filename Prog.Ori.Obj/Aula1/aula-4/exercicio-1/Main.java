import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Scanner;
import java.util.Collections;
public class Main {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        Boolean menu = true;
        ArrayList <String> pessoas = new ArrayList <String>();
        pessoas.add("Contin");
        pessoas.add("Simini");
        pessoas.add("Gris");
        pessoas.add("Falks");
        pessoas.add("Josvaldo");

        while (menu == true){
            int opcao_menu = 0;
            System.out.println("*** MENU ***");
            System.out.println("(1) Imprimir em ordenado");
            System.out.println("(2) Imprimir não ordenado");
            System.out.println("(9) Sair\n");
            System.out.print("Opcão: ");
            opcao_menu = scanner.nextInt();
            switch (opcao_menu){
                case 1:
                    ArrayList <String> PessoasOrdenadas = new ArrayList<String>(pessoas);
                    Collections.sort(PessoasOrdenadas);

                    for (int i = 0; i < PessoasOrdenadas.size(); i++) {
                        System.out.println("Indice [" + i + "] = " + PessoasOrdenadas.get(i));
                    }
                    break;
                case 2:
                    for (int i = 0; i < pessoas.size(); i++) {
                        System.out.println("Indice [" + i + "] = " + pessoas.get(i));
                    }
                    break;
                case 9:
                    menu = false;
                    System.out.println("Saindo...");
                    break;
                default:
                    continue;
            }
        }
    }
}
