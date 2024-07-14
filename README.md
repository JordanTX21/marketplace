# Setup


# Backend
```
py -m venv env
```
```
cd services/backend
```
```
cp .env.example .env
```
```
env\Scripts\activate
```
```
py -m pip install -r requirements.txt
```
```
uvicorn src.main:app --reload
```

# Frontend
```
cd services/frontend
```
```
npm install
```
```
npm run dev
```
```
npm run build
```