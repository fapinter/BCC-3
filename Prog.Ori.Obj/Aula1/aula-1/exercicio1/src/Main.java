//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {


    public static void main(String[] args) {
        Gato gato1 = new Gato();

        gato1.cor = "laranja";
        gato1.nome= "Pringles";

        Cachorro cachorro1 = new Cachorro();

        cachorro1.nome = "Romario";

        System.out.println("o gato se chama "+ gato1.nome);
        System.out.println("o cachorro se chama "+ cachorro1.nome);



    }
}