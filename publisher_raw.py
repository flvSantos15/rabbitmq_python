import pika

connection_parameters = pika.ConnectionParameters(
  host='localhost',
  port=5672,
  credentials=pika.PlainCredentials(
    username='admin',
    password='admin'
  )
) # parametros de conexão

channel = pika.BlockingConnection(connection_parameters).channel() # abrirmos a conexão

channel.basic_publish(
  exchange="data_exchange",
  routing_key="",
  body="Hello World! from publisher",
  properties=pika.BasicProperties(
    delivery_mode=2 # make message persistent
  )
)
