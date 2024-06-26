from sqlalchemy import *
import sqlalchemy.orm as orm

Base = orm.declarative_base()

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)


class Client(Base):
    __tablename__ = "client_account"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String[11], nullable=False)
    address = Column(String[30])
    account = orm.relationship("Conta",
                               back_populates="cliente",
                               cascade="all, delete-orphan")

    def __repr__(self):
        return (f"Client(id = {self.id}, name={self.name}, " +
                f"cpf={self.cpf}, address={self.address})")


class Conta(Base):
    __tablename__ = "conta_account"
    id = Column(Integer, primary_key=True)
    kind = Column(String)
    agency = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    id_client = Column(Integer,
                       ForeignKey("client_account.id"),
                       nullable=False)
    saldo = Column(DECIMAL, nullable=False)
    cliente = orm.relationship("Client", back_populates="account")

    def __repr__(self):
        return (f"Conta(id = {self.id}, kind={self.kind}, " +
                f"agency={self.agency}, number={self.number})," +
                f"id_client={self.id_client}, saldo={self.saldo}")


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

with orm.Session(engine) as session:
    lucas = Client(name="Lukas Maximo",
                   cpf="09107813465",
                   address="lukasmaximo@gmail.com",
                   account=[
                       Conta(kind="Conta Corrente",
                             agency="001",
                             number=55,
                             saldo=10.50),
                       Conta(kind="Poupança",
                             agency="001",
                             number=51,
                             saldo=750.50)
                   ])
    sam = Client(name="Samuel Tarly",
                 cpf="00999090123",
                 address="samtarly@thunderbird.com",
                 account=[
                     Conta(kind="Conta Corrente",
                           agency="002",
                           number=55,
                           saldo=200.00),
                     Conta(kind="Conta Corrente",
                           agency="001",
                           number=51,
                           saldo=400.00)
                 ])
    patrick = Client(name="Patrick Star",
                     cpf="01012343210",
                     address="patrickhighstar@yahoo.com.br",
                     account=[
                         Conta(kind="Conta Corrente",
                               agency="002",
                               number=55,
                               saldo=300.00),
                         Conta(kind="Cheque Especial",
                               agency="002",
                               number=13,
                               saldo=1000000000.00)
                     ])

    session.add_all([lucas, sam, patrick])
    session.commit()

stat = select(Client)
print(stat)

for line in session.scalars(stat):
    print(line)

stat2 = select(Conta)
for line in session.scalars(stat2):
    print(line)

stat3 = select(Client, Conta).join_from(Conta, Client)
print(stat3)
conn = engine.connect()
results = conn.execute(stat3).fetchall()
for result in results:
    print(result)
