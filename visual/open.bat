set ppath="C:\Users\Joseph CP\AppData\Local\Programs\Python\Python312\python.exe"
%ppath% -m venv env
call env\Scripts\activate.bat
pip install -r requirements.txt
python vis.py   
:: pip install --upgrade pip
:: pip install --force-reinstall --no-cache-dir --upgrade -r requirements.txt
:: jupyter lab