import socket

def receive_pdf(client_socket, save_path):
    #Recibe el tamaño del archivo PDF
    pdf_size_bytes = client_socket.recv(4)
    pdf_size = int.from_bytes(pdf_size_bytes, byteorder='big')

    #Recibe el archivo PDF en bloques y escribe en un archivo
    with open(save_path, 'wb') as file:
        remaining_size = pdf_size
        while remaining_size > 0:
            data = client_socket.recv(1024)
            file.write(data)
            remaining_size -= len(data)

#Configura el cliente
host = '192.168.5.2' #Se configura manualmente la ip del servidor
port = 5555
save_path = 'documento_recibido.pdf'  # Cambia esto con la ruta donde quieras guardar el PDF

#Se establece la comunicación TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta el socket al servidor
client_socket.connect((host, port))

#Recibe el archivo PDF del servidor
receive_pdf(client_socket, save_path)

#Cierra la conexión con el servidor
client_socket.close()