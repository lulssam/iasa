package jogo.ambiente;

// Imports

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class AmbienteJogo implements Ambiente {

    // Usamos uma visibilidade privada para evitar acoplamento
    private Scanner scanner = new Scanner(System.in); // Inicializar o scanner para receber os inputs do utilizador
    private Map<String, EventoJogo> eventos; // "Traduzir" a string para o tipo EventoJogo
    private EventoJogo evento; // Pedimos ao utilizador para gerar um EventoJogo

    /**
     * Construtor:
     * Mapeamos as teclas aos diferentes modos usando um HashMap
     */
    public AmbienteJogo() {
        eventos = new HashMap<>();
        eventos.put("s", EventoJogo.SILENCIO); // A tecla "s" vai ativar o "SILENCIO"
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }

    /**
     * Atualizar o evento
     */
    @Override
    public void evoluir() {
        evento = gerarEvento();
    }


    /**
     * Dar acesso ao evento e mostra o evento observado
     * @return evento
     */
    @Override
    public Evento observar() {
        evento.mostrar();
        return evento;
    }

    /**
     * Mostrar o comando com o método da interface
     * @param comando Comando que utilizador pedir
     */
    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    /**
     * Método auxiliar que pede ao utilizador para indicar o ambiente e gera-o
     */
    private EventoJogo gerarEvento() {
        System.out.print("\nEvento? ");
        String textoComando = scanner.next(); // Pedir ao utilzador o evento
        return eventos.get(textoComando); // Mapear a string em eventojogo
    }

    public EventoJogo getEvento() {
        return evento;
    }
}
