import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        Pessoa p1 = new Pessoa();

        System.out.print("Digite um nome: ");
        p1.setNome(scanner.nextLine());

        System.out.print("Digite um numero: ");
        p1.setIdade(scanner.nextInt());

        Musica m1 = new Musica();
        m1.setTitulo("Dont go away");
        m1.setDuracao(3);

        Album a1 = new Album();
        a1.setGenero("Rock");
        a1.setNome("Sem nome");
        a1.setAno(2023);
        a1.setArtista(p1);
        a1.setMusica(m1);

        a1.mostraTodosOsDados();
    }

}
