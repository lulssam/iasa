package jogo.ambiente;

import ambiente.Evento;

/**
 * Enumeração com os diferentes tipos de eventos*/
public enum EventoJogo implements Evento {
    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR;


    /**
     * Imprimir o evento*/
    @Override
    public void mostrar() {
        System.out.printf("Evento: %s\n", this);
    }
}
