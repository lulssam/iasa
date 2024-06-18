package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/**
 * Classe que estende Agente para definir a jogo.personagem dependente do ambiente de jogo*/

public class Personagem extends Agente {
    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
}
