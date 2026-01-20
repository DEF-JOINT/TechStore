import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import {
  ShoppingBag,
  Smartphone,
  Laptop,
  Headphones,
  Shield,
  Truck,
  CreditCard
} from 'lucide-react';
import Hero from '../components/Home/Hero';
import ProductCarousel from '../components/Home/ProductCarousel';
import CategoryGrid from '../components/Home/CategoryGrid';
import Features from '../components/Home/Features';

const HomePage: React.FC = () => {
  const categories = [
    { id: 1, name: 'Смартфоны', icon: Smartphone, count: 45, image: '/images/categories/smartphones.jpg' },
    { id: 2, name: 'Ноутбуки', icon: Laptop, count: 32, image: '/images/categories/laptops.jpg' },
    { id: 3, name: 'Наушники', icon: Headphones, count: 28, image: '/images/categories/headphones.jpg' },
    { id: 4, name: 'Умные часы', icon: ShoppingBag, count: 19, image: '/images/categories/smartwatches.jpg' },
  ];

  const features = [
    {
      icon: Truck,
      title: 'Бесплатная доставка',
      description: 'При заказе от $50'
    },
    {
      icon: Shield,
      title: 'Гарантия 2 года',
      description: 'На всю технику'
    },
    {
      icon: CreditCard,
      title: 'Удобная оплата',
      description: 'Картой или криптовалютой'
    }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <Hero />

      {/* Categories */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">
            Популярные категории
          </h2>
          <CategoryGrid categories={categories} />
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <div className="flex justify-between items-center mb-12">
            <h2 className="text-3xl font-bold">Новинки</h2>
            <Link
              to="/products"
              className="text-blue-600 hover:text-blue-800 font-semibold"
            >
              Смотреть все →
            </Link>
          </div>
          <ProductCarousel />
        </div>
      </section>

      {/* Features */}
      <section className="py-16 bg-gradient-to-r from-blue-50 to-indigo-50">
        <div className="container mx-auto px-4">
          <Features features={features} />
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-blue-600 to-indigo-600 text-white">
        <div className="container mx-auto px-4 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-4xl font-bold mb-4">
              Готовы обновить свои гаджеты?
            </h2>
            <p className="text-xl mb-8 opacity-90">
              Присоединяйтесь к тысячам довольных клиентов
            </p>
            <Link
              to="/products"
              className="inline-block bg-white text-blue-600 px-8 py-4 rounded-lg font-bold text-lg hover:bg-gray-100 transition-colors duration-300"
            >
              Начать покупки
            </Link>
          </motion.div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
