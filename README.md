# 🍽️ Smart Canteen Ordering System

A full-stack web application that allows users to browse menu items, place food orders, and manage canteen operations efficiently. This system is designed to provide a smooth and fast ordering experience similar to platforms like Swiggy or Zomato.

---

## 🚀 Features

### 👨‍🍳 User Side

* View menu items with images, prices, and descriptions
* Add items to cart
* Place orders easily
* Responsive and user-friendly UI

### 🛠️ Admin / Backend

* Manage menu items
* Handle customer orders
* Store and retrieve data using SQL database
* REST API integration

---

## 🏗️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python (Flask)

### Database

* MySQL / PostgreSQL (SQL-based database)

---

## 📁 Project Structure

```
smart-canteen/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   └── routes/
│       ├── auth.py
│       ├── menu.py
│       └── orders.py
│
├── frontend/
│   ├── index.html
│   ├── menu.html
│   ├── cart.html
│   └── styles.css
│
├── database/
│   └── schema.sql
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/smart-canteen.git
cd smart-canteen
```

### 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### 3️⃣ Configure Database

* Install MySQL/PostgreSQL
* Create a database
* Run `schema.sql` to create tables
* Update database credentials in `db.py`

### 4️⃣ Run Backend Server

```bash
python app.py
```

Server will run at:

```
http://127.0.0.1:5000
```

### 5️⃣ Open Frontend

* Open `frontend/index.html` in browser
  OR
* Use Live Server (VS Code)

---

## 🔗 API Endpoints

### 📌 Menu

* `GET /menu` → Fetch all items

### 📌 Orders

* `POST /order` → Place order

### 📌 Auth (Optional)

* `POST /register`
* `POST /login`

---

## 🍔 Sample Menu Items

* Chicken Biryani
* Veg Biryani
* Egg Biryani
* Noodles
* Fried Rice
* Manchurian
* Snacks & Beverages

---

## 🎯 Future Enhancements

* Payment integration (UPI / Razorpay)
* Order tracking system
* Admin dashboard
* Mobile app version
* AI-based food recommendations

---

## 📌 Use Case

This project is ideal for:

* College canteens
* Small restaurants
* Food court systems
* Student projects (Full Stack / Data Science)

---

## 👨‍💻 Author

**Shaik Thouhid Hussain**
📧 [shaikthouhid2434@gmail.com](mailto:shaikthouhid2434@gmail.com)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
