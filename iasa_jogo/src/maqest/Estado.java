package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

public class Estado {
    private String nome;
    private Map<Evento, Transicao> transicoes;

    /**
     * Construtor
     *
     * @param nome Guardar nome do estado
     */
    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<>();
    }

    /**
     * Processar o evento.
     *
     * @param evento Evento a ser processado
     * @return Transição
     */
    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /**
     * Adicionar a dicionário de transições -> Transicão sem ação
     *
     * @param evento
     * @param estadoSucessor
     * @return Estado
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Adicionar a dicionário de transições -> Transição com ação
     *
     * @param evento
     * @param accao
     * @param estadoSucessor
     * @return Estado
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        transicoes.put(evento, new Transicao(accao, estadoSucessor));
        return this;
    }

    public String getNome() {
        return nome;
    }

    public Map<Evento, Transicao> getTransicoes() {
        return transicoes;
    }
}
