package agente;

import ambiente.Evento;

/**
 * Representa a percepção do agente sobre o ambiente.
 */
public class Percepcao {
    private Evento evento;

    /**
     * Construtor
     * @param evento */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    /**
     * Obtém o evento associado à percepção
     * @return evento "{read only}"
     * */
    public Evento getEvento() {
        return this.evento;
    }
}
