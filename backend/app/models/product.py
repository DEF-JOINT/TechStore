from sqlalchemy import Column, String, Text, Numeric, Integer, Boolean, JSON, UUID, ForeignKey
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base, TimestampMixin

class Product(Base, TimestampMixin):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sku = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    category = Column(String(100), nullable=False)  # smartphone, laptop, etc.
    brand = Column(String(100))
    price = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(3), default="USD")
    stock_quantity = Column(Integer, default=0)
    specifications = Column(JSON)  # {"ram": "8GB", "storage": "256GB", ...}
    images = Column(JSON)  # ["image1.jpg", "image2.jpg"]
    is_active = Column(Boolean, default=True)
    rating = Column(Numeric(3, 2), default=0.0)
    review_count = Column(Integer, default=0)

    # Связи
    cart_items = relationship("CartItem", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")

    def __repr__(self):
        return f"<Product {self.name}>"

class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("product_categories.id"))

    parent = relationship("ProductCategory", remote_side=[id], backref="children")

    def __repr__(self):
        return f"<Category {self.name}>"
