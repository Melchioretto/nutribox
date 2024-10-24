import tkinter as tk
from tkinter import messagebox

# Funções principais para cálculos
def calcular_tmb(peso, altura, idade, sexo):
    if sexo == 'M':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    return tmb

def calcular_necessidades_caloricas(tmb, meta, atividade_fisica):
    if atividade_fisica == "Sedentário":
        fator_atividade = 1.2
    elif atividade_fisica == "Leve":
        fator_atividade = 1.375
    elif atividade_fisica == "Moderado":
        fator_atividade = 1.55
    else:
        fator_atividade = 1.725

    calorias_diarias = tmb * fator_atividade
    if meta == "Perder":
        calorias_diarias -= 500
    elif meta == "Ganhar":
        calorias_diarias += 500
    
    return calorias_diarias

def distribuir_macronutrientes(calorias):
    proteinas = 0.3 * calorias / 4  # 30% de proteínas
    carboidratos = 0.4 * calorias / 4  # 40% de carboidratos
    gorduras = 0.3 * calorias / 9  # 30% de gorduras
    return proteinas, carboidratos, gorduras

# Função para sugerir refeições em cinco momentos do dia, incluindo legumes, verduras e frutas
def sugerir_plano_alimentar(preferencia_alimentar, proteinas, carboidratos, gorduras):
    cafe_manha = {
        "Vegano": f"Smoothie de frutas (300ml), 1 maçã - 3g de proteína, 45g de carboidrato, 1g de gordura",
        "Vegetariano": f"Iogurte com granola (200ml), 1 banana - 10g de proteína, 40g de carboidrato, 5g de gordura",
        "Onívoro": f"Ovo mexido com abacate (2 ovos, 100g de abacate), 1 fatia de pão integral - 12g de proteína, 20g de carboidrato, 15g de gordura"
    }

    almoco = {
        "Vegano": f"Salada de quinoa (100g), 200g de brócolis e cenoura - 10g de proteína, 40g de carboidrato, 5g de gordura",
        "Vegetariano": f"Salada caprese (150g de tomate, 100g de queijo), 200g de alface e rúcula - 12g de proteína, 30g de carboidrato, 15g de gordura",
        "Onívoro": f"Frango grelhado (200g), arroz integral (100g), 100g de legumes variados - {proteinas * 0.7:.1f}g de proteína, 45g de carboidrato, 10g de gordura"
    }

    cafe_tarde = {
        "Vegano": f"Tofu grelhado (150g), cenoura crua (100g) - {proteinas * 0.6:.1f}g de proteína, 20g de carboidrato, 5g de gordura",
        "Vegetariano": f"Omelete de claras (4 ovos), salada de tomate e alface - {proteinas * 0.5:.1f}g de proteína, 10g de carboidrato, 5g de gordura",
        "Onívoro": f"Peixe com arroz (150g de peixe, 100g de arroz), 100g de salada verde - {proteinas * 0.5:.1f}g de proteína, {carboidratos * 0.4:.1f}g de carboidrato, 8g de gordura"
    }

    jantar = {
        "Vegano": f"Salada de grão de bico (150g de grão de bico), 100g de espinafre - {proteinas * 0.4:.1f}g de proteína, 30g de carboidrato, 5g de gordura",
        "Vegetariano": f"Sopa de legumes com brócolis e abobrinha (200g), 100g de batata-doce - 15g de proteína, 40g de carboidrato, 5g de gordura",
        "Onívoro": f"Bife grelhado (150g), purê de batata-doce (100g), 100g de espinafre - {proteinas * 0.6:.1f}g de proteína, {carboidratos * 0.3:.1f}g de carboidrato, 8g de gordura"
    }

    ceia = {
        "Vegano": f"Frutas com castanhas (100g de frutas, 30g de castanhas), chá verde - 5g de proteína, 30g de carboidrato, 15g de gordura",
        "Vegetariano": f"Leite desnatado (200ml), 1 fatia de queijo branco - 10g de proteína, 12g de carboidrato, 5g de gordura",
        "Onívoro": f"Queijo cottage (100g) com torrada integral e 1 maçã - 12g de proteína, 25g de carboidrato, 5g de gordura"
    }

    plano = {
        "Café da Manhã": cafe_manha[preferencia_alimentar],
        "Almoço": almoco[preferencia_alimentar],
        "Café da Tarde": cafe_tarde[preferencia_alimentar],
        "Jantar": jantar[preferencia_alimentar],
        "Ceia": ceia[preferencia_alimentar]
    }

    return plano

def salvar_plano(resultado):
    # Salvar o plano em um arquivo com codificação UTF-8
    with open("plano_dieta.txt", "w", encoding="utf-8") as file:
        file.write(resultado)
    messagebox.showinfo("Sucesso", "Plano de dieta salvo com sucesso!")


def calcular_imc(peso, altura):
    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)
    return imc

def validar_entradas(peso, altura, idade):
    if peso <= 0 or altura <= 0 or idade <= 0:
        messagebox.showerror("Erro", "Todos os valores devem ser positivos.")
        return False
    return True

# Função para gerar o plano de dieta
def gerar_plano():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        idade = int(entry_idade.get())
        sexo = var_sexo.get()
        meta = var_meta.get()
        atividade_fisica = var_atividade.get()
        preferencia_alimentar = var_preferencia.get()

        if not validar_entradas(peso, altura, idade):
            return

        # Calcular TMB, calorias e macronutrientes
        tmb = calcular_tmb(peso, altura, idade, sexo)
        calorias_diarias = calcular_necessidades_caloricas(tmb, meta, atividade_fisica)
        proteinas, carboidratos, gorduras = distribuir_macronutrientes(calorias_diarias)
        plano = sugerir_plano_alimentar(preferencia_alimentar, proteinas, carboidratos, gorduras)

        # Calcular IMC
        imc = calcular_imc(peso, altura)

        # Formatando a saída com espaçamentos e emojis
        resultado = f"✨ Seu Plano Alimentar do Dia ✨\n"
        resultado += f"==============================\n"
        resultado += f"📊 Ingestão calórica diária recomendada: {calorias_diarias:.2f} kcal\n"
        resultado += f"🍗 Proteínas: {proteinas:.2f} g\n"
        resultado += f"🍞 Carboidratos: {carboidratos:.2f} g\n"
        resultado += f"🥑 Gorduras: {gorduras:.2f} g\n"
        resultado += f"==============================\n\n"

        resultado += f"📝 IMC: Seu IMC é {imc:.2f} - "
        if imc < 18.5:
            resultado += "⚠️ Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado += "✅ Peso normal"
        elif 25 <= imc < 29.9:
            resultado += "⚠️ Sobrepeso"
        else:
            resultado += "❌ Obesidade"
        
        resultado += "\n🍽️ Plano Alimentar do Dia:\n"
        resultado += "==============================\n"
        
        # Exibindo cada refeição com espaçamento adequado
        for refeicao, descricao in plano.items():
            resultado += f"🍴 **{refeicao}**\n{descricao}\n\n"

        # Exibir a mensagem final
        messagebox.showinfo("Plano de Dieta", resultado)

        # Botão para salvar o plano
        tk.Button(root, text="Salvar Plano de Dieta", command=lambda: salvar_plano(resultado)).grid(row=8, column=1)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Sistema de Planejamento de Dieta Nutricional")

# Labels e campos de entrada
tk.Label(root, text="Peso (kg):").grid(row=0, column=0)
entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1)

tk.Label(root, text="Altura (cm):").grid(row=1, column=0)
entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1)

tk.Label(root, text="Idade:").grid(row=2, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=2, column=1)

tk.Label(root, text="Sexo:").grid(row=3, column=0)
var_sexo = tk.StringVar(value="M")
tk.Radiobutton(root, text="Masculino", variable=var_sexo, value="M").grid(row=3, column=1)
tk.Radiobutton(root, text="Feminino", variable=var_sexo, value="F").grid(row=3, column=2)

tk.Label(root, text="Meta:").grid(row=4, column=0)
var_meta = tk.StringVar(value="Manter")
tk.OptionMenu(root, var_meta, "Perder", "Ganhar", "Manter").grid(row=4, column=1)

tk.Label(root, text="Nível de Atividade Física:").grid(row=5, column=0)
var_atividade = tk.StringVar(value="Moderado")
tk.OptionMenu(root, var_atividade, "Sedentário", "Leve", "Moderado", "Intenso").grid(row=5, column=1)

tk.Label(root, text="Preferência Alimentar:").grid(row=6, column=0)
var_preferencia = tk.StringVar(value="Onívoro")
tk.OptionMenu(root, var_preferencia, "Vegano", "Vegetariano", "Onívoro", "Low Carb", "Cetogênica").grid(row=6, column=1)

# Botão para gerar plano de dieta
tk.Button(root, text="Gerar Plano de Dieta", command=gerar_plano).grid(row=7, column=1)

# Rodar a interface
root.mainloop()
