package ambiente;

/**
 * Interface que utiliza interfaces Evento e Comando
 * */

public interface Ambiente {
    /**
     * Não necessitamos de por public pois a interface em si já em publica e depois seria redundante*/
    void evoluir();
    Evento observar();
    void executar(Comando comando);
}
