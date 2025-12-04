import time
import threading
import logging
from datetime import datetime

# configura o arquivo de auditoria
logging.basicConfig(
    filename="auditoria.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# usuários cadastrados para o teste
contas = {
    "paciente": {"senha": "123", "perfil": "paciente"},
    "medico": {"senha": "123", "perfil": "profissional"},
    "admin": {"senha": "123", "perfil": "admin"}
}

# funções simples para simular requisitos não funcionais
def aplicar_wcag():
    print("(acessibilidade ok)")

def carregar_interface():
    print("(interface responsiva carregada)")

def testar_servidores():
    print("Verificando disponibilidade...")
    time.sleep(0.3)
    return True

# backup automático
def rotina_backup():
    while True:
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("backup.txt", "a") as arq:
            arq.write(f"Backup feito: {agora}\n")
        time.sleep(20)  # intervalo curto só para teste

def iniciar_backup():
    thr = threading.Thread(target=rotina_backup, daemon=True)
    thr.start()

# mede o tempo de resposta
def medir_resposta(t0, limite=0.5):
    tempo = time.time() - t0
    if tempo < limite:
        logging.info(f"Resposta rápida: {tempo:.3f}s")
    else:
        logging.warning(f"Resposta lenta: {tempo:.3f}s")

# menu do paciente
def menu_paciente(user):
    print("\n--- MENU PACIENTE ---")
    print("1. Atualizar dados")
    print("2. Agendar consulta")
    print("3. Cancelar consulta")
    print("4. Ver histórico")
    print("0. Sair")
    op = input("Escolha: ")

    logging.info(f"{user} -> opção {op} (paciente)")

    if op == "1":
        print("Dados atualizados.")
    elif op == "2":
        print("Consulta agendada.")
    elif op == "3":
        print("Consulta cancelada.")
    elif op == "4":
        print("Histórico exibido.")

# menu do profissional
def menu_profissional(user):
    print("\n--- MENU PROFISSIONAL ---")
    print("1. Agenda")
    print("2. Atualizar prontuário")
    print("3. Prescrever")
    print("4. Histórico do paciente")
    print("0. Sair")
    op = input("Escolha: ")

    logging.info(f"{user} -> opção {op} (profissional)")

    if op == "1":
        print("Agenda aberta.")
    elif op == "2":
        print("Prontuário atualizado.")
    elif op == "3":
        print("Prescrição emitida.")
    elif op == "4":
        print("Histórico mostrado.")

# menu do administrador
def menu_admin(user):
    print("\n--- MENU ADMINISTRADOR ---")
    print("1. Cadastros")
    print("2. Leitos")
    print("3. Suprimentos")
    print("4. Relatórios")
    print("5. Auditoria")
    print("0. Sair")
    op = input("Escolha: ")

    logging.info(f"{user} -> opção {op} (admin)")

    if op == "1":
        print("Gerenciando cadastros...")
    elif op == "2":
        print("Controle de leitos aberto.")
    elif op == "3":
        print("Suprimentos exibidos.")
    elif op == "4":
        print("Relatórios prontos.")
    elif op == "5":
        try:
            with open("auditoria.log", "r") as f:
                linhas = f.readlines()[-20:]
                print("\n--- ÚLTIMAS AÇÕES ---")
                for linha in linhas:
                    print(linha.strip())
        except:
            print("Nenhum log disponível.")

# login simples
def login():
    print("\n===== LOGIN =====")
    user = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if user in contas and contas[user]["senha"] == senha:
        logging.info(f"Acesso de {user}")
        return user, contas[user]["perfil"]
    else:
        print("Login inválido.")
        return None, None

# programa principal
def main():
    aplicar_wcag()
    carregar_interface()

    if not testar_servidores():
        print("Erro no servidor.")
        return

    iniciar_backup()

    while True:
        t0 = time.time()

        usuario, perfil = login()
        medir_resposta(t0)

        if not usuario:
            continue

        if perfil == "paciente":
            menu_paciente(usuario)
        elif perfil == "profissional":
            menu_profissional(usuario)
        elif perfil == "admin":
            menu_admin(usuario)

        sair = input("\nQuer encerrar? (s/n): ").lower()
        if sair == "s":
            print("Encerrando...")
            break

# início do sistema
if __name__ == "__main__":
    main()
