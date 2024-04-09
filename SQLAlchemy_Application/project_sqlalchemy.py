
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    cpf = Column(String(11), unique=True)
    endereco = Column(String, unique=True)

    conta = relationship("Conta", back_populates="cliente", cascade="all, delete-orphan")

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_conta = Column(String, default="conta corrente")
    agencia = Column(String)
    num = Column(String)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    saldo = Column(Float)

    cliente = relationship("Cliente", back_populates="conta") 

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

with Session(engine) as session:
    manuel = Cliente(
        name='Manuel',
        cpf='01234567890',
        endereco='Rua ABC',
        conta=[Conta(tipo_conta="Poupança", agencia="0000", num="0000000 - 1", saldo= "1000")]
    )
    
    fernanda = Cliente(
        name='Fernanda',
        cpf='09876543210',
        endereco='Rua XYZ',
        conta=[Conta(tipo_conta="Salário", agencia="0001", num="0000000 - 2", saldo= "7520")]
    )
    
    claudio = Cliente(
        name='Claudio',
        cpf='74102589632',
        endereco='Rua VVSVB',
        conta=[Conta(tipo_conta="Corrente", agencia="0003", num="0000000 - 3", saldo= "45000")]
    )
    
    session.add_all([manuel, fernanda, claudio])
    session.commit()
    

stmt = select(Cliente).where(Cliente.name.in_(["Manuel"]))
for user in session.scalars(stmt):
    print(user.name, user.cpf, user.endereco)
    
    
stmt_join = select(Cliente.name, Conta.saldo).join_from(Cliente, Conta)
results = session.execute(stmt_join).fetchall()
for result in results:
    print(result)
        

