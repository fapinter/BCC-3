public class ContaBancaria {
    int nroConta;
    String agencia;
    Cartao cartao;
    Pessoa cliente;

    public ContaBancaria(int nroConta, String agencia, Cartao cartao, Pessoa cliente){
        this.nroConta = nroConta;
        this.agencia = agencia;
        this.cartao = cartao;
        this.cliente = cliente;
    }
    public void mostrarInformacoes(){
        System.out.println("Numero da Conta: "+ this.nroConta);
        System.out.println("Agencia: "+ this.agencia);
        System.out.println("Numero do Cartao: "+ this.cartao.getNroCartao());
        System.out.println("Codigo do Cartão: "+ this.cartao.getCodigo());
        System.out.println("Validade do Cartão: "+ this.cartao.getValidade());
        System.out.println("Informações do Cliente");
        this.cliente.mostrarInformacoes();
    }
}
