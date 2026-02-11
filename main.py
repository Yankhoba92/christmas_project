from abc import ABC, abstractmethod

class TypeGiftOrder(ABC):
    def createGift(self):
        pass

class PlayOrder(TypeGiftOrder):
    def description(self):
        return "Play"

class PhoneOrder(TypeGiftOrder):
    def description(self):
        return "Phone"

class RingOrder(TypeGiftOrder):
    def description(self):
        return "Ring"

class TypeGiftOrderFactory:
    @staticmethod
    def createGift(typeGift):
        if typeGift == "Play":
            return PlayOrder()
        elif typeGift == "Ring":
            return RingOrder()
        elif typeGift == "Phone":
            return PhoneOrder()
        raise ValueError("Type de jouer indisponible")

toy1 = TypeGiftOrderFactory.createGift("Play")
toy2 = TypeGiftOrderFactory.createGift("Phone")

print(toy1.description())
print(toy2.description())


class Giftpersonalization:
    def __init__(self, gift):
        self.gift = gift

    def description(self):
        return self.gift.description()


class pesrnalizedMessage(Giftpersonalization):
    def __init__(self, gift, text):
        super().__init__(gift)
        self.text = text
    def description(self):
        return self.gift.description()+ f" with message '{self.text}'"

class personalizedPackaging(Giftpersonalization):
    def description(self):
        return  self.gift.description() + " avec un packaging specifique"

class basicPersonalization(Giftpersonalization):
    def description(self):
        return self.gift.description() + "Cadeau  basic sans personalisation"

gift1 = pesrnalizedMessage(toy1, "Happy Birthday!")
gift2 = personalizedPackaging(toy2)
print(gift1.description())
print(gift2.description())


class Elf:
    def __init__(self, name):
        self.name = name

    def update(self, gift_description):
        print(f"Elf {self.name} notified: {gift_description}")
class Workshop:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify(self, gift_description):
        for observer in self.observers:
            observer.update(gift_description)

workshop = Workshop()
elf1 = Elf("Buddy")
workshop.register(elf1)
workshop.notify(gift1.description())

class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self, gift: Giftpersonalization) -> str:
        pass

class ReindeerDelivery(DeliveryStrategy):
    def deliver(self, gift: Giftpersonalization) -> str:
        return f"Delivered by Reindeer: {gift.description()}"

class SleighDelivery:
    def deliver(self):
        return "Delivered by magic sleigh"

class DroneDelivery(DeliveryStrategy):
    def deliver(self, gift: Giftpersonalization) -> str:
        return f"Delivered by Drone: {gift.description()}"


delivery1 = DroneDelivery()
print(delivery1.deliver(gift1))

class SantaClausFacade:
    def __init__(self):
        self.factory = Giftpersonalization()
        self.workshop = Workshop()
        self.workshop.register(elf1)

    def prepare_and_deliver(self, TypeGift, personalization_type, delivery_strategy):

        gift = TypeGiftOrderFactory.createGift(TypeGift)

        if personalization_type == "message":
            gift = pesrnalizedMessage(gift, "We wish u a merry christmas!")
        elif personalization_type == "packaging":
            gift = personalizedPackaging(gift)
        else:
            gift = basicPersonalization(gift)

        self.workshop.notify(gift.description())
        return delivery_strategy.deliver(gift)