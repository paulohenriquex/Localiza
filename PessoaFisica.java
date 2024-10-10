import java.util.Date;

public class PessoaFisica extends Cliente {

    private String cpf;
    private Date dataDeNascimento;

    public PessoaFisica(String cpf, Date dataDeNascimento, String nome, String rua, String cidade, int numero) {
        super(nome, rua, cidade, numero);
        this.cpf = cpf;
        this.dataDeNascimento = dataDeNascimento;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getCpf() {
        return cpf;
    }

    public void setDataDeNascimento(Date dataDeNascimento) {
        this.dataDeNascimento = dataDeNascimento;
    }

    public Date getDataDeNascimento(){
        return dataDeNascimento;
    }
}