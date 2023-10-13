#!/usr/bin/env python
# coding: utf-8


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

def add_chess_t(save = True):
    value = ent_chess_t.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['chess_training']+=int(value)
            lbl_chess_t2['text'] = data['chess_training']
            ent_chess_t.delete(0, tk.END)
        else:
            errors.append("chess training")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for chess trainig. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)

def add_chess_g(save = True):
    value = ent_chess_g.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['chess_games']+=int(value)
            lbl_chess_g2['text'] = data['chess_games']
            ent_chess_g.delete(0, tk.END)
        else:
            errors.append("chess games")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for chess games. Please enter a valid value.")
            with open("Jawor_TGoL.txt", "w") as file:
                json.dump(data, file)
    
def add_spanish_t(save = True):
    value = ent_spanish_t.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['spanish_talking']+=int(value)
            lbl_spanish_t2['text'] = data['spanish_talking']
            ent_spanish_t.delete(0, tk.END)
        else:
            errors.append("spanish talking")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for spanish talking. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)

def add_learning_s_w(save = True):
    value = ent_learning_s_w.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['learning_spanish_words']+=int(value)
            lbl_learning_s_w2['text'] = data['learning_spanish_words']
            ent_learning_s_w.delete(0, tk.END)
        else:
            errors.append("learning spanish words")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for learning spanish words. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)
    
def add_intense_s_l(save = True):
    value = ent_intense_s_l.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['intense_spanish_learning']+=int(value)
            lbl_intense_s_l2['text'] = data['intense_spanish_learning']
            ent_intense_s_l.delete(0, tk.END)
        else:
            errors.append("intense spanish learning")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for intense spanish learning. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)
    
def add_euros(save = True):
    value = ent_euros.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['euros_earned']+=int(value)
            lbl_euros2['text'] = data['euros_earned']
            ent_euros.delete(0, tk.END)
        else:
            errors.append("euros earned")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for euros earned. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)
    
def add_juggling_t(save = True):
    value = ent_juggling_t.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['juggling_training']+=int(ent_juggling_t.get())
            lbl_juggling_t2['text'] = data['juggling_training']
            ent_juggling_t.delete(0, tk.END)
        else:
            errors.append("juggling training")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for juggling training. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)
    
def add_books(save = True):
    value = ent_books.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['books']+=int(value)
            lbl_books2['text'] = data['books']
            ent_books.delete(0, tk.END)
        else:
            errors.append("books")
        if save:
            if errors:
                errors.clear()
                messagebox.showerror("Error", "Invalid input for books. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)
    
def add_running(save = True):
    value = ent_running.get()
    if not value:
        pass
    else:
        if value.isdigit():
            data['running']+=int(value)
            lbl_running2['text'] = data['running']
            ent_running.delete(0, tk.END)
        else:
            errors.append("running")
        if save:
            if errors:
                errors.clear
                messagebox.showerror("Error", "Invalid input for running. Please enter a valid value.")
            else:
                with open("Jawor_TGoL.txt", "w") as file:
                    json.dump(data, file)
    
def save_fasting(event=None, save = True):
    data['fasting']=1 if combobox.get()=="Yes" else 0
    if save:
        with open("Jawor_TGoL.txt", "w") as file:
            json.dump(data, file)

def reset_all():
    data["chess_training"]=0
    data["chess_games"]=0
    data["spanish_talking"]=0
    data["learning_spanish_words"]=0
    data["intense_spanish_learning"]=0
    data["euros_earned"]=0
    data["juggling_training"]=0
    data["books"]=0
    data["running"]=0
    data["fasting"]=0
    lbl_chess_t2['text'] = 0
    lbl_chess_g2['text'] = 0
    lbl_spanish_t2['text'] = 0
    lbl_learning_s_w2['text'] = 0
    lbl_intense_s_l2['text'] = 0
    lbl_euros2['text'] = 0
    lbl_juggling_t2['text'] = 0
    lbl_books2['text'] = 0
    lbl_running2['text'] = 0
    combobox.set("No")
    
def add_all():
    add_chess_t(save = False)
    add_chess_g(save = False)
    add_spanish_t(save = False)
    add_learning_s_w(save = False)
    add_intense_s_l(save = False)
    add_euros(save = False)
    add_juggling_t(save = False)
    add_books(save = False)
    add_running(save = False)
    with open("Jawor_TGoL.txt", "w") as file:
        json.dump(data, file)
    if errors:
        errors_str = f"Invalid input for {errors[0]}"
        for error in errors[1:]:
            errors_str += ', '+error
        errors_str +=". Please enter a valid value."
        errors.clear()
        messagebox.showerror("Error", errors_str)
    else:
        return True
    
def quit():
    window.destroy()

def submit():
    if add_all():
        cur_chess = int(data["chess_training"]/10 + data["chess_games"])
        cur_spanish = int(data["spanish_talking"]*5/6 + data["learning_spanish_words"]*2/15 + data["intense_spanish_learning"]/10)
        cur_juggling = int(data["euros_earned"] + data["juggling_training"]/10)
        exp_sum = int(cur_chess+cur_spanish+cur_juggling+data['books']*30+data['running'])
        if data["fasting"]:
            exp_sum += 10
        data['remained_exp'] = data["remained_exp"]+exp_sum
        lvl_promotion = False
        out_lvl = f"lvl : {data['lvl']}"
        while data["remained_exp"] >= 50*data["lvl"]+100:
            data["remained_exp"] = round(data["remained_exp"]-50*data["lvl"]-100, 1)
            data["lvl"] += 1
            lvl_promotion = True

        frame_top.destroy()
        frame_bottom.destroy()
        empty_frame_bottom.destroy()

        data['day']+=1
        lbl_day = tk.Label(master=window, text=f"Day {data['day']}")
        lbl_day.pack()

        summary = f"Congratulations, you have earned {exp_sum} exp today"
        if lvl_promotion:
            summary+= f' and reached {data["lvl"]}lvl'
            out_lvl += f" -> {data['lvl']}"
        summary+= ".\nYour personal stats are as follows:"

        label_final = tk.Label(master=window, pady=2, text=summary)
        label_final.pack()
        lbl_stats1 = tk.Label(master=window, text=f"{out_lvl}", fg="green" if lvl_promotion else "black")
        lbl_stats1.pack()

        out_exp = f"exp: {data['start_exp']}"
        if not lvl_promotion and exp_sum>0:
            out_exp += f" -> {data['remained_exp']}"
        lbl_stats2 = tk.Label(master=window, text=out_exp, fg="green" if exp_sum>0 else "black")
        lbl_stats2.pack()

        out_best = f"best: {data['best']}"
        if exp_sum > data['best']:
            out_best += f" -> {exp_sum}"
        lbl_stats3 = tk.Label(master=window, text=out_best, fg="green" if exp_sum >= data["best"] else "black")
        lbl_stats3.pack()

        out_best_chess = f"best chess: {data['best_chess']}"
        if cur_chess > data["best_chess"]:
            out_best_chess += f" -> {cur_chess}"
        lbl_stats4 = tk.Label(master=window, text=out_best_chess, fg="green" if cur_chess>=data["best_chess"] else "black")
        lbl_stats4.pack()

        out_best_spanish = f"best spanish: {data['best_spanish']}"
        if cur_spanish > data["best_spanish"]:
            out_best_spanish += f" -> {cur_spanish}"
        lbl_stats5 = tk.Label(master=window, text=out_best_spanish, fg="green" if cur_spanish>=data["best_spanish"] else "black")
        lbl_stats5.pack()

        out_best_juggling = f"best juggling: {data['best_juggling']}"
        if cur_juggling > data["best_juggling"]:
            out_best_juggling += f" -> {cur_juggling}"
        lbl_stats6 = tk.Label(master=window, text=out_best_juggling, fg="green" if cur_juggling>=data["best_juggling"] else "black")
        lbl_stats6.pack()

        if data["spanish_talking"]>=60:
            lbl_stats7 = tk.Label(master=window, text=f"FP: {data['FP']} -> {data['FP']+data['spanish_talking']//60}", fg="green")
        else:
            lbl_stats7 = tk.Label(master=window, text=f"FP: {data['FP']}")
        lbl_stats7.pack()

        if data['running']>=10:
            lbl_stats8 = tk.Label(master=window, text=f"DP: {data['DP']} -> {data['DP']+data['running']//10}", fg='green')
        else:
            lbl_stats8 = tk.Label(master=window, text=f"DP: {data['DP']}")
        lbl_stats8.pack()                          

        data['best'] = max(data['best'], exp_sum)
        data['best_chess'] = max(data['best_chess'], cur_chess)
        data['best_spanish'] = max(data['best_spanish'], cur_spanish)
        data['best_juggling'] = max(data['best_juggling'], cur_juggling)
        data['start_exp'] = data['remained_exp']
        for cur_score in ("chess_training", "chess_games", "spanish_talking", "learning_spanish_words", "intense_spanish_learning", "euros_earned", "juggling_training", "books", "fasting", "running"):
            data[cur_score] = 0

        with open("Jawor_TGoL.txt", "w") as file:
              json.dump(data, file)

        btn_quit = tk.Button(master=window, text="QUIT", command=quit)
        btn_quit.pack(padx=10, side="right")
        lbl_empty = tk.Label(master=window)
        lbl_empty.pack(pady=10)
    
try:
    with open("Jawor_TGoL.txt", "r") as file:
        data = json.load(file)
    elements = ["best", "best_chess", "best_spanish", "best_juggling", "FP", "DP", "lvl", "start_exp", "remained_exp", "chess_training", "chess_games", "spanish_talking", "learning_spanish_words", "intense_spanish_learning", "euros_earned", "juggling_training", "books", "running", "fasting", "day"]
    for element in elements:
        if element not in data or type(data[element])!=int:
            raise ValueError("Missing or wrong data")
except:
    data = {"best":0, "best_chess":0, "best_spanish":0, "best_juggling":0, "FP":0, "DP":0, "lvl":0, "start_exp":0, "remained_exp":0, "chess_training":0, "chess_games":0, "spanish_talking":0, "learning_spanish_words":0, "intense_spanish_learning":0, "euros_earned":0, "juggling_training":0, "books":0, "running":0, "fasting":0, "day":0}
finally:
    errors = []
    window = tk.Tk()
    window.minsize(width=520, height=180)
    window.title("The Game Of Life")

    frame_top = tk.Frame(master=window)

    frame_left1 = tk.Frame(master=frame_top, padx=15)
    lbl_chess_t1 = tk.Label(master=frame_left1, relief=tk.RAISED, borderwidth=2, text="chess training", width=18)
    lbl_chess_t1.pack(side=tk.LEFT)
    lbl_chess_t2 = tk.Label(master=frame_left1, relief=tk.RAISED, borderwidth=2, text=f"{data['chess_training']}", padx=5, width=2)
    lbl_chess_t2.pack(side=tk.LEFT)
    ent_chess_t = tk.Entry(master=frame_left1, width=5)
    ent_chess_t.pack(side=tk.LEFT)
    btn_chess_t = tk.Button(master=frame_left1, text="ADD", command=add_chess_t)
    btn_chess_t.pack(side=tk.LEFT)

    frame_left2 = tk.Frame(master=frame_top)
    lbl_chess_g1 = tk.Label(master=frame_left2, relief=tk.RAISED, borderwidth=2, text="chess games", width=18)
    lbl_chess_g1.pack(side=tk.LEFT)
    lbl_chess_g2 = tk.Label(master=frame_left2, relief=tk.RAISED, borderwidth=2, text=f"{data['chess_games']}", padx=5, width=2)
    lbl_chess_g2.pack(side=tk.LEFT)
    ent_chess_g = tk.Entry(master=frame_left2, width=5)
    ent_chess_g.pack(side=tk.LEFT)
    btn_chess_g = tk.Button(master=frame_left2, text="ADD", command=add_chess_g)
    btn_chess_g.pack(side=tk.LEFT)

    frame_left3 = tk.Frame(master=frame_top)
    lbl_spanish_t1 = tk.Label(master=frame_left3, relief=tk.RAISED, borderwidth=2, text="spanish talking", width=18)
    lbl_spanish_t1.pack(side=tk.LEFT)
    lbl_spanish_t2 = tk.Label(master=frame_left3, relief=tk.RAISED, borderwidth=2, text=f"{data['spanish_talking']}", padx=5, width=2)
    lbl_spanish_t2.pack(side=tk.LEFT)
    ent_spanish_t = tk.Entry(master=frame_left3, width=5)
    ent_spanish_t.pack(side=tk.LEFT)
    btn_spanish_t = tk.Button(master=frame_left3, text="ADD", command=add_spanish_t)
    btn_spanish_t.pack(side=tk.LEFT)

    frame_left4 = tk.Frame(master=frame_top)
    lbl_learning_s_w1 = tk.Label(master=frame_left4, relief=tk.RAISED, borderwidth=2, text="learning spanish words", width=18)
    lbl_learning_s_w1.pack(side=tk.LEFT)
    lbl_learning_s_w2 = tk.Label(master=frame_left4, relief=tk.RAISED, borderwidth=2, text=f"{data['learning_spanish_words']}", padx=5, width=2)
    lbl_learning_s_w2.pack(side=tk.LEFT)
    ent_learning_s_w = tk.Entry(master=frame_left4, width=5)
    ent_learning_s_w.pack(side=tk.LEFT)
    btn_learning_s_w = tk.Button(master=frame_left4, text="ADD", command=add_learning_s_w)
    btn_learning_s_w.pack(side=tk.LEFT)

    frame_left5 = tk.Frame(master=frame_top)
    lbl_intense_s_l1 = tk.Label(master=frame_left5, relief=tk.RAISED, borderwidth=2, text="intense spanish learning", width=18)
    lbl_intense_s_l1.pack(side=tk.LEFT)
    lbl_intense_s_l2 = tk.Label(master=frame_left5, relief=tk.RAISED, borderwidth=2, text=f"{data['intense_spanish_learning']}", padx=5, width=2)
    lbl_intense_s_l2.pack(side=tk.LEFT)
    ent_intense_s_l = tk.Entry(master=frame_left5, width=5)
    ent_intense_s_l.pack(side=tk.LEFT)
    btn_intense_s_l = tk.Button(master=frame_left5, text="ADD", command=add_intense_s_l)
    btn_intense_s_l.pack(side=tk.LEFT)

    frame_right1 = tk.Frame(master=frame_top, padx=15)
    lbl_euros1 = tk.Label(master=frame_right1, relief=tk.RAISED, borderwidth=2, text="euros earned", width=18)
    lbl_euros1.pack(side=tk.LEFT)
    lbl_euros2 = tk.Label(master=frame_right1, relief=tk.RAISED, borderwidth=2, text=f"{data['euros_earned']}", padx=5, width=2)
    lbl_euros2.pack(side=tk.LEFT)
    ent_euros = tk.Entry(master=frame_right1, width=5)
    ent_euros.pack(side=tk.LEFT)
    btn_euros = tk.Button(master=frame_right1, text="ADD", command=add_euros)
    btn_euros.pack(side=tk.LEFT)

    frame_right2 = tk.Frame(master=frame_top)
    lbl_juggling_t1 = tk.Label(master=frame_right2, relief=tk.RAISED, borderwidth=2, text="juggling training", width=18)
    lbl_juggling_t1.pack(side=tk.LEFT)
    lbl_juggling_t2 = tk.Label(master=frame_right2, relief=tk.RAISED, borderwidth=2, text=f"{data['juggling_training']}", padx=5, width=2)
    lbl_juggling_t2.pack(side=tk.LEFT)
    ent_juggling_t = tk.Entry(master=frame_right2, width=5)
    ent_juggling_t.pack(side=tk.LEFT)
    btn_juggling_t = tk.Button(master=frame_right2, text="ADD", command=add_juggling_t)
    btn_juggling_t.pack(side=tk.LEFT)

    frame_right3 = tk.Frame(master=frame_top)
    lbl_books1 = tk.Label(master=frame_right3, relief=tk.RAISED, borderwidth=2, text="books", width=18)
    lbl_books1.pack(side=tk.LEFT)
    lbl_books2 = tk.Label(master=frame_right3, relief=tk.RAISED, borderwidth=2, text=f"{data['books']}", padx=5, width=2)
    lbl_books2.pack(side=tk.LEFT)
    ent_books = tk.Entry(master=frame_right3, width=5)
    ent_books.pack(side=tk.LEFT)
    btn_books = tk.Button(master=frame_right3, text="ADD", command=add_books)
    btn_books.pack(side=tk.LEFT)

    frame_right4 = tk.Frame(master=frame_top)
    lbl_running1 = tk.Label(master=frame_right4, relief=tk.RAISED, borderwidth=2, text="running", width=18)
    lbl_running1.pack(side=tk.LEFT)
    lbl_running2 = tk.Label(master=frame_right4, relief=tk.RAISED, borderwidth=2, text=f"{data['running']}", padx=5, width=2)
    lbl_running2.pack(side=tk.LEFT)
    ent_running = tk.Entry(master=frame_right4, width=5)
    ent_running.pack(side=tk.LEFT)
    btn_running = tk.Button(master=frame_right4, text="ADD", command=add_running)
    btn_running.pack(side=tk.LEFT)

    frame_right5 = tk.Frame(master=frame_top)
    lbl_fasting1 = tk.Label(master=frame_right5, relief=tk.RAISED, borderwidth=2, text="fasting", width=18)
    lbl_fasting1.pack(side=tk.LEFT)
    combobox = ttk.Combobox(master=frame_right5, values=["No", "Yes"], width=13, justify="center")
    combobox.pack(side=tk.LEFT)
    combobox.set("No" if data['fasting']==0 else "Yes")
    combobox.bind("<<ComboboxSelected>>", save_fasting)

    frame_left1.grid(row=0, column=0)
    frame_left2.grid(row=1, column=0)
    frame_left3.grid(row=2, column=0)
    frame_left4.grid(row=3, column=0)
    frame_left5.grid(row=4, column=0)
    frame_right1.grid(row=0, column=1)
    frame_right2.grid(row=1, column=1)
    frame_right3.grid(row=2, column=1)
    frame_right4.grid(row=3, column=1)
    frame_right5.grid(row=4, column=1)
    frame_top.grid(pady=8)


    frame_bottom = tk.Frame(master=window, padx=10)
    frame_bottom.grid(row=5, sticky="e")
    btn_submit = tk.Button(master=frame_bottom, text="SUBMIT", command=submit)
    btn_submit.pack(side=tk.RIGHT)
    btn_save = tk.Button(master=frame_bottom, text="ADD ALL", command=add_all)
    btn_save.pack(side=tk.RIGHT, padx=10)
    btn_reset = tk.Button(master=frame_bottom, text="RESET", command=reset_all)
    btn_reset.pack(side=tk.RIGHT)
    empty_frame_bottom = tk.Frame(master=window, height=7)
    empty_frame_bottom.grid(row=6)

    window.mainloop()

