public class Cartao {
    int nroCartao;
    int codigo;

    String validade;

    public int getNroCartao(){
        return this.nroCartao;
    }
    public int getCodigo(){
        return this.codigo;
    }
    public String getValidade(){
        return this.validade;
    }
    public Cartao(int nroCartao, int codigo, String validade){
        this.nroCartao = nroCartao;
        this.codigo = codigo;
        this.validade = validade;
    }

}
