package maqest;

import agente.Accao;

public class Transicao {
    private Accao accao;
    private Estado estadoSucessor;

    public Transicao(Accao accao, Estado estadoSucessor) {
        this.accao = accao;
        this.estadoSucessor = estadoSucessor;
    }

    public Accao getAccao() {
        return accao;
    }

    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }
}
