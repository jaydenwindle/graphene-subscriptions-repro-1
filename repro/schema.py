import graphene

from repro1.subscriptions import HelloSubscription

class Query(graphene.ObjectType):
    base = graphene.String()

class Subscription(HelloSubscription):
    pass


schema = graphene.Schema(
    query=Query,
    subscription=Subscription
)