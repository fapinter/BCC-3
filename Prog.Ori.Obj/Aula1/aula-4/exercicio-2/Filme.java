public class Filme {
     String titulo;
     String genero;
     int anoLancamento;

     public Filme (String titulo, String genero, int anoLancamento){
         this.titulo = titulo;
         this.genero = genero;
         this.anoLancamento = anoLancamento;

     }

     public String getTitulo(){
         return this.titulo;
     }
     public String getGenero(){
         return this.genero;
     }
     public int getAnoLancamento(){
         return this.anoLancamento;
     }

}
