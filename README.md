# 🧠 HNG13 Backend — Stage 0 Task

### 🔹 Description
A simple Flask REST API that returns my profile details and a random cat fact fetched dynamically from the **Cat Facts API**.

---

### ⚙️ Endpoint
**GET** `/me`

Example:
```
https://your-app-url.onrailway.app/me
```

---

### 🧾 Example Response
```json
{
  "status": "success",
  "user": {
    "email": "samuelfikayomi08@gmail.com",
    "name": "Samuel Oluwafikunayomi",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-19T18:45:00.000Z",
  "fact": "Cats sleep for 70% of their lives."
}
```

---

### 🚀 How to Run Locally
1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd backend-stage0
   ```
2. Create virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Windows: venv\Scripts\activate)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Visit:  
   [http://127.0.0.1:5000/me](http://127.0.0.1:5000/me)

---

### 🌐 Deploy on Railway
1. Push your code to GitHub.
2. Go to [https://railway.app](https://railway.app)
3. Click **New Project → Deploy from GitHub Repo**
4. Select this repo and wait for Railway to build & deploy.
5. Copy your live endpoint URL and test with `/me`

---

### 🧠 Author
**Name:** Samuel Oluwafikunayomi  
**Email:** samuelfikayomi08@gmail.com  
**Stack:** Python/Flask  
**HNG Track:** Backend (Stage 0)

---

### ✅ Submission
In the `#track-backend` Slack channel, run:
```
/stage-zero-backend
```
Then submit:
- **Server URL:** your deployed `/me` endpoint  
- **GitHub Repo:** your repo link  
- **Full Name:** Samuel Oluwafikunayomi  
- **Email:** samuelfikayomi08@gmail.com  
- **Stack:** Python/Flask
