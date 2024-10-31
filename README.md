# Evento

## Descrição

Prog e Cackto, personagens de um jogo de RPG chamado Fortaleza, precisam calcular a nova quantidade de experiência (XP) que os monstros terão durante um evento de aumento de experiência. O jogador deve ajudar a calcular essa nova XP com base em um fator de aumento fornecido.

## Entrada

A entrada consiste em múltiplos casos de teste, onde cada caso contém dois inteiros:
- `X`: um valor que indica o aumento da XP dos monstros (0 < X ≤ 3).
- `M`: o valor de XP atual do monstro (10 ≤ M ≤ 2²³ - 1).

A sequência de casos termina quando ambos os valores `X` e `M` forem iguais a 0. Esses valores não devem ser processados.

## Saída

Para cada caso de teste, o programa deve imprimir um único valor `E`, que é a nova experiência do monstro.

## Fórmula

A nova experiência é calculada usando a seguinte fórmula:
\[ E = M \times X \]

## Exemplo de Entrada e Saída

### Exemplo de Entrada:
```
1 544768710
2 538533133
3 38884958
0 0
```

### Exemplo de Saída:
```
544768710
1077066266
116654874
```

## Restrições

- 0 < X ≤ 3
- 10 ≤ M ≤ 2²³ - 1

## Implementação

Um exemplo de implementação em Python é:

```python
while True:
    X, M = map(int, input().split())
    if X == 0 and M == 0:
        break
    E = M * X
    print(E)
```

## Notas

- O programa deve garantir que a entrada seja processada até que `X` e `M` sejam ambos zero.
- Certifique-se de que os resultados sejam impressos como inteiros, sem casas decimais.
