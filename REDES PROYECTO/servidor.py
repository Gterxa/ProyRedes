import socket

def send_pdf(client_socket, pdf_path):
    # Abre y lee el archivo PDF en binario
    with open(pdf_path, 'rb') as file:
        pdf_data = file.read()

    # Envía el tamaño del archivo al cliente
    pdf_size = len(pdf_data)
    client_socket.sendall(pdf_size.to_bytes(4, byteorder='big'))

    # Envía el archivo PDF al cliente
    client_socket.sendall(pdf_data)

# Configura el servidor
host = '0.0.0.0'
port = 5555
pdf_path = 'documento.pdf'  # Cambia esto con la ruta de tu archivo PDF

# Crea un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula el socket a una dirección y puerto
server_socket.bind((host, port))

# Escucha las conexiones entrantes
server_socket.listen(5)
print(f"El servidor está escuchando en {host}:{port}")

while True:
    # Acepta la conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión desde: {client_address}")

    # Envía el archivo PDF al cliente
    send_pdf(client_socket, pdf_path)

    # Cierra la conexión con el cliente actual
    client_socket.close()
    