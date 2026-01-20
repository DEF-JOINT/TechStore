from sqlalchemy import Column, String, Boolean, Enum, UUID, ForeignKey
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base, TimestampMixin
from app.schemas.user import UserRole

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)

    # Связи
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user")
    cart = relationship("Cart", back_populates="user", uselist=False)

    def __repr__(self):
        return f"<User {self.email}>"

class Address(Base, TimestampMixin):
    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    street = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100))
    country = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    is_default = Column(Boolean, default=False)
    phone_number = Column(String(20))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"<Address {self.city}, {self.country}>"
