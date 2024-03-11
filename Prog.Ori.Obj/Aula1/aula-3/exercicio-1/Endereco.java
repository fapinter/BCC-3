public class Endereco {
    int cep;
    String rua;
    int numero;

    public void setCep(int cep){
        this.cep = cep;
    }
    public int getCep(){
        return this.cep;
    }
    public void setRua(String rua){
        this.rua = rua;
    }
    public String getRua(){
        return this.rua;
    }
    public void setNumero(int numero){
        this.numero = numero;
    }
    public int getNumero(){
        return this.numero;
    }
    public Endereco(int cep, String rua, int numero){
        this.cep = cep;
        this.rua = rua;
        this.numero = numero;
    }
}
