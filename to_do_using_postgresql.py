import psycopg2
conn =  psycopg2.connect(
   
   host = "localhost",
   user = "postgres",
   password = "trisha123",
   port = 5432,
   database =  "postgres"
)
welcome = "-------WELCOME TO TODO LIST APP------------------------"
print(welcome)
def create_table():
    with  conn.cursor() as  cursor:
        cursor.execute("create table if not exists to_do(id serial primary key,task TEXT,status boolean default false);")
create_table()
def add_tasks(task):
    with  conn.cursor()  as cursor:
        cursor.execute("insert into to_do(task) values(%s);",(task,))
def view_all():
    with conn.cursor() as cursor:
        cursor.execute("select * from to_do;")
        row  = cursor.fetchall()
        for r in row:
            status =  "✅ Done" if r[2] else "❌ Not Done"
            print(f"{r[0]}   {r[1]}  {status}")
def mark_done(title):
    with conn.cursor() as cursor:
        cursor.execute("update to_do set status = TRUE where task = (%s);",(title,))
        print(f"congrats for completing {title}")

menu = """
1.Add a task

2.mark a task as completed

3.view all tasks



"""

while (user_input := input(menu)) != "4":
    if user_input == "1":
        task = input("enter a task to enter:")
        add_tasks(task)
        print("task added successfully")
    elif user_input == "2":
        title = input("enter a task to mark it as completed")
        mark_done(title)
    elif user_input == "3":
        view_all()
    else :
        print("invalid input!! please try again")



conn.commit()
conn.close()