package maqest;

import agente.Accao;
import ambiente.Evento;

public class MaquinaEstados {

    private Estado estado;

    /**
     * @param estadoInicial Guardar o estado inicial (Procura)
     */
    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    /**
     * Método que representa o processo interno. Ativamos o processar evento do seu estado
     * para e à tabela, e assim acede-la fazendo o get(evento): Este get vai retornar a
     * transição que corresponde ao evento.
     * @param evento
     * @return Ação
     */
    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        } else {
            return null;
        }
    }

    /**
     * Getter do estado
     */
    public Estado getEstado() {

        return estado;
    }
}
