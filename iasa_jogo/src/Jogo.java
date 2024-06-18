import jogo.ambiente.AmbienteJogo;
import jogo.personagem.Personagem;

import static jogo.ambiente.EventoJogo.TERMINAR;

// AULA 4 DE MARÇO
/*
* Acoplamento: Queremos ter o menos acoplamento possivel para evitar interdependência
* e deixar um código mais simples. Para tal, usamos variaveis mais restritas (privadas, package)

* Coesão: Até que ponto o código está bem organizado ou não. Aqui, temos as coisas organizadas
* por semelhança em diferentes packages.

* Simplicidade: Até que ponto é fácil compreender o código. Até aqui usamos conhecimentos básicos
* introduzindo somente os Maps

* Adaptabilidade: Até que ponto é fácil mudar o código. Este codigo é bastante simples e direto logo
* e fosse preciso de mudar coisas, não seria muito complicado

* Queremos ter portanto um código com menos acoplamento e com mais coesão.
* Para desenvolvermos o código, começamos primeiro pela parte estrutural e só depois fazemos
* a implementação dos diferentes métodos.
*/

// AULA 11 DE MARÇO
/*
* MODELAÇÃO DE UM SISTEMA COMPUTACIONAL:

* Evolução no tempo que descreve os estados que um sistema pode assumir e a forma como
* elas evoluem ao longo do tempo determinando o comportamento do sistema. Estado do sistema
* evolui através do estado atual e da entrada. A função de saida transforma o estado para
* o exterior (lambda). A função Delta só se preocupa com a evolução.

* Saidas: Ações que o jogo.personagem vai fazer.
* Entradas: Tudo o que vem do exterior.
* Estado: Em que situação está o sistema

* ALFABETO:
* Letras maisculas: Usadas para conjuntos. Estes serão conjuntos de simbolos à entrada.
* Letras minusculas: Instâncias dos conjuntos. Estes seram conjuntos de simbolos à saida.
* Lambda: função de saida representada por z.
* Delta: função de entrada representada por s.

* DINÂMICA DA PERSONAGEM:
* Usamos um diagrama de transição de estado do comportamento do sistema pois permite
* representar graficamente a informação das tabelas, tornando mais facil a leitura e
* compreensão do sistema.

* DIAGRAMA DE TRANSIÇÃO DE ESTADO:
* Rectangulos ovais: estados.
* Bola preta: Estado inicial.
* Bola branca com ponto preto: Estado final.
* Setas: transições, acontecimento através do qual o sistema evolui de um estado actual
*        para um novo.
* Parenteses retos: condição booleana a ser verificada para ter de passar para o novo
*                   estado.
* Barra: Saida para gerar, ex: e1[g1]A2 -> o estado s1 faz a ação A1. Se ocorrer o
*        o evento e1 sendo que g1 é verdadeiro, executar A2 e ir para S2.

* EXEMPLO: COMPORTAMENTO DA PERSONAGEM
* Estado: Procura.
* Transição: ruido/aproximar.
* Novo Estado: Inspeção
* Aqui, quando ocorrer o evento "ruido", faz a ação "aproximar" e fica em inspeção.

* IMPLEMENTAÇÃO DA MÁQUINA DE ESTADOS
* Podemos factorizar a partir da colocação para evitar acoplamento nos métodos. A factorização consiste
* na decomposisão das partes de um sistema de modo a eliminiar a redundância. Vem do conceito matemático onde
* metemos em evidência a parte comum num produto. Em codigo, as partes repetidas serão eliminadas, e as partes
* partilhadas são mantidas.
* A máquina de estados vai representar o nosso processo interno.

* DIAGRAMAS DE ATIVIDADES:
* Losango: Decisão
* Um sistema pode ter vários fluxos / "caminhos" possiveis que são representados pelas setas.

* PARTIÇÕES DE EXECUÇÃO:
* Associar um comportamento a uma diferente parte da execução.

* FLUXO DE OBJETOS:
* Rectangulos: Objeto.
* Rectangulo oval: Atividade.

* MODELO DE AGENTE:
* Percepcionar ----> : Percepcao quer dizer que há uma ativação da percepcao que depois
* gera uma instancia (Percepcao p = percepcionar();)
* processar -----> : Accao -----> Actuar quer dizer qe processar vai devolver uma ação (varivel local).
* Também vai gerar uma instância ação.
* As setas entre : Percepcao e processar são de fluxo de controlo (inicia-se no processo agente)
*                   --> controlo.processar(percepcao);
* */

/**
 * Classe Jogo que contem o main */
public class Jogo {
    /**
     * De acordo com o diagrama de interação, começamos com criar o ambiente e a jogo.personagem*/
    private static AmbienteJogo ambiente;
    private static Personagem personagem;

    /**
     * De seguida, no main, inicializamos as variveis e chamamos o método executar*/
    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * Método executar resposavel por executar o jogo*/
    public static void executar() {
        do {
            ambiente.evoluir();
            personagem.executar();
        } while (ambiente.getEvento() != TERMINAR);
    }
}
