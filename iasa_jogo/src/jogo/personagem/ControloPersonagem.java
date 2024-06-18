package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import maqest.Estado;
import maqest.MaquinaEstados;

import static jogo.ambiente.ComandoJogo.*;
import static jogo.ambiente.EventoJogo.*;

/**
 * Classe que trata da ação do jogo.personagem*/
public class ControloPersonagem implements Controlo {
    private MaquinaEstados maqEst;

    /**
     * Construtor onde definimos os diferentes estados, ações e transições*/
    public ControloPersonagem() {
        // Definir estados
        Estado procura = new Estado("Procura");
        Estado inspecao = new Estado("Inspeção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        // Definir ações
        Accao procurar = new Accao(PROCURAR);
        Accao aproximar = new Accao(APROXIMAR);
        Accao observar = new Accao(OBSERVAR);
        Accao fotografar = new Accao(FOTOGRAFAR);


        // Definir transições
        procura.transicao(SILENCIO, procura, procurar) // Se o evento for SILENCIO, jogo.personagem vai para o estado procura e fica a procurar
                .transicao(ANIMAL, observacao, aproximar) // Se o evento for ANIMAL, jogo.personagem vai para o estado observacao e fica a aproximar
                .transicao(RUIDO, inspecao, aproximar);

        inspecao.transicao(RUIDO, inspecao, procurar)
                .transicao(ANIMAL, observacao, aproximar)
                .transicao(SILENCIO, procura);

        observacao.transicao(FUGA, inspecao)
                .transicao(ANIMAL, registo, observar);

        registo.transicao(ANIMAL, registo, fotografar)
                .transicao(FUGA, procura)
                .transicao(FOTOGRAFIA, procura);


        // Inciar maquina de estados com o estado inicial (procura)
        maqEst = new MaquinaEstados(procura);
    }

    /**
     * Método que obtém o evento e processa com a maquina de estados
     * @param percepcao Percepção
     *  @return accao - A ação que o agente deve executar com base na percepção.*/
    @Override
    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    /**
     * Método que mostra ações da jogo.personagem*/
    private void mostrar() {
        System.out.printf("Estado: %s\n",getEstado().getNome());
    }

    public Estado getEstado() {
        return maqEst.getEstado();
    }
    
}
