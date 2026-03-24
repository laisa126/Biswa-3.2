# IN16 Study Manager 🎓

A full-featured Django class management app for IN16 Software Engineering students.  
Login · Notes · Units · Groups · Class List · Announcements · Reminders · Dark Mode

---

## Features

- 🔐 Register / Login with student profile (reg number, gender)
- 📚 Units with note & group counts
- 📝 Per-unit notes with full-detail view
- 👥 Study groups with member listings
- 🎓 Full class list with search & gender filter
- 📣 Announcements board
- ⏰ Personal study reminders
- 🌙 Dark mode toggle
- 📱 Fully responsive (Bootstrap 5)
- ⚙️ Django Admin panel

---

## 🚀 Deploy to Vercel (Step-by-Step)

### 1. Push to GitHub

```bash
cd biswa_deploy
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/biswa-class-manager.git
git push -u origin main
```

### 2. Import to Vercel

1. Go to [vercel.com](https://vercel.com) → **Add New → Project**
2. Import your GitHub repository
3. Vercel auto-detects the `vercel.json` — no framework preset needed
4. Click **Deploy** (the first deploy may fail until env vars are set — that is expected)

### 3. Set Environment Variables

In Vercel → Project → **Settings → Environment Variables**, add:

| Variable | Value |
|---|---|
| `SECRET_KEY` | Any random 50+ character string |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*` |
| `DATABASE_URL` | `postgresql://postgres.sgqypmhvoljfdbzpldka:Nabiswa1james@aws-1-eu-west-1.pooler.supabase.com:6543/postgres` |
| `CSRF_TRUSTED_ORIGINS` | `https://YOUR-PROJECT.vercel.app` |

> After setting the variables, go to **Deployments → Redeploy** to pick them up.

### 4. Run migrations (once, before first use)

Vercel lambdas can't run `migrate` at startup, so run it once from your local machine:

```bash
# In the project directory, with your .env file populated:
export DATABASE_URL="postgresql://postgres.sgqypmhvoljfdbzpldka:Nabiswa1james@aws-1-eu-west-1.pooler.supabase.com:5432/postgres"
python manage.py migrate
```

### 5. Seed the database (optional but recommended)

```bash
python manage.py seed
```

### 6. Your app is live

- App: `https://YOUR-PROJECT.vercel.app`
- Admin: `https://YOUR-PROJECT.vercel.app/admin/` → `admin / admin123`
- Student login: `kevinkiptoo / pass1234`

---

## 💻 Run Locally

```bash
# 1. Clone and enter project
git clone https://github.com/YOUR_USERNAME/biswa-class-manager.git
cd biswa-class-manager

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create local .env (SQLite used if no DATABASE_URL)
cp .env.example .env

# 5. Run migrations
python manage.py migrate

# 6. Seed sample data
python manage.py seed

# 7. Collect static files
python manage.py collectstatic --noinput

# 8. Start server
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## 🗂️ Project Structure

```
biswa_deploy/
├── api/
│   └── index.py              ← Vercel serverless entry point
├── vercel.json               ← Vercel build + routing config
├── build_files.sh            ← Runs collectstatic at Vercel build time
├── requirements.txt          ← Django, psycopg2, dj-database-url, whitenoise
├── manage.py
├── seed_data.py
├── .env                      ← Local env vars (DO NOT COMMIT)
├── .env.example              ← Safe-to-commit template
├── .gitignore
├── IN16_Study_Manager/
│   ├── settings.py           ← Production-ready settings
│   ├── urls.py
│   └── wsgi.py
└── notes_app/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── admin.py
    ├── management/
    │   └── commands/
    │       └── seed.py       ← python manage.py seed [--clear]
    └── templates/
        └── notes_app/        ← All 11 HTML templates
```

---

## How the Vercel deployment works

| Phase | What happens |
|---|---|
| **Build** | Vercel runs `build_files.sh` → installs packages → runs `collectstatic` |
| **Deploy** | `api/index.py` is packaged as a Python serverless lambda |
| **Request** | All routes → `api/index.py` → Django WSGI app |
| **Static files** | WhiteNoise middleware intercepts `/static/*` and serves from `staticfiles/` |
| **Database** | Supabase PostgreSQL via connection pooling (port 6543) |

---

## Default Credentials

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| Student | `kevinkiptoo` | `pass1234` |
| Student | `lynettechepkemoi` | `pass1234` |

> Change the admin password immediately after first login in production.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5 |
| Frontend | Bootstrap 5.3 + Bootstrap Icons |
| Fonts | Sora + JetBrains Mono (Google Fonts) |
| Database | PostgreSQL (Supabase) / SQLite (local) |
| Static files | WhiteNoise |
| Hosting | Vercel (Python serverless) |
| Auth | Django built-in |
