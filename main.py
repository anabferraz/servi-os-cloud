from s3_ada import create_s3, list_s3, upload_file_s3, list_obj
from sqs import send_message
from receiver import consume_queue

def main():
    print("Bem-vindo(a) ao Controle AWS da Nuclea! Vamos começar criando o seu bucket.")
    create_s3()
    upload_file_s3()
    list_s3()
    list_obj()
    send_message()
    consume_queue()
    print("Obrigado(a) por utilizar o Controle AWS da Núclea! Volte sempre! :D")

if __name__ == '__main__':

    response = main()