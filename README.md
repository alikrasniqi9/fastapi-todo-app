## Screenshot

![App Screenshot](screenshot.png)

Modern full-stack inventory/product management app built with FastAPI and React.

## Features

- Create products
- Update products
- Delete products
- Search products
- Sort products
- Responsive modern UI
- FastAPI REST API
- SQLite database
- React frontend

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite

### Frontend
- React
- Axios
- CSS


## Backend Setup

```bash
cd backend

python -m venv .venv
```

Activate venv:

### Windows
```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs on:

```text
http://localhost:3000
```

---

## API Routes

| Method | Route | Description |
|---|---|---|
| GET | /products | Get all products |
| GET | /products/{id} | Get product by id |
| POST | /products | Create product |
| PUT | /products/{id} | Update product |
| DELETE | /products/{id} | Delete product |

---

## Author

Ali Krasniqi