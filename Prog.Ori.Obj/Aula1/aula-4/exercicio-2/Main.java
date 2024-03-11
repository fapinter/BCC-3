
import java.util.ArrayList;

public class Main {

    public static void main(String args[]){
        ArrayList <Filme> filmes = new ArrayList<Filme>();
        filmes.add(new Filme("Duna 2", "Ficção Cientifica", 2024));
        filmes.add(new Filme("Oppenheimer", "Documentario", 2023));
        filmes.add(new Filme("Barbie", "Comédia", 2023));
        filmes.add(new Filme("Uma nova espernça", "Ficção Cientifica", 1977));
        filmes.add(new Filme("Megamente ", "Animação", 2010));

        for (int i = 0; i < filmes.size(); i++){
            System.out.println("-----------------");
            System.out.println("Título: "+ filmes.get(i).getTitulo());
            System.out.println("Gênero: "+ filmes.get(i).getGenero());
            System.out.println("Ano de Lançamento: "+ filmes.get(i).getAnoLancamento());
        }
    }
}
