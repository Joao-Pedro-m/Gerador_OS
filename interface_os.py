# interface_os.py
import tkinter as tk
from tkinter import messagebox
from gerador_os import gerar_ordem_servico

class OrdemServicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Ordem de Serviço")

        # Variáveis
        self.nome_cliente = tk.StringVar()
        self.veiculo = tk.StringVar()
        self.servicos = []

        # Widgets
        tk.Label(root, text="Nome do Cliente:").grid(row=0, column=0, sticky="w")
        self.entry_nome = tk.Entry(root, textvariable=self.nome_cliente, width=40)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(root, text="Veículo:").grid(row=1, column=0, sticky="w")
        self.entry_veiculo = tk.Entry(root, textvariable=self.veiculo, width=40)
        self.entry_veiculo.grid(row=1, column=1)

        # Seção para adicionar serviços
        tk.Label(root, text="Serviços Realizados:").grid(row=2, column=0, sticky="w")
        self.entry_servico = tk.Entry(root, width=20)
        self.entry_servico.grid(row=3, column=0)
        self.entry_qtd = tk.Entry(root, width=10)
        self.entry_qtd.grid(row=3, column=1)
        self.entry_preco = tk.Entry(root, width=10)
        self.entry_preco.grid(row=3, column=2)
        tk.Button(root, text="Adicionar Serviço", command=self.adicionar_servico).grid(row=3, column=3)

        self.lista_servicos = tk.Listbox(root, width=70)
        self.lista_servicos.grid(row=4, column=0, columnspan=4)

        # Botão Gerar PDF
        tk.Button(root, text="Gerar PDF", command=self.gerar_pdf).grid(row=5, column=1, pady=10)

    def adicionar_servico(self):
        descricao = self.entry_servico.get()
        quantidade = self.entry_qtd.get()
        preco = self.entry_preco.get()

        if descricao and quantidade and preco:
            self.servicos.append({
                "descricao": descricao,
                "quantidade": quantidade,
                "preco": float(preco)
            })
            self.lista_servicos.insert(tk.END, f"{descricao} - {quantidade}x - R$ {float(preco):.2f}")
            self.entry_servico.delete(0, tk.END)
            self.entry_qtd.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Inválida", "Preencha todos os campos do serviço.")

    def gerar_pdf(self):
        nome_cliente = self.nome_cliente.get()
        veiculo = self.veiculo.get()

        if not nome_cliente or not veiculo or not self.servicos:
            messagebox.showwarning("Entrada Incompleta", "Preencha todos os campos antes de gerar o PDF.")
            return

        total = sum(servico['preco'] for servico in self.servicos)
        gerar_ordem_servico(nome_cliente, veiculo, self.servicos, total)
        messagebox.showinfo("Sucesso", "Ordem de Serviço gerada com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrdemServicoApp(root)
    root.mainloop()
