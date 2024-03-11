public class Pessoa {
    String email;
    String CPF;
    String nome;
    int idade;
    Endereco endereco;

    public void setEmail(String email){
        this.email = email;
    }
    public void setCPF(String CPF){
        this.CPF = CPF;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setIdade(int idade){
        this.idade = idade;
    }
    public void setEndereco(Endereco endereco){
        this.endereco = endereco;
    }
    public String getEmail(){
        return this.email;
    }
    public String getCPF(){
        return this.CPF;
    }
    public String getNome(){
        return this.nome;
    }
    public int getIdade(){
        return this.idade;
    }
    public Endereco getEndereco(){
        return this.endereco;
    }

    public void mostrarInformacoes(){
        System.out.println("Email: "+ this.email);
        System.out.println("CPF: "+ this.CPF);
        System.out.println("Nome: "+ this.nome);
        System.out.println("Idade: "+ this.idade);
        System.out.println("CEP: "+ this.endereco.getCep());
        System.out.println("Rua: "+ this.endereco.getRua());
        System.out.println("Numero: "+ this.endereco.getNumero());
    }

    public Pessoa(String email, String CPF, String nome, int idade, Endereco endereco){
        this.email = email;
        this.CPF = CPF;
        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
    }
}
