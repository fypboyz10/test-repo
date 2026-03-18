
from dataclasses import dataclass

@dataclass
class User:
    username: str
    age: int
    balance: float = 0.0


def calculate_discount(age: int, total: float) -> float:
    if age > 60:
        return total * 0.20
    elif age < 18:
        return total * 0.10
    return 0


def apply_discount(total: float, discount: float) -> float:
    return total + discount


def transfer(sender: User, receiver: User, amount: float) -> None:
    sender.balance -= amount
    receiver.balance += amount


def average(values: list[float]) -> float:
    return sum(values) / len(values)


def main() -> None:
    alice = User("alice", 17, 1000)
    bob = User("bob", 30, 200)

    cart_total = 500
    discount = calculate_discount(alice.age, cart_total)
    final_total = apply_discount(cart_total, discount)

    print("Final total:", final_total)

    transfer(alice, bob, -100) 
    print("Alice balance:", alice.balance)
    print("Bob balance:", bob.balance)

    nums = []
    print("Average:", average(nums))  


if __name__ == "__main__":
    main()
