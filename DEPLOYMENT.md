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

# Deployment Guide - Vercel Only

## 🚀 **Deploy Everything on Vercel**

Vercel supports both Next.js (frontend) and Python serverless functions (backend API) from the same repository!

### **Live URLs** (After Deployment)
- **Frontend**: `https://your-project.vercel.app`
- **Backend API**: `https://your-project.vercel.app/api/campaigns`

---

## 📁 **Project Structure for Vercel**

```
your-repo/
├── frontend/              # Next.js app
├── backend/               # Original FastAPI (for local dev)
├── api/                   # Vercel serverless functions
│   └── campaigns.py       # API endpoint
├── vercel.json           # Vercel configuration
└── README.md
```

---

## Step 1: Files Already Created ✅

The following files have been created for Vercel deployment:

### `vercel.json` - Vercel Configuration
```json
{
  "buildCommand": "cd frontend && npm run build",
  "outputDirectory": "frontend/.next",
  "framework": "nextjs",
  "functions": {
    "api/campaigns.py": {
      "runtime": "python3.9"
    }
  }
}
```

### `api/campaigns.py` - Serverless API Function
- Contains the same 10 sample campaigns
- Supports status filtering with `?status=Active`
- CORS enabled for frontend communication

### Frontend Updated
- API URL changed to use `/api` (Vercel serverless functions)
- No other changes needed

---

## Step 2: Deploy to Vercel

### Option A: Deploy via Vercel Dashboard (Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "feat: ready for Vercel deployment"
   git push origin main
   ```

2. **Deploy on Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - **Important**: Set **Root Directory** to `frontend`
   - Click "Deploy"

3. **Vercel will automatically**:
   - Build the Next.js frontend
   - Deploy the Python API functions
   - Provide you with a live URL

### Option B: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from project root
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name: grippi-dashboard
# - Directory: ./frontend
```

---

## Step 3: Test Your Deployment

### Test API Endpoints
```bash
# Replace with your actual Vercel URL
curl https://your-project.vercel.app/api/campaigns
curl "https://your-project.vercel.app/api/campaigns?status=Active"
```

### Test Frontend
1. Visit your Vercel URL
2. Verify campaign table loads
3. Test status filtering dropdown
4. Check responsive design

---

## Step 4: Environment Variables (Optional)

If you need environment variables:

1. Go to Vercel Dashboard
2. Select your project
3. Go to Settings → Environment Variables
4. Add any needed variables

For this project, no additional environment variables are needed since the API is now internal.

---

## 🎯 **Advantages of Vercel-Only Deployment**

### ✅ **Simplified Deployment**
- Single platform for everything
- No need to manage multiple services
- Automatic HTTPS and CDN

### ✅ **Serverless Backend**
- Python functions scale automatically
- No server management needed
- Pay only for usage

### ✅ **Integrated Frontend + Backend**
- Same domain for API and frontend
- No CORS issues
- Faster API calls (same server)

---

## 🔧 **Local Development**

You can still run locally for development:

### Option 1: Use Vercel Dev (Recommended)
```bash
# Install Vercel CLI
npm i -g vercel

# Run local development with serverless functions
vercel dev
```

### Option 2: Use Original FastAPI
```bash
# Terminal 1: Backend
cd backend
uvicorn main:app --reload

# Terminal 2: Frontend  
cd frontend
npm run dev
```

---

## 📋 **Deployment Checklist**

- [ ] All code committed to Git
- [ ] Repository pushed to GitHub
- [ ] `vercel.json` configuration file created
- [ ] `api/campaigns.py` serverless function created
- [ ] Frontend updated to use `/api` endpoint
- [ ] Deployed to Vercel
- [ ] Live URL working
- [ ] API endpoints responding
- [ ] Frontend functionality tested

---

## 🎉 **You're Done!**

Your Campaign Analytics Dashboard is now live on Vercel with:
- ✅ Next.js frontend
- ✅ Python serverless API
- ✅ 10 sample campaigns
- ✅ Status filtering
- ✅ Professional UI
- ✅ Single URL for everything

**Share your live Vercel URL for evaluation!** 🚀