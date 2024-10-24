# Sistema de Planejamento de Dieta Nutricional

Este é um sistema desenvolvido em Python utilizando a biblioteca Tkinter para criar uma interface gráfica que auxilia na geração de um plano alimentar baseado nas informações fornecidas pelo usuário, incluindo peso, altura, idade, sexo, meta (perder, manter ou ganhar peso), nível de atividade física e preferência alimentar.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Cálculo da Taxa Metabólica Basal (TMB)**: Baseada em peso, altura, idade e sexo do usuário.
2. **Necessidades Calóricas Diárias**: Calculadas com base na TMB e no nível de atividade física.
3. **Distribuição de Macronutrientes**: A proporção de proteínas, carboidratos e gorduras é calculada para um plano alimentar balanceado.
4. **Plano Alimentar Personalizado**: O usuário pode selecionar a preferência alimentar (vegano, vegetariano, onívoro, etc.) e o sistema sugere um plano diário com café da manhã, almoço, café da tarde, jantar e ceia.
5. **Cálculo de IMC (Índice de Massa Corporal)**: O sistema calcula o IMC com base no peso e altura do usuário e indica se ele está abaixo do peso, com peso normal, com sobrepeso ou com obesidade.
6. **Salvar Plano Alimentar**: O plano gerado pode ser salvo em um arquivo de texto para futura referência.

## Requisitos

- **Python 3.x**
- **Tkinter** (já incluída em instalações padrão do Python)

## Como usar

1. **Clone ou baixe este repositório.**
2. **Instale as dependências (caso necessário)**:  
   O Tkinter já vem embutido nas instalações padrão do Python. Caso tenha problemas, siga o comando abaixo para instalar:
   ```
   sudo apt-get install python3-tk
   ```

3. **Execute o script principal**:
   Para executar o script, navegue até o diretório do arquivo e use o seguinte comando:
   ```bash
   python3 seu_script.py
   ```

4. **Preencha as informações solicitadas na interface gráfica**:
   - Peso (em kg)
   - Altura (em cm)
   - Idade (em anos)
   - Sexo (Masculino ou Feminino)
   - Meta (Perder, Manter, Ganhar peso)
   - Nível de Atividade Física (Sedentário, Leve, Moderado, Intenso)
   - Preferência Alimentar (Vegano, Vegetariano, Onívoro, Low Carb, Cetogênica)

5. **Clique em "Gerar Plano de Dieta"**:
   O sistema calculará as calorias e os macronutrientes necessários e gerará um plano alimentar diário.

6. **Salvar Plano**:
   O plano gerado pode ser salvo em um arquivo de texto para referência futura clicando em "Salvar Plano de Dieta".

## Estrutura do Código

- `calcular_tmb(peso, altura, idade, sexo)`: Calcula a Taxa Metabólica Basal (TMB).
- `calcular_necessidades_caloricas(tmb, meta, atividade_fisica)`: Calcula as calorias diárias necessárias com base na TMB, meta e nível de atividade física.
- `distribuir_macronutrientes(calorias)`: Distribui as calorias em proteínas, carboidratos e gorduras.
- `sugerir_plano_alimentar(preferencia_alimentar, proteinas, carboidratos, gorduras)`: Sugere refeições baseadas na preferência alimentar do usuário.
- `calcular_imc(peso, altura)`: Calcula o Índice de Massa Corporal (IMC).
- `salvar_plano(resultado)`: Salva o plano gerado em um arquivo de texto.

## Exemplo de Plano Alimentar Gerado

```
Ingestão calórica diária recomendada: 2100.00 kcal
Proteínas: 157.50 g
Carboidratos: 210.00 g
Gorduras: 70.00 g

Seu IMC é: 23.5 - Peso normal

Plano Alimentar do Dia:
Café da Manhã: Ovo mexido com abacate (2 ovos, 100g de abacate), 1 fatia de pão integral - 31.5g de proteína, 42.0g de carboidrato, 21.0g de gordura
Almoço: Frango grelhado (200g), arroz integral (100g), 100g de legumes variados - 47.3g de proteína, 63.0g de carboidrato, 21.0g de gordura
Café da Tarde: Peixe com arroz (150g de peixe, 100g de arroz), 100g de salada verde - 31.5g de proteína, 42.0g de carboidrato, 12.0g de gordura
Jantar: Bife grelhado (150g), purê de batata-doce (100g), 100g de espinafre - 36.8g de proteína, 31.5g de carboidrato, 16.8g de gordura
Ceia: Queijo cottage (100g) com torrada integral e 1 maçã - 15.8g de proteína, 31.5g de carboidrato, 7.0g de gordura
```
