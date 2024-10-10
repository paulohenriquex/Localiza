public class Cliente {

    private String nome;
    private String rua;
    private String cidade;
    private int numero;

    Cliente(String nome, String rua, String cidade, int numero) {
        this.nome = nome;
        this.rua = rua;
        this.cidade = cidade;
        this.numero = numero;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setRua(String rua) {
        this.rua = rua;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getNome() {
        return nome;
    }

    public String getRua() {
        return rua;
    }

    public String getCidade() {
        return cidade;
    }

    public int getNumero() {
        return numero;
    }
}