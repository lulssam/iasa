package agente;

import ambiente.Comando;

/**
 * Representa uma ação que o agente pode executar num ambiente
 * */

public class Accao{

    private Comando comando;

    /**
     * Construtor
     * @param comando */
    public Accao(Comando comando) {
        this.comando = comando;
    }

    /**
     * Obtém o comndo associado à ação.
     * @return comando
     * */
    public Comando getComando() {
        return comando;
    }
}
