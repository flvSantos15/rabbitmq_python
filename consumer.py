import pika


class RabbitMQConsumer:
  def __init__(self, callback):
    self.__host = 'localhost'
    self.__port = 5672
    self.__username = 'admin'
    self.__password = 'admin'
    self.__queue = 'data_queue'
    self.__calback = callback
    self.__channel = self.__create_channel()

  def __create_channel(self):
    connection_parameters = pika.ConnectionParameters(
      host=self.__host,
      port=self.__port,
      credentials=pika.PlainCredentials(
        username=self.__username,
        password=self.__password
      )
    )

    channel = pika.BlockingConnection(connection_parameters).channel()
    channel.queue_declare(
      queue=self.__queue,
      durable=True
    )
    channel.basic_consume(
      queue=self.__queue,
      auto_ack=True,
      on_message_callback=self.__calback
    )

    return channel

  def start(self):
    print(f'Listen RabbitMQ on port {self.__port}')
    self.__channel.start_consuming()

def minha_calback(channel, method, properties, body):
  print('Mensagem recebida:', body)

rabbitmq_consumer = RabbitMQConsumer(minha_calback)
rabbitmq_consumer.start()
