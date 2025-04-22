import services.funcionario_service as func_service
import services.insumo_service as insu_service
import services.financeiro_service as finan_service
import services.relatorio_service as relat_service
import services.talhoes_service as talh_service
import services.tarefa_service as tare_service

def exibir_menu_principal():
    print("\n======= MENU PRINCIPAL =======")
    print("1 - Funcionários e Atividades")
    print("2 - Gestão de Insumos e Estoque")
    print("3 - Produção por Talhão")
    print("4 - Controle Financeiro") 
    print("5 - Relatórios")
    print("6 - Checklist de Tarefas")
    print("7 - Sair")

def exibir_menu_crud(titulo):
    print(f"\n--- Menu: {titulo} ---")
    print("1 - Criar")
    print("2 - Consultar")
    print("3 - Atualizar")
    print("4 - Remover")
    print("5 - Voltar ao menu principal")

def normalizar_entrada(opcao):
    return opcao.strip().lower()

def menu_funcionarios():
    while True:
        exibir_menu_crud("Funcionários e Atividades")
        entrada = input("Escolha uma opção: ")
        opcao = normalizar_entrada(entrada)

        match opcao:
            case "1" | "criar":
                print("----- CADASTRAR FUNCIONÁRIO -----\n")
                func_service.cadastrar_funcionario()

            case "2" | "consultar":
                print("----- CONSULTAR FUNCIONÁRIO -----\n")
                func_service.consultar_funcionario()

            case "3" | "atualizar":
                print("----- ATUALIZAR FUNCIONÁRIO -----\n")
                func_service.atualizar_funcionario()

            case "4" | "remover":
                print("----- REMOVER FUNCIONÁRIO -----\n")
                func_service.remover_funcionario()

            case "5" | "voltar":
                break
            case _:
                print("Opção inválida. Tente novamente.")

def menu_insumos():
    while True:
        exibir_menu_crud("Gestão de Insumos e Estoque")
        entrada = input("Escolha uma opção: ")
        opcao = normalizar_entrada(entrada)

        match opcao:
            case "1" | "criar":
                print("----- CADASTRAR INSUMO -----\n")
                insu_service.cadastrar_insumo()

            case "2" | "consultar":
                print("----- CONSULTAR INSUMO -----\n")
                insu_service.consultar_insumo()

            case "3" | "atualizar":
                print("----- ATUALIZAR INSUMO -----\n")
                insu_service.atualizar_insumo()

            case "4" | "remover":
                print("----- REMOVER INSUMO -----\n")
                insu_service.remover_insumo()

            case "5" | "voltar":
                break
            case _:
                print("Opção inválida. Tente novamente.")

def menu_producao():
    while True:
        exibir_menu_crud("Produção por Talhão")
        entrada = input("Escolha uma opção: ")
        opcao = normalizar_entrada(entrada)

        match opcao:
            case "1" | "criar":
                print("----- CADASTRAR PRODUÇÃO -----\n")
                talh_service.cadastrar_talhao()

            case "2" | "consultar":
                print("----- CONSULTAR PRODUÇÃO -----\n")
                talh_service.consultar_talhao()

            case "3" | "atualizar":
                print("----- ATUALIZAR PRODUÇÃO -----\n")
                talh_service.update_talhao()

            case "4" | "remover":
                print("----- REMOVER PRODUÇÃO -----\n")
                talh_service.delete_talhao()

            case "5" | "voltar":
                break
            case _:
                print("Opção inválida. Tente novamente.")

def menu_financeiro():
    while True:
        exibir_menu_crud("Controle Financeiro")
        entrada = input("Escolha uma opção: ")
        opcao = normalizar_entrada(entrada)

        match opcao:
            case "1" | "criar":
                print("----- CADASTRAR FINANÇAS -----\n")
                finan_service.cadastrar_financeiro()

            case "2" | "consultar":
                print("----- CONSULTAR FINANÇAS -----\n")
                finan_service.consultar_financeiro()

            case "3" | "atualizar":
                print("----- ATUALIZAR FINANÇAS -----\n")
                finan_service.atualizar_financeiro()

            case "4" | "remover":
                print("----- REMOVER FINANÇAS -----\n")
                finan_service.remover_financeiro()

            case "5" | "voltar":
                break
            case _:
                print("Opção inválida. Tente novamente.")

def menu_relatorios():
    while True:
        exibir_menu_crud("Relatórios")
        entrada = input("Escolha uma opção: ")
        opcao = normalizar_entrada(entrada)

        match opcao:
            case "1" | "criar":
                print("----- CADASTRAR RELATÓRIO -----\n")
                relat_service.cadastrar_relatorio()

            case "2" | "consultar":
                print("----- CONSULTAR RELATÓRIO -----\n")
                relat_service.consultar_relatorio()

            case "3" | "atualizar":
                print("----- ATUALIZAR RELATÓRIO -----\n")
                relat_service.update_relatorio()

            case "4" | "remover":
                print("----- REMOVER RELATÓRIO -----\n")
                relat_service.delete_relatorio()

            case "5" | "voltar":
                break
            case _:
                print("Opção inválida. Tente novamente.")

def menu_checklist():
    while True:
        exibir_menu_crud("Checklist de Tarefas")
        entrada = input("Escolha uma opção: ")
        opcao = normalizar_entrada(entrada)

        match opcao:
            case "1" | "criar":
                print("----- CADASTRAR TAREFAS -----\n")
                tare_service.cadastrar_tarefa()

            case "2" | "consultar":
                print("----- CONSULTAR TAREFAS -----\n")
                tare_service.consultar_tarefa()

            case "3" | "atualizar":
                print("----- ATUALIZAR TAREFAS -----\n")
                tare_service.atualizar_tarefa()

            case "4" | "remover":
                print("----- REMOVER TAREFAS -----\n")
                tare_service.remover_tarefa()

            case "5" | "voltar":
                break
            case _:
                print("Opção inválida. Tente novamente.")


def main():
    while True:
        exibir_menu_principal()
        entrada = input("Escolha uma opção: ")
        opcao = normalizar_entrada(entrada)

        match opcao:
            case "1" | "funcionarios" | "funcionários e atividades":
                menu_funcionarios()
            case "2" | "insumos" | "gestão de insumos e estoque":
                menu_insumos()
            case "3" | "produção" | "producao" | "produção por talhão":
                menu_producao()
            case "4" | "financeiro" | "controle financeiro":
                menu_financeiro()
            case "5" | "relatórios" | "relatorios":
                menu_relatorios()
            case "6" | "checklist" | "checklist de tarefas":
                menu_checklist()
            case "7" | "sair":
                print("Encerrando o sistema. Obrigado!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
