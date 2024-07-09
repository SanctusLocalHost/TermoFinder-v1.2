import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def buscar_termo():
    termo = entry_termo.get()
    diretorio = entry_diretorio.get()

    if not termo:
        messagebox.showwarning("Aviso", "Por favor, insira um termo para buscar.")
        return
    
    if not diretorio:
        messagebox.showwarning("Aviso", "Por favor, selecione um diretório.")
        return

    resultados_text.delete(1.0, tk.END)  # Limpa a caixa de texto de resultados

    arquivos = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f)) and not f.endswith(('.py', '.pyw', '.exe'))]
    encontrados = []

    for arquivo in arquivos:
        try:
            with open(os.path.join(diretorio, arquivo), 'r', encoding='utf-8') as f:
                conteudo = f.read()
                if termo.lower() in conteudo.lower():
                    encontrados.append(arquivo)
        except Exception as e:
            print(f"Erro ao ler o arquivo {arquivo}: {e}")

    if encontrados:
        resultados_text.insert(tk.END, f"Termos localizados nos seguintes arquivos:\n")
        for arquivo in encontrados:
            resultados_text.insert(tk.END, f"- {arquivo}\n")
    else:
        resultados_text.insert(tk.END, "Nenhum item encontrado.")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        entry_diretorio.delete(0, tk.END)
        entry_diretorio.insert(0, diretorio)

# Configuração da janela principal
root = tk.Tk()
root.title("TermoFinder V1.2")

# Configuração da interface
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Campo de entrada para o diretório
ttk.Label(frame, text="Diretório:", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, sticky=tk.W)
entry_diretorio = ttk.Entry(frame, width=30)
entry_diretorio.grid(row=0, column=1, sticky=(tk.W, tk.E))

# Botão para selecionar o diretório
btn_selecionar_diretorio = ttk.Button(frame, text="Selecionar Diretório", command=selecionar_diretorio)
btn_selecionar_diretorio.grid(row=0, column=2, sticky=tk.W)

# Campo de entrada para o termo de busca
ttk.Label(frame, text="Termo para buscar:", font=('Helvetica', 10, 'bold')).grid(row=1, column=0, sticky=tk.W)
entry_termo = ttk.Entry(frame, width=30)
entry_termo.grid(row=1, column=1, sticky=(tk.W, tk.E))

# Botão para iniciar a busca
btn_buscar = ttk.Button(frame, text="Buscar", command=buscar_termo)
btn_buscar.grid(row=1, column=2, sticky=tk.W)

# Caixa de texto para exibir resultados
resultados_text = tk.Text(frame, height=15, width=50)
resultados_text.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

# Rótulo de dica para uso
dica_label = ttk.Label(frame, text="Dica de Uso:\n1. Selecione o diretório onde os arquivos estão localizados.\n2. Insira o termo que deseja buscar.\n3. Clique em 'Buscar' para ver os resultados.")
dica_label.grid(row=3, column=0, columnspan=3, pady=10)

# Configuração do redimensionamento
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

# Iniciar a aplicação
root.mainloop()
