import pika


def minha_calback(channel, method, properties, body):
  print('Mensagem recebida: ', body)

connection_parameters = pika.ConnectionParameters(
  host='localhost',
  port=5672,
  credentials=pika.PlainCredentials(
    username='admin',
    password='admin'
  )
) # parametros de conexão

channel = pika.BlockingConnection(connection_parameters).channel() # abrirmos a conexão
channel.queue_declare(
  queue='data_queue', # nome como foi definido no rabbit
  durable=True
)
channel.basic_consume(
  queue='data_queue', # de quem eu vou consumir
  auto_ack=True,
  on_message_callback=minha_calback
)

print(f'Listen RabbitMQ on port 5672') 
channel.start_consuming()