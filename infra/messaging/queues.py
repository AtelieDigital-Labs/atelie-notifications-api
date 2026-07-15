from faststream.rabbit import RabbitQueue
from infra.messaging.constants import Queue, RoutingKey

user_created_queue = RabbitQueue(
    name=Queue.USER_CREATED,
    routing_key=RoutingKey.USER_CREATED,
    durable=True,
)
