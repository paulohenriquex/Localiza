public class Caminhao extends Veiculos {

    private int quantidadeDeEixos;

    public Caminhao(String placa, String marca,String modelo,String cor, int anoFabricacao, int quantidadeDeEixos ){
        super(placa,marca,modelo,cor,anoFabricacao);
        this.quantidadeDeEixos = quantidadeDeEixos;
    }

    public void setQuantidadeDeEixos(int quantidadeDeEixos){
        this.quantidadeDeEixos = quantidadeDeEixos;
    }
    
    public int getQuantidadeDeEixos(){
        return quantidadeDeEixos;
    }
}
