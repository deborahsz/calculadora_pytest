Calculadora com Testes Unitários


Sobre:

Esse projeto foi desenvolvido para praticar testes unitários utilizando Python e a biblioteca pytest.

A ideia foi implementar uma calculadora simples com algumas operações básicas e, em seguida, criar testes para verificar se essas funções estão funcionando corretamente.

Funcionalidades:

A calculadora possui as seguintes operações:

soma
subtração
multiplicação
divisão (com tratamento para divisão por zero)
fatorial (com validação para número negativo)
potência
Testes

Os testes foram feitos utilizando pytest.

Foram criados testes para:

casos normais (valores positivos)
casos com números negativos
casos de erro (como divisão por zero e fatorial de número negativo)
alguns casos limite (como zero)

O objetivo foi garantir que as funções se comportem corretamente em diferentes situações.


Estrutura:

calculadora.py → contém as funções da calculadora
test_calculadora.py → contém os testes
requirements.txt → dependência do projeto

--Como executar:

Instalar o pytest:

pip install -r requirements.txt


Rodar os testes:

python -m pytest
pytest

Observação:

Os testes foram pensados para cobrir diferentes cenários de uso, incluindo situações válidas e inválidas, seguindo o que foi visto em aula sobre testes unitários.
