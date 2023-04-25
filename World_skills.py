from tkinter import *
from tkinter.messagebox import showinfo, showerror
import numpy
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import pandas as pd


def check_data():
    if not vendor.get().isdigit():
        showerror(title="Ошибка", message="Неверный формат vendor_id")
        return False
    if not passenger_count.get().isdigit():
        showerror(title="Ошибка", message="Неверный формат ввода passenger_count")
        return False
    return True


def learning_algo(data):
    result = pd.read_csv("data.csv", index_col='Unnamed: 0')
    result = result.drop('seconds', axis=1)
    X_df = result.drop('trip_duration', axis=1)
    y = result['trip_duration']
    X_train, X_valid, y_train, y_valid = train_test_split(X_df, y, test_size=0.2, random_state=42)
    clf_lasso = Lasso(alpha=0.01).fit(X_train, y_train)
    res = pd.DataFrame([data], columns=['vendor_id', 'passenger_count', 'maximum temperature', 'maximum temperature',
                                        'average temperature', 'pickup_month', 'pickup_day', 'length_way', 'Cluster'])
    return clf_lasso.predict(res)


def predict(event):
    global prediction_data
    prediction_data.config(text='')
    if not check_data():
        return

    prediction_label = Label(master, text="Предсказанное время поездки")
    prediction_label.pack()
    prediction_data.place(x=450, y=20)

    data = [vendor.get(), passenger_count.get(), max_temp.get(), min_temp.get(), avr_temp.get(),
            pickup_day.get(), pickup_month.get(), length_way.get(), cluster.get()]

    data = numpy .array(list(map(float, data)))
    print(data)
    result = int(learning_algo(data)[0])
    print(result)
    prediction_data.config(text=result, font=("Arial", 25), background="black", fg="red")

    with open("prediction.txt", mode='w') as file:
        file.write(str(result))


def info(event):
    showinfo(title="правка о командах", message="Данное сообщение является спавкой о ключевых команда.\n"
             "Вы можете вводить данные призанков, а также получать результаты\n"
             " отдельном файле. Вводите только корректную инфу")


master = Tk()
master.title("Сессия 4")
master.geometry("700x500")
master.resizable(False, False)
#  master.mainloop()
label_data = Label(master, text="Введите необходимые данные")
label_data.pack()
label_data.place(x=10, y=10)

label_vendor = Label(master, text="vendor_id")
label_vendor.pack()
label_vendor.place(x=20, y=40)
vendor = Entry()
vendor.pack()
vendor.place(x=20, y=60)

label_passenger_count = Label(master, text="passenger_count")
label_passenger_count.pack()
label_passenger_count.place(x=20, y=100)
passenger_count = Entry()
passenger_count.pack()
passenger_count.place(x=20, y=120)

label_max_temp = Label(master, text="max_temp")
label_max_temp.pack()
label_max_temp.place(x=20, y=220)
max_temp = Entry()
max_temp.pack()
max_temp.place(x=20, y=240)

label_min_temp = Label(master, text="min_temp")
label_min_temp.pack()
label_min_temp.place(x=20, y=280)
min_temp = Entry()
min_temp.pack()
min_temp.place(x=20, y=300)

label_avr_temp = Label(master, text="avr_temp")
label_avr_temp.pack()
label_avr_temp.place(x=280, y=40)
avr_temp = Entry()
avr_temp.pack()
avr_temp.place(x=280, y=60)

label_pickup_month = Label(master, text="pickup_month")
label_pickup_month.pack()
label_pickup_month.place(x=280, y=100)
pickup_month = Entry()
pickup_month.pack()
pickup_month.place(x=280, y=120)

label_pickup_day = Label(master, text="pickup_day")
label_pickup_day.pack()
label_pickup_day.place(x=280, y=160)
pickup_day = Entry()
pickup_day.pack()
pickup_day.place(x=280, y=180)

label_length_way = Label(master, text="length_way")
label_length_way.pack()
label_length_way.place(x=280, y=220)
length_way = Entry()
length_way.pack()
length_way.place(x=280, y=240)

label_cluster = Label(master, text="cluster")
label_cluster.pack()
label_cluster.place(x=280, y=280)
cluster = Entry()
cluster.pack()
cluster.place(x=280, y=300)

prediction_data = Label(master, text="")
prediction_data.pack()
prediction_data.place(x=450, y=60)

help_btn = Button(text="Справка",
                  width=15, height=3)
help_btn.pack()
help_btn.place(x=520, y=350)

predict_btn = Button(text="Спрогнозировать",
                  width=15, height=3)
predict_btn.pack()
predict_btn.place(x=20, y=350)

predict_btn.bind('<Button-1>', predict)
help_btn.bind('<Button-1>', info)

master.mainloop()



