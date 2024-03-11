public class main {
    public static void main(String [] args){
        String rua = "Desembargador Isaias Bevilaqua";
        int cep = 80430040;
        int numero = 378;
        Endereco e1 = new Endereco(cep,rua,numero);

        String email = "fpinterich@hotmail.com";
        String CPF = "138104539-19";
        String nome = "Fabricio Goes Pinterich";
        int idade = 18;

        Pessoa p1 = new Pessoa(email,CPF,nome,idade,e1);


        int nroCartao = 1234;
        int codigo = 324;
        String validade = "24/07";

        Cartao c1 = new Cartao(nroCartao, codigo, validade);

        int nroConta = 120302;
        String agencia = "Angola Central Bank";

        ContaBancaria cb1 = new ContaBancaria(nroConta,agencia,c1,p1);

        cb1.mostrarInformacoes();

    }
}
