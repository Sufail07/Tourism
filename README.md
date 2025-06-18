
# 🌍 Tourism Web App

**Tourism** is a full-stack travel application built with **Django**, **Django REST Framework (DRF)**, and a Bootstrap-based frontend. It allows users to **create, view, update, and delete travel destinations**, upload images, and add map links to each location.

This app can be used to maintain a personal travel log, power a small-scale tourism site, or serve as a portfolio project for Django and REST API development. ✈️🧳

---

## ✨ Features

- ➕ Add new travel destinations  
- 🖼️ Upload photos for each destination  
- 🗺️ Include Google Maps links  
- 🔄 Full CRUD operations (Create, Read, Update, Delete)  
- 🌐 RESTful API with DRF  
- 💻 Responsive and mobile-friendly design using Bootstrap  

---

## 🛠️ Tech Stack

### Backend
- 🐍 Django (`Tourism` project)
- 🔗 Django REST Framework (DRF)
- 📁 App name: `core`

### Frontend
- 🧱 HTML5
- 🎨 CSS3
- 🅱️ Bootstrap 5

### Database
- 🛢️ SQLite (can be replaced with PostgreSQL, MySQL, etc.)

### Media
- 🖼️ Image upload using Django `MEDIA` configuration

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sufail07/Tourism.git
cd Tourism
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

📍 Visit `http://127.0.0.1:8000/destinations/` in your browser to access the site.

---

## 🔗 URL Patterns

### 🔹 API Endpoints (`/api/`)

| Method | Endpoint               | Description                  |
| ------ | ---------------------- | ---------------------------- |
| GET    | `/api/list`            | List all destinations        |
| POST   | `/api/create`          | Create a new destination     |
| GET    | `/api/<int:pk>`        | Retrieve a destination by ID |
| PUT    | `/api/<int:pk>/update` | Update a destination         |
| DELETE | `/api/<int:pk>/delete` | Delete a destination         |

### 🔸 Frontend Routes (`/destinations/`)

| URL                             |  Description                  |
| ------------------------------- |  ---------------------------- |
| `/destinations/`                |  View all destinations        |
| `/destinations/create`          |  Add a new destination        |
| `/destinations/<int:pk>`        |  View a specific destination  |
| `/destinations/<int:pk>/update` |  Edit an existing destination |
| `/destinations/<int:pk>/delete` |  Delete a destination         |

---

## 📁 Project Structure

```
Tourism/
├── core/                   # Main app (models, views, urls, serializers)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── Tourism/                # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/              # HTML templates
├── static/                 # Static CSS/JS/images
├── media/                  # Uploaded images
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo 🍴
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add new feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request ✅

---


Made with ❤️ by [@Sufail07](https://github.com/Sufail07)

```
