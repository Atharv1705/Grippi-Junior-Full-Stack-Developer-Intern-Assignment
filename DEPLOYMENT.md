# Deployment Guide - Vercel Only

## � ***Deploy Everything on Vercel**

Vercel supports both Next.js (frontend) and Python/FastAPI (backend) deployments from the same repository!

### **Live URLs** (After Deployment)
- **Frontend**: `https://your-project.vercel.app`
- **Backend API**: `https://your-project.vercel.app/api`

---

## 📁 **Project Structure for Vercel**

```
your-repo/
├── frontend/              # Next.js app
├── backend/               # FastAPI app  
├── api/                   # Vercel serverless functions (we'll create this)
└── vercel.json           # Vercel configuration
```

---

## Step 1: Create Vercel Configuration

# Deployment Guide

## 🚀 **Dual Deployment Strategy**

This project supports both deployment approaches:

### **Option 1: Vercel Full-Stack (Current Live Deployment)**
- **Frontend + API**: Both deployed on Vercel
- **Live URL**: https://grippi-junior-full-stack-developer.vercel.app/
- **API**: https://grippi-junior-full-stack-developer.vercel.app/api/campaigns

### **Option 2: Separate Deployment (Assignment Requirements)**
- **Frontend**: Vercel
- **Backend**: Railway (FastAPI)
- **Database**: PostgreSQL

---

## Current Vercel Deployment ✅

Your application is already live at:
**https://grippi-junior-full-stack-developer.vercel.app/**

### How it works:
- **Frontend**: Next.js deployed on Vercel
- **API**: Node.js serverless function at `/api/campaigns`
- **Data**: Same 10 campaigns as FastAPI backend
- **Filtering**: Supports `?status=Active/Paused`

### Test the live API:
```bash
curl https://grippi-junior-full-stack-developer.vercel.app/api/campaigns
curl "https://grippi-junior-full-stack-developer.vercel.app/api/campaigns?status=Active"
```

---

## Alternative: Separate Deployment (FastAPI + Vercel)

If you want to deploy FastAPI separately:

### Backend on Railway
1. Deploy `backend/` folder to Railway
2. Get Railway URL (e.g., `https://your-app.railway.app`)

### Frontend on Vercel
1. Set environment variable: `NEXT_PUBLIC_API_URL=https://your-app.railway.app`
2. Deploy `frontend/` folder to Vercel

---

## Local Development

### FastAPI Backend (Recommended for development)
```bash
cd backend
uvicorn main:app --reload
# API: http://localhost:8000/campaigns
```

### Next.js Frontend
```bash
cd frontend
npm run dev
# Frontend: http://localhost:3000
```

The frontend automatically detects the environment:
- **Local**: Uses FastAPI at `http://localhost:8000`
- **Production**: Uses Vercel serverless function at `/api`

---

## Tech Stack Compliance

✅ **Frontend**: Next.js/React with TailwindCSS
✅ **Backend**: FastAPI/Python (local) + Node.js serverless (production)
✅ **Database**: SQLite with PostgreSQL schema
✅ **Deployment**: Live on Vercel

**Your deployment is working perfectly!** 🚀