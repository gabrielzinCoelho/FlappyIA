# Neural Network x Flappy Bird

Projeto onde uma rede neural foi desenvolvida para aprender a jogar **Flappy Bird**.

<p align="center">
  <img src="https://github.com/gabrielzinCoelho/FlappyIA/blob/main/preview.gif" alt="Demo animated">
</p>

# Sobre o Projeto

A ideia consiste em utilizar uma seleção artificial em conjunto com uma mutação para ajustar os pesos das sinapses entre os neurônios da rede. Dessa forma, os pesos dos pássaros que obtiveram o melhor desempenho tendem a ser conservados e reproduzidos nas novas gerações, com pequenas alterações em seus valores.

O jogo foi recriado do zero, sem engines, e totalmente programado na linguagem Python. A interface gráfica foi construída utilizando a biblioteca **Pygame**.

A Rede Neural utilizada foi uma Perceptron com 3 camadas:

 - Camada de Entrada com 2 neurônios, um para a distância horizontal até o centro da abertura e outro para a distância vertical até o mesmo.

 - Camada Escondida com 5 neurônios.

 - Camada de Saída com apenas 1 neurônio (responsável pela ação de pular).

 - A função de ativação utilizada em todos neurônios foi a **Logistic Sigmoid**.

 - O tamanho da população de cada geração foi de 60 passarinhos.

# Por quê?

O projeto foi desenvolvido com o objetivo de aprender na prática o funcionamento de uma rede neural.
