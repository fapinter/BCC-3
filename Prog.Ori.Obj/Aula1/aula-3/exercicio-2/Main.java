import java.util.Scanner;


/* CORRIGIR, INTERFACE GRAFICA EM UMA CLASS MAIN, MESMA LOGICA MAS EM OUTRA CLASSE*/
public class Main {


    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        Boolean menu = true;

        Area a1 = new Area(10,20);
        Area a2 = new Area("10", "20");

        while (menu == true){
            int opcao_menu = 0;
            System.out.println("*** MENU ***");
            System.out.println("(1) Area Quadrado: ");
            System.out.println("(2) Area Triangulo: ");
            System.out.println("(9) Sair: ");
            opcao_menu = scanner.nextInt();
            if (opcao_menu == 1) {

                System.out.println(a1.areaQuadrado(a1.base, a1.altura));
                System.out.println(a2.areaQuadrado(a2.base, a2.altura));
            }
            else if (opcao_menu == 2) {

                System.out.println(a1.areaTriangulo(a1.base, a1.altura));
                System.out.println(a2.areaTriangulo(a2.base, a2.altura));
            }
            else if(opcao_menu == 9) {
                System.out.println("Saindo...");
                menu = false;
            }
            else{
                continue;
            }

        }




    }
}
