from faststream.rabbit import RabbitExchange, ExchangeType
from infra.messaging.constants import Exchange

exchange_accounts = RabbitExchange(
    name=Exchange.ACCOUNTS, type=ExchangeType.TOPIC, durable=True
)
