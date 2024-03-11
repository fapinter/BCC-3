import java.util.ArrayList;
public class Album {
    private String nome;
    private String genero;
    private int ano;
    private Pessoa artista;
    public ArrayList<Musica> musicas;

    public Album(String nome, String genero, int ano, Pessoa artista){
        this.nome = nome;
        this.genero = genero;
        this.ano = ano;
        this.artista = artista;
        this.musicas = new ArrayList<Musica>();
    }

    public void addMusica(String nome, int duracao){
       Musica m1 = new Musica(nome, duracao);
       this.musicas.add(m1);
    }
    public void mostrarTodosDados(){
        System.out.println("-------------------");
        System.out.println("Nome album: "+ this.nome);
        System.out.println("Genero album: "+ this.genero);
        System.out.println("Ano album: "+ this.ano);
        System.out.println("Nome artista: "+ this.artista.getNome());
        System.out.println("Idade artista: "+ this.artista.getIdade());
        System.out.println("Para mostrar as musicas escolha Mostrar Musicas");
        System.out.println("-------------------");
    }
}
