package agente;

public interface Controlo {

    /**
     * Processa uma percepção e decide qual é a ação que o agente tem que executar.
     *
     * @param percepcao A percepção do ambiente.
     */
    Accao processar(Percepcao percepcao);
}
