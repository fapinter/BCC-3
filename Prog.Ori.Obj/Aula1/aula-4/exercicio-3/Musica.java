public class Musica {
    private String nome;
    private int duracao;

    public void setNome(String nome){
        this.nome = nome;
    }
    public void setDuracao(int duracao){
        this.duracao = duracao;
    }
    public String getNome(){
        return this.nome;
    }
    public int getDuracao(){
        return this.duracao;
    }
    public Musica(String nome, int duracao){
        this.setNome(nome);
        this.setDuracao(duracao);
    }

    public String tocarMusica(String nome){
        return "turururu";
    }
}
