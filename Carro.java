public class Carro extends Veiculos {

    private int quantiaddeDePortas;

    public Carro(
        String placa,
        String marca,
        String modelo,
        String cor,
        int anoFabricacao,
        int quantiaddeDePortas
    ) {
        super(placa, marca, modelo, cor, anoFabricacao);
        this.quantiaddeDePortas = quantiaddeDePortas;
    }

    public void setQuantidadeDePortas(int quantiaddeDePortas) {
        this.quantiaddeDePortas = quantiaddeDePortas;
    }

    public int getQuantidadeDePortas() {
        return quantiaddeDePortas;
    }
}
