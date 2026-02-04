#!/bin/bash

echo "Setting up Grippi Campaign Analytics Dashboard"

# Backend setup
echo "Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
echo "Backend dependencies installed"

# Frontend setup
echo " Setting up frontend..."
cd ../frontend
npm install
cp .env.example .env.local
echo "Frontend dependencies installed"

echo "Setup complete!"
echo ""
echo "To start development:"
echo "1. Backend: cd backend && uvicorn main:app --reload"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "Visit http://localhost:3000 to see the dashboard"