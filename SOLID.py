#S ->   Single Responsibility Principle (SRP)
"""
This principle asserts that a class should focus on a single task or function.
It should have only one responsibility or reason for change.
This ensures that the class remains easier to comprehend, maintain, and modify.
"""
#! wrong example
class TransactionManager:
    def __init__(self):
        self.transactions = []
    
    # Responsibility for adding a new transaction
    def add_transaction(self, amount, description):
        self.transactions.append({"amount": amount, "description": description})
    
    # Total Account Responsibility
    def calculate_total(self):
        return sum(transaction["amount"] for transaction in self.transactions)
    
    # Responsibility for printing the report
    def print_report(self):
        print("Transaction Report:")
        for transaction in self.transactions:
            print(f"{transaction['description']}: ${transaction['amount']}")
        print(f"Total: ${self.calculate_total()}")

#todo Correct example
# Class responsible for representing financial transactions
class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

# Class responsible for managing transactions (adding, calculating total)
class TransactionManager:
    def __init__(self):
        self.transactions = []
    
    # Method to add a new transaction
    def add_transaction(self, amount, description):
        self.transactions.append(Transaction(amount, description))
    
    # Method to calculate the total of all transactions
    def calculate_total(self):
        return sum(transaction.amount for transaction in self.transactions)

# Class responsible for printing the transaction report
class ReportPrinter:
    def print_report(self, transaction_manager):
        print("Transaction Report:")
        for transaction in transaction_manager.transactions:
            print(f"{transaction.description}: ${transaction.amount}")
        print(f"Total: ${transaction_manager.calculate_total()}")

# Composite class that groups the objects together to form the system
class TransactionSystem:
    def __init__(self):
        # Composing the objects inside the TransactionSystem class
        self.manager = TransactionManager()
        self.report_printer = ReportPrinter()
    
    # Interface to add transactions
    def add_transaction(self, amount, description):
        self.manager.add_transaction(amount, description)
    
    # Interface to print the report
    def print_report(self):
        self.report_printer.print_report(self.manager)
    
    # Interface to get the total of all transactions
    def get_total(self):
        return self.manager.calculate_total()

# transaction_system = TransactionSystem()

# transaction_system.add_transaction(100, "شراء منتجات")
# transaction_system.add_transaction(50, "دفع فواتير")
# transaction_system.add_transaction(200, "إيداع في الحساب")

# transaction_system.print_report()

# total = transaction_system.get_total()
# print(f"المجموع الكلي لجميع المعاملات: ${total}")









#O ->   Open/Closed Principle (OCP)
"""
The Open/Closed Principle suggests that software entities (classes, modules, functions, etc.)
should be open for extension but closed for modification.
In other words:you should be able to extend the behavior of a class without modifying its existing code.
When writing the code, remember that you may add features to this code in the future,
so make your code ready for this."""
#! wrong example
class PaymentProcessor:
    def process_payment(self, amount, payment_type):
        if payment_type == "credit_card":
            print(f"Processing credit card payment of {amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of {amount}")
        else:
            raise ValueError("Unsupported payment type")

# processor = PaymentProcessor()
# processor.process_payment(100, "credit_card")  # Valed
# processor.process_payment(200, "paypal")      # Valed
# processor.process_payment(300, "bank_transfer")  # Error

#todo Correct example
from abc import ABC, abstractmethod

# واجهة مشتركة لجميع أنواع الدفع
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")


class BankTransferPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of {amount}")


class PaymentService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_payment(self, amount: float):
        self.payment_processor.process_payment(amount)


# credit_card_processor = CreditCardPaymentProcessor()
# paypal_processor = PayPalPaymentProcessor()
# bank_transfer_processor = BankTransferPaymentProcessor()


# payment_service = PaymentService(credit_card_processor)
# payment_service.process_payment(100)  # Valed

# payment_service = PaymentService(paypal_processor)
# payment_service.process_payment(200)  # Valed


# payment_service = PaymentService(bank_transfer_processor)
# payment_service.process_payment(300)  # Valed









#L -> Liskov Substitution Principle (LSP)
"""
According to this principle, objects of a subclass should be replaceable
with objects of the superclass without affecting the correctness of the program.
That is, subclasses should be able to substitute the parent class
without introducing errors or altering the desired behavior.

The core idea of the Liskov Substitution Principle (LSP) is that
a child class should be compatible with the parent class in terms of behavior,
so that you can replace an instance of the parent class with
an instance of the child class without causing logical problems or unexpected
changes in the program's behavior.

This means that the behavior the program expects when dealing with the parent
must be consistent with the behavior it expects when dealing with the child.

The principle is a standard for testing code and ensuring that derived
types do not cause unexpected behavior when used in place of base types.
"""
#! wrong example
class Car:
    def drive(self):
        print("Driving the car...")

    def refueling(self):
        print("Car refueling Now ...")


class LorryCar(Car):
    def drive(self):
        print("Driving the car...")

    def refueling(self):
        print("Car refueling Now ...")


class ElectricCar(Car):
    def drive(self):
        print("Driving the car...")

    def refueling(self):
        raise Exception("You can't fuel an electric car.")




#todo Correct example
class Car:
    def drive(self):
        print("Driving the car...")


class GasCar(Car):
    def refueling(self):
        print("Car refueling Now ...")

class ElectricCar(Car):
    def recharge(self):
        print("Car recharge Now ...")


class LorryCar(GasCar):
    def drive(self):
        print("Driving the LorryCar...")

    def refueling(self):
        print("Car refueling Now the LorryCar ...")


class TeslaElectricCar(ElectricCar):
    def drive(self):
        print("Driving the TeslaElectricCar...")

    def recharge(self):
        print("Car recharge Now The TeslaElectricCar ...")






#I -> Interface Segregation Principle (ISP)
"""
This principle advises that clients should not be forced to depend on interfaces
they do not use. Instead of having one large, general-purpose interface, break it down into smaller,
more specific interfaces that focus on a particular set of functionalities.
"""
#! wrong example

class IEmployee(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def take_break(self):
        pass
    
    @abstractmethod
    def attend_meeting(self):
        pass


class Worker(IEmployee):
    def work(self):
        print("Working...")
    
    def eat(self):
        print("Eating...")
    
    def take_break(self):
        print("Taking a break...")
    
    def attend_meeting(self):
        #Not necessary for this type of employee.
        print("Attending a meeting...")


class Manager(IEmployee):
    def work(self):
        print("Managing...")

    def eat(self):
        print("Eating...")

    def take_break(self):
        print("Taking a break...")
    
    def attend_meeting(self):
        print("Attending a meeting...")

#todo Correct example


# Business interface only
class IWorkable(ABC):
    @abstractmethod
    def work(self):
        pass

# Food only interface
class IFeedable(ABC):
    @abstractmethod
    def eat(self):
        pass

# Interface just for taking a break
class ITakableBreak(ABC):
    @abstractmethod
    def take_break(self):
        pass

# Meetings only interface
class IAttendingMeetings(ABC):
    @abstractmethod
    def attend_meeting(self):
        pass


class Worker(IWorkable, IFeedable, ITakableBreak):
    def work(self):
        print("Working...")
    
    def eat(self):
        print("Eating...")
    
    def take_break(self):
        print("Taking a break...")


class Manager(IWorkable, IFeedable, ITakableBreak, IAttendingMeetings):
    def work(self):
        print("Managing...")

    def eat(self):
        print("Eating...")

    def take_break(self):
        print("Taking a break...")
    
    def attend_meeting(self):
        print("Attending a meeting...")










#D -> Dependency Inversion Principle (DIP)
"""
This principle suggests that high-level modules should not depend on low-level modules.
Both should depend on abstractions (interfaces or abstract classes).
It also means that details should depend on abstractions, not the other way around.

Both high-level and low-level code depend on classes that inherit from
an abstract class or implement an interface.

Instead of relying on a fixed object that is hard-coded,
create an abstract class that defines the type of this object
and its behaviors. Then, create multiple classes that inherit from it
and implement these behaviors in their own way. You can then replace
these classes as needed and switch between them.
"""
#! wrong example
class SmtpEmailSender:
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to} via SMTP. Subject: {subject}, Body: {body}")

class EmailService:
    def __init__(self):
        self.smtp_sender = SmtpEmailSender()  # violation

    def send_email(self, to: str, subject: str, body: str):
        self.smtp_sender.send_email(to, subject, body)


#todo Correct example

class EmailSender(ABC): 
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str):
        pass


class SmtpEmailSender(EmailSender):
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to} via SMTP. Subject: {subject}, Body: {body}")

class MailgunEmailSender(EmailSender):
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to} via Mailgun API. Subject: {subject}, Body: {body}")

class SendGridEmailSender(EmailSender):
    def send_email(self, to: str, subject: str, body: str):
        print(f"Sending email to {to} via SendGrid API. Subject: {subject}, Body: {body}")


class EmailService:
    def __init__(self, sender: EmailSender): 
        self.sender = sender

    def send_email(self, to: str, subject: str, body: str):
        self.sender.send_email(to, subject, body)


mailgun_sender = MailgunEmailSender()
email_service_mailgun = EmailService(mailgun_sender)
email_service_mailgun.send_email("example@example.com", "Mailgun Test", "This is a test email using Mailgun.")