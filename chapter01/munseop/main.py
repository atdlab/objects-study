from chapter01.Bag import Bag
from chapter01.Invitation import Invitation
from chapter01.Ticket import Ticket

bag = Bag(amount=100, ticket=Ticket())
print(bag.plus_amount(10))
