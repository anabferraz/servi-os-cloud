from s3_ada import create_s3, list_s3, upload_file_s3
from sqs import send_message
from receiver import consume_queue

def main():
    print("Bem-vindo(a) ao Controle de relatórios AWS da Nuclea! Vamos começar criando o seu bucket.")
    create_s3()
    upload_file_s3()
    list_s3()
    send_message()
    consume_queue()
    print("Obrigado(a) por utilizar o Controle de relatórios AWS da Núclea! Volte sempre! :D")

if __name__ == '__main__':

    response = main()