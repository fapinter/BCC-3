import java.util.Scanner;

public class Main {

    public static void main(String args[]){
        Boolean menu = true;
        Scanner scanner = new Scanner(System.in);
        Scanner scanner2 = new Scanner(System.in);

        Pessoa p1 = new Pessoa("Fabricio Pinterich", 19);
        Album a1 = new Album("Sem nome", "Rock", 2024, p1);


        while (menu == true){
            int opcao_menu = 0;
            System.out.println("*** MENU ***");
            System.out.println("(1) Add Musica");
            System.out.println("(2) Mostrar Musicas");
            System.out.println("(3) Mostrar Dados do Album");
            System.out.println("(9) Sair\n");
            System.out.print("Opção: ");
            opcao_menu = scanner.nextInt();

            switch (opcao_menu){
                case 1:
                    System.out.print("Digite o nome da música: ");
                    String nome = scanner2.nextLine();
                    System.out.print("Digite a duracao da musica: ");
                    int duracao = scanner.nextInt();
                    a1.addMusica(nome,duracao);
                    break;
                case 2:
                    for (int i = 0; i < a1.musicas.size(); i++){
                        System.out.println("Título: "+ a1.musicas.get(i).getNome());
                        System.out.println("Duracao da música: "+ a1.musicas.get(i).getDuracao());
                        System.out.println("--------------");
                    }
                    break;
                case 3:
                    a1.mostrarTodosDados();
                    break;
                case 9 :
                    menu = false;
                    System.out.println("Saindo...");
                    break;


            }

        }
    }
}
