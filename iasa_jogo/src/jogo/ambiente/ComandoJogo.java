package jogo.ambiente;

import ambiente.Comando;

/**
 * Enumaração com os diferentes tipos de ações
 * */
public enum ComandoJogo implements Comando {
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    /**
     * Imprimir a ação*/
    @Override
    public void mostrar() {
        System.out.printf("Ação: %s\n", this);
    }
}
