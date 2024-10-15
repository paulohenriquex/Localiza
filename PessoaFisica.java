import java.time.LocalDate;

public class PessoaFisica extends Clientes {

    private String cpf;
    private LocalDate dataDeNascimento;
    
    public PessoaFisica(String cpf, LocalDate dataDeNascimento, String nome, String rua, String cidade, int numero) {
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

    public void setDataDeNascimento(LocalDate dataDeNascimento) {
        this.dataDeNascimento = dataDeNascimento;
    }

    public LocalDate getDataDeNascimento() {
        return dataDeNascimento;
    }
}
