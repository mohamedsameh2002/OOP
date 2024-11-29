# استيراد مكتبة ABC و abstractmethod لإنشاء فئات مجردة (Abstract Base Classes)
from abc import ABC, abstractmethod

# تعريف فئة Library تمثل مكتبة
class Library:
    # قائمة لتخزين الكتب والفروع في المكتبة
    _books = []
    _branches = []
    
    # إضافة كتاب إلى مكتبة المكتبة
    @classmethod
    def add_book(cls, book):
        cls._books.append(book)
        
    # استرجاع قائمة الكتب من المكتبة
    @classmethod
    def get_books(cls):
        return cls._books
    
    # إضافة فرع جديد للمكتبة
    @classmethod
    def add_branch(cls, branch):
        cls._branches.append(branch)
        
    # استرجاع قائمة الفروع في المكتبة
    @classmethod
    def get_branches(cls):
        return cls._branches


# تعريف فئة مجردة Item تمثل عنصر في المكتبة (مثل الكتاب)
class Item(ABC):
    def __init__(self, title, author):
        # يتم تخزين العنوان واسم المؤلف كخصائص خاصة
        self._title = title
        self._author = author
    
    # تعريف الدالة المجردة للحصول على تفاصيل العنصر
    @abstractmethod
    def get_details(self):
        pass
    
    # خاصية للحصول على العنوان
    @property
    def title(self):
        return self._title
    
    # خاصية للحصول على اسم المؤلف
    @property
    def author(self):
        return self._author

# فئة Book تمثل الكتاب وتورث من فئة Item
class Book(Item):
    def __init__(self, title, author, isbn, category):
        # استدعاء مُنشئ الفئة المجردة
        super().__init__(title, author)
        self._isbn = isbn  # تخزين رقم الكتاب الدولي
        self._category = category  # تخزين الفئة (مثل: ديني، رواية، الخ)
        
    # تنفيذ دالة الحصول على تفاصيل الكتاب
    def get_details(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self._isbn}, Category: {self._category}"
    
    # تمثيل النص للكتاب
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    # تمثيل الكتاب بطريقة أكثر تفصيلًا
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self._isbn}', '{self._category}')"

# فئة EBook تمثل الكتاب الإلكتروني، وهي تورث من فئة Book
class EBook(Book):
    def __init__(self, title, author, isbn, category, file_size):
        # استدعاء مُنشئ فئة الكتاب
        super().__init__(title, author, isbn, category)
        self._file_size = file_size  # تخزين حجم الملف بالميجابايت
    
    # تنفيذ دالة الحصول على تفاصيل الكتاب الإلكتروني
    def get_details(self):
        return f"EBook: {self.title} by {self.author}, ISBN: {self._isbn}, Category: {self._category}, File Size: {self._file_size}MB"
    
    # تمثيل النص للكتاب الإلكتروني
    def __str__(self):
        return f"EBook: {self.title} by {self.author}"

# فئة Branch تمثل فرعًا من فروع المكتبة
class Branch:
    def __init__(self, name, location):
        self.name = name  # اسم الفرع
        self.location = location  # مكان الفرع
        self.books = []  # قائمة لتخزين الكتب المتاحة في هذا الفرع
    
    # إضافة كتاب إلى الفرع
    def add_book(self, book):
        self.books.append(book)
    
    # الحصول على قائمة الكتب المتاحة في الفرع
    def get_books(self):
        return self.books
    
    # تمثيل النص للفرع
    def __str__(self):
        return f"Branch: {self.name} - {self.location}"
    
    # تمثيل الفرع بطريقة أكثر تفصيلًا
    def __repr__(self):
        return f"Branch('{self.name}', '{self.location}')"

# فئة Person تمثل شخصًا (يمكن أن يكون عميلًا في المكتبة)
class Person:
    def __init__(self, name, age):
        self.name = name  # اسم الشخص
        self.age = age  # عمر الشخص

    # تمثيل النص للشخص
    def __str__(self):
        return f"{self.name}, {self.age} years old"

# فئة Customer تمثل العميل الذي يمكنه استعارة الكتب
# وتورث من فئة Person
class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)  # استدعاء مُنشئ فئة Person
        self.customer_id = customer_id  # تخزين معرف العميل
        self.borrowed_books = []  # قائمة الكتب المستعارة
        self.payment_history = []  # سجل المدفوعات (مثل الغرامات)

    # استعارة كتاب من فرع معين
    def borrow_book(self, book, branch):
        if isinstance(book, Book):
            self.borrowed_books.append(book)
            branch.add_book(book)  # إضافة الكتاب إلى فرع المكتبة
            print(f"{self.name} borrowed {book.title} from {branch.name} branch")
    
    # إعادة كتاب إلى فرع المكتبة
    def return_book(self, book, branch):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title} to {branch.name} branch")
    
    # تقييم الكتاب
    def rate_book(self, book, rating):
        if book in self.borrowed_books:
            print(f"{self.name} rated the book '{book.title}' with {rating} stars")
    
    # دفع غرامة
    def pay_fine(self, amount):
        self.payment_history.append(amount)
        print(f"{self.name} paid a fine of {amount} USD")
    
    # تمثيل النص للعميل
    def __str__(self):
        return f"{super().__str__()} (Customer ID: {self.customer_id})"
    
    # تمثيل العميل بطريقة أكثر تفصيلًا
    def __repr__(self):
        return f"Customer('{self.name}', {self.age}, '{self.customer_id}')"

# فئة BillingSystem تمثل نظام الفواتير الذي يقوم بتوليد الفواتير للعملاء
class BillingSystem:
    @staticmethod
    def generate_invoice(customer, books_borrowed, overdue_days=0):
        total_amount = 0
        # حساب الغرامات بناءً على الأيام المتأخرة
        for book in books_borrowed:
            if overdue_days > 0:
                fine = overdue_days * 1  # فرض غرامة يومية قدرها 1 دولار
                total_amount += fine
        print(f"Invoice for {customer.name}: Total Fine = {total_amount} USD")
        return total_amount

# فئة LibraryManager تدير المكتبة وتوفر وظائف مثل عرض الكتب والعدد الإجمالي لها
class LibraryManager:
    @staticmethod
    def list_books():
        books = Library.get_books()
        if books:
            for book in books:
                print(book.get_details())
        else:
            print("No books available.")
    
    @staticmethod
    def total_books():
        return len(Library.get_books())

# فئة LibraryItem تمثل عنصرًا في المكتبة مع دعم لبعض العمليات مثل الوصول للعنصر وحساب طوله
class LibraryItem:
    def __init__(self, title, type_):
        self.title = title
        self.type = type_  # تحديد نوع العنصر (كتاب، كتاب إلكتروني، الخ)

    # الماجيك ميثود __getitem__ للحصول على العنصر بالترتيب
    def __getitem__(self, index):
        return f"Item {index}: {self.title} ({self.type})"
    
    # الماجيك ميثود __len__ للحصول على طول اسم العنصر
    def __len__(self):
        return len(self.title)

    # تمثيل النص للعنصر
    def __str__(self):
        return f"LibraryItem: {self.title} ({self.type})"
    
    # تمثيل العنصر بطريقة أكثر تفصيلًا
    def __repr__(self):
        return f"LibraryItem('{self.title}', '{self.type}')"

# تطبيق الكود في حالة التشغيل الرئيسية
if __name__ == "__main__":
    # إضافة فروع للمكتبة
    branch1 = Branch("Main Branch", "Downtown")
    branch2 = Branch("East Side Branch", "Eastville")
    
    Library.add_branch(branch1)
    Library.add_branch(branch2)
    
    # إضافة الكتب إلى المكتبة
    book1 = Book("1984", "George Orwell", "123456789", "Dystopian")
    ebook1 = EBook("Digital Fortress", "Dan Brown", "1122334455", "Thriller", 5)
    
    # إضافة الكتب إلى الفروع المختلفة
    branch1.add_book(book1)
    branch2.add_book(ebook1)
    
    # إنشاء عميل جديد
    customer = Customer("John Doe", 30, "C001")
    
    # العميل يستعير كتبًا من فروع مختلفة
    customer.borrow_book(book1, branch1)
    customer.borrow_book(ebook1, branch2)
    
    # العميل يقيم كتابًا
    customer.rate_book(book1, 5)
    
    # عرض جميع الكتب المتاحة في المكتبة
    print("\nBooks in the Library:")
    LibraryManager.list_books()
    
    # العميل يدفع غرامة
    BillingSystem.generate_invoice(customer, [book1, ebook1], overdue_days=3)
    
    # العميل يعيد الكتاب إلى الفرع
    customer.return_book(book1, branch1)
    
    # عرض عدد الكتب الإجمالي في المكتبة
    print("\nTotal books in the library:", LibraryManager.total_books())
    
    # استخدام الماجيك ميثود
    item = LibraryItem("The Catcher in the Rye", "Book")
    print(item[0])  # الوصول للعنصر باستخدام __getitem__
    print(len(item))  # استخدام __len__
    print(item)  # استخدام __str__
    print(repr(item))  # استخدام __repr__
