# Library-Management-System
This is a library management system programmed through Python and MySQL.

Frontend.py: the frontend part of the system.
Backend.py: the backend part of the system.

How to run?
1. Make sure you have already installed Python and MySQL
2. Install Tkinter, mysql.connector, installer libraries of Python.
3. Create a database called "test" by root user of MySQL.
4. Open backend.py, find the following part of code:
    conn=mysql.connector.connect(
    host="localhost",        
    user="root",               
    passwd="12345678",       //here should be your own password of MySQL root user
    database="test"
    )
    
   Set passwd variable to be your password of MySQL root user. All of the data created or modified by GUI will be recorded in the "test" database in MySQL.
   
5. Use the following command to create .exe file
    pyinstaller --onefile --windowed frontend.py
    
6. Click the .exe file, and the program will run.
