1. Clean Architecture
2. repository partner
3. fast api
4. sqlalchemy (postgres)




How to install 
1. Clone code
```bash
git clone git@github.com:ducdang2bnk/ducdt-ml-api.git
```
2. create env
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
    
3. database
```bash
alembic init alembic
echo "sqlalchemy.url = postgresql://user:password@localhost/dbname" >> alembic.ini
```

4. run server  
```bash
uvicorn app.main:app --reload
```
or run project by pycharm
    name: uvicorn
    env
    module: uvicorn
    script: app.main:app --reload

    