public class PessoaJuridica extends Clientes {

    private String cnpj;

    public PessoaJuridica(String cnpj, String nome, String rua, String cidade, int numero) {
        super(nome, rua, cidade, numero);
        this.cnpj = cnpj;
    }

    public void setCnpj(String cnpj){
        this.cnpj = cnpj;
    }
    public String getCnpj(){
        return cnpj;
    }

}