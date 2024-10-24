# 🥗 Sistema de Planejamento de Dieta Nutricional

Este é um sistema desenvolvido em **Python** utilizando a biblioteca **Tkinter** para criar uma interface gráfica que auxilia na geração de um plano alimentar personalizado. Baseado nas informações fornecidas pelo usuário, como peso, altura, idade, sexo, meta de peso, nível de atividade física e preferência alimentar, o sistema sugere refeições adequadas ao longo do dia. 🍽️

## ✨ Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. 🧮 **Cálculo da Taxa Metabólica Basal (TMB)**: Baseada em peso, altura, idade e sexo do usuário.
2. 🔥 **Necessidades Calóricas Diárias**: Calculadas com base na TMB e no nível de atividade física.
3. 🍏 **Distribuição de Macronutrientes**: Calcula a quantidade de proteínas, carboidratos e gorduras para um plano alimentar balanceado.
4. 🍽️ **Plano Alimentar Personalizado**: O usuário pode selecionar sua preferência alimentar (vegano, vegetariano, onívoro, etc.) e o sistema sugere refeições para cada momento do dia (café da manhã, almoço, etc.).
5. 📊 **Cálculo de IMC (Índice de Massa Corporal)**: O sistema calcula o IMC com base no peso e altura e fornece um status de saúde.
6. 💾 **Salvar Plano Alimentar**: O plano gerado pode ser salvo em um arquivo de texto para consulta futura.

## 🔧 Requisitos

- **Python 3.x** 🐍
- **Tkinter** (já incluída nas instalações padrão do Python)

## 🚀 Como usar

1. **Clone ou baixe este repositório.**
2. **Instale as dependências (se necessário)**:
   O Tkinter já vem embutido nas instalações padrão do Python. Caso haja problemas, use o comando abaixo:
   ```bash
   sudo apt-get install python3-tk
