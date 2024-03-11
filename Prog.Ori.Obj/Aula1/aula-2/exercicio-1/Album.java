public class Album {
    private String genero;
    private int ano;
    private String nome;
    private Pessoa artista;
    private Musica musica;

    public void setGenero(String genero){
        this.genero = genero;
    }
    public String getGenero(){
        return this.genero;
    }

    public void setAno(int ano){
        this.ano = ano;
    }
    public int getAno(){
        return this.ano;
    }

    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNome(){
        return this.nome;
    }

    public void setArtista(Pessoa artista){
        this.artista = artista;
    }

    public Pessoa getArtista(){
        return this.artista;
    }

    public void setMusica(Musica musica){
        this.musica = musica;
    }
    public Musica getMusica(){
        return this.musica;
    }

    public void mostraTodosOsDados(){
        System.out.println("Nome do Album:" + this.nome);
        System.out.println("Genero: "+ this.genero);
        System.out.println("Ano: " + this.ano);
        System.out.println("Nome artista: "+ this.artista.getNome());
        System.out.println("Idade artista: "+ this.artista.getIdade());
        System.out.println("Titulo musica: "+ this.musica.getTitulo());
        System.out.println("Duracao musica: "+ this.musica.getDuracao());
    }
}
