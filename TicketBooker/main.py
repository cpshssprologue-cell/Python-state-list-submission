#API1 = "99ae80812dcd62ae39deb0967afcd554"
#root1:main tkinter, thing1: frame inside tkinter window, API login for TMDB not OMDB, for login the text is black, and field is yellow, and for passwords the opposite. pack screen3.


import tkinter as tk
import platform
import requests
import random
import webbrowser
import datetime
from datetime import timedelta, datetime
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import io
from io import BytesIO
x = 0
y = 0
i = 0
l = []
iflog = 44331
API1 = "99ae80812dcd62ae39deb0967afcd554"
Red1 = '#470B0B'
Red2 = '#6F1111'
Red3 = '#540D0D'
news = ['Jumanji 4 confirmed to waste your time on release day',
        'J.K Rowling escapes Insane Asylum',
        'Paddington Bear shot down in Detroit']
loginsdict = {
    44331: [
        'Neil', 
        '12345678', 
        ['Project Hail Mary', 'Breaking Bad', 'Bojack Horseman', 'Better Call Saul', 'Mr. Robot', 'Spider-man: Into the Spiderverse'], 
        ['The Grand Tour', 'Back to the Future', 'For all Mankind', 'Citizen Kane', 'El Camino', 'Spider-man: Beyond the Spiderverse'], 
        1262, 
        [['03/04/26', 'Project Hail Mary', '14:30']],
        'Cineroyal'
    ],
    70653: [
        'Addu05', 
        'password123', 
        ['Inception', 'The Bear', 'Succession', 'Interstellar'], 
        ['The Prestige', 'Dune: Part Two'], 
        450, 
        [['01/12/17', 'Inception', '19:00'], ['02/12/24', 'Dune: Part Two', '21:15']],
        'VOX Movies'        
    ],
    71823: [
        'Ryan', 
        'qwertyuiop', 
        ['The Office', 'Parks and Rec', 'Paddington 2', 'Paddington'], 
        ['Shrek 5', 'Severance'], 
        892, 
        [['20/11/23', 'Paddington 2', '14:00']],
        'Puthettu Cinemas'
    ],
    83235: [
        'B. Butcher', 
        'i1nfm5oefs2345', 
        ['Black Mirror', 'Severance', 'Dark', 'The Matrix', 'The Boys'], 
        ['The Boys','Andor', 'The Batman'], 
        2105, 
        [['05/10/25', 'The Matrix', '23:30'], ['12/25/25', 'The Batman', '18:45']],
        'Puthettu Cinemas'
    ],
    81302: [
        'Ali', 
        'NiceGuy321', 
        ['Succession', 'Billions', 'Avatar', 'The Whale'], 
        ['Wolf of Wall Street', 'Gladiator II', 'American Psycho'], 
        7340, 
        [['04/01/26', 'Avatar', '20:00']],
        'Puthettu Cinemas'
    ]
}

#def loading():    Nevermind this, possible future code for a loading screen while the movies and stuff load??
    #loadingroot = tk.Tk()
    #loadingroot.geometry(f"720x400")
    #loadingroot.title("LOADING")
    #tk.Label(loadingroot, text = 'LOADING, PLEASE WAIT', fg = 'yellow', bg = 'black', font = ('Menlo', 32))
    #home()
    
def article(name, id1):
    root2 = tk.Toplevel()
    screenx = (int((root2.winfo_screenwidth())*(15/16)))
    screeny = (int((root2.winfo_screenheight())*(7/8)))
    root2.geometry(f"{screenx}x{screeny}")
    root2.title("Rotten Potatoes: " + name)
    root2.configure(bg = Red1, cursor = "star")
    root2.thing1 = tk.Frame(root2, bg = Red2)
    root2.thing1.place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight = 0.9, anchor = 'center')
    link = f"https://api.themoviedb.org/3/search/movie?api_key={API1}&query={name}"
    share2 = requests.get(link).json()
    mdbid = share2['results'][0]['id']
    link1 = f"https://api.themoviedb.org/3/movie/{mdbid}?api_key={API1}&language=en-US"
    share1 = requests.get(link1).json()
    name1 = share1.get('title')
    desc = share1.get('overview')
    posterlink = share1.get('poster_path')
    date = share1.get('release_date')
    meter = share1.get('vote_average')
    tagline = share1.get('tagline')
    runtime = share1.get('runtime')
    if posterlink:
        link2 = f"https://image.tmdb.org/t/p/w500{posterlink}"
        thing2 = requests.get(link2).content
        imageopen = Image.open(BytesIO(thing2)).resize((int(0.35 * screenx), int(0.9 * screeny)))
        tkinterprocess = ImageTk.PhotoImage(imageopen)
        framing = tk.Label(root2.thing1, image=tkinterprocess, bg='black', bd=15, relief="ridge")
        framing.image = tkinterprocess
        framing.pack(side = 'left', anchor = 'n', padx = 15, pady = 15)
    else:
        noimage = tk.Frame(root2, bg = Red2)
        noimage.place(relx = 0.03, rely = 0.5, relwidth = 0.35, relheight = 0.9, anchor = 'w')
        framing = tk.LabelFrame(noimage, text = "No Poster", fg = "white", font = ("Menlo", 56))
        framing.pack(padx=1, pady=10, fill="both", expand=True)
    releasedetails = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.now()
    maincontainer1 = tk.Frame(root2.thing1, bg = Red2)
    maincontainer1.pack(side = 'left', fill = 'both', expand = True, padx = 20, pady = 20)
    title = tk.Label(maincontainer1, text = name1, fg = "white", bg = Red2, font = ("Menlo", 48, "bold"), wraplength = screenx*0.5, justify="left")
    title.pack(anchor = 'w', pady = (0, 10))
    date2 = tk.Label(maincontainer1, text = f"{date}", fg = "yellow", bg = Red2, font = ("Menlo", 24))
    date2.pack(anchor = 'w', pady = (0, 15))
    subtitle1 = tk.Label(maincontainer1, text = f"{tagline}", fg = "yellow", bg = Red2, font = ("Menlo", 24))
    subtitle1.pack(anchor = 'w', pady = (0, 20))
    runtime1 = tk.Label(maincontainer1, text = f"{runtime} minutes", fg = "yellow", bg = Red2, font = ("Menlo", 24))
    runtime1.pack(anchor = 'w', pady = (0, 25))
    descmain = tk.Label(maincontainer1, text = desc, fg = "white", bg = Red2, font = ("Menlo", 16), wraplength = screenx*0.5, justify = "left")
    descmain.pack(anchor = 'w', pady = (0, 30))
    meter1 = tk.Label(maincontainer1, text = f"{meter} on the potatometer", fg = "yellow", bg = Red2, font = ("Menlo", 24))
    meter1.pack(anchor = 'w', pady = (0, 35))
    
    i = (today - releasedetails).days
    if i <= 60:
        nowshowing = tk.Label(maincontainer1, text = "NOW SHOWING IN THEATERS", fg = "white", bg = Red2, font = ("Menlo", 24, "bold"))
        nowshowing.pack(anchor = 'w', pady = 10)
    def watchlist1():
        if name1 not in loginsdict[iflog][3]:
            loginsdict[iflog][3].append(name1)
    if iflog:
        watchlist2 = tk.Button(maincontainer1, text = "Add to Watchlist", font = ("Menlo", 18), command = watchlist1)
        watchlist2.pack(anchor = 'w', pady = 20)
    else:
        watchlist3 = tk.Label(maincontainer1, text = "Login to add to watchlist", fg = "yellow", bg = Red2, font = ("Menlo", 18))
        watchlist3.pack(anchor = 'w', pady = 20)

    def booker():
        bookwin = tk.Toplevel(root2)
        bookwin.title(f"Booking Tickets")
        bookwin.geometry("1080x720")
        bookwin.configure(bg=Red3)
        
        theater = loginsdict[iflog][6]
        tk.Label(bookwin, text=f"Booking at {theater}", fg="yellow", bg=Red3, font=("Menlo", 22)).pack(pady=10)

        tk.Label(bookwin, text="Date:", fg="white", bg=Red3).pack()
        
        datenow = tk.StringVar(value=(datetime.now().strftime("%d/%m")))
        datesframe = tk.Frame(bookwin, bg=Red3)
        datesframe.pack()
        for i in range(7):
            d = (datetime.now() + timedelta(days=i)).strftime("%d/%m")
            if i == 0:
                d = 'Today'
            elif i == 1:
                d = 'Tomorrow'
            tk.Radiobutton(datesframe, text=d, variable=datenow, value=d).pack(side="left", padx=2)
            
        tk.Label(bookwin, text="Time:", fg="white", bg=Red3).pack(pady=(10,0))
        timev = tk.StringVar(value="14:30")
        times = ["10:00", "14:30", "18:00", "21:15"]
        times2 = ["11:30", "13:00", "19:30", "23:30"]
        timesframe = tk.Frame(bookwin, bg=Red3)
        timesframe.pack()
        for t in times:
            tk.Radiobutton(timesframe, text=t, variable=timev, value=t).pack(side="left", padx=2)


        screen = Image.open("screen.png")
        screen2 = ImageTk.PhotoImage(screen)
        screen3 = tk.Label(bookwin, image = screen2, bg=Red3)

        
        tk.Label(bookwin, text="SCREEN", fg="white", bg="black", font = ('Menlo', 24, "bold")).pack(pady=50, ipady=20, fill="x")
        
        sframe = tk.Frame(bookwin, bg=Red3)
        sframe.pack()
        seats = []
        for r in range(6):
            rows = []
            for c in range(8):
                ting = tk.BooleanVar()
                toggler = tk.Checkbutton(sframe, variable=ting, bg=Red3, activebackground="yellow")
                toggler.grid(row=r, column=c)
                rows.append(ting)
            seats.append(rows)

        def confirm():
            booked = []
            for r in range(6):
                for c in range(8):
                    if seats[r][c].get(): booked.append(f"{chr(65+r)}{(c+1)}")
            if booked:
                bookwin.destroy()

        tk.Button(bookwin, text="CONFIRM BOOKING", command=confirm, bg="yellow", fg="black", font = ('Menlo')).pack(pady=20)

    if i <= 60:
        booker0 = tk.Button(maincontainer1, text=f"Book tickets for {loginsdict[iflog][6]}", 
                             bg="yellow", font=("Menlo", 18), command = booker)
        booker0.pack(anchor='w', pady=10)
    
    
def home():
    root1 = tk.Tk()
    screenx = int(root1.winfo_screenwidth()*(7/8))
    screeny = int(root1.winfo_screenheight()*(7/8))
    root1.geometry(f"{screenx}x{screeny}")
    root1.state('zoomed')
    root1.title("ROTTEN POTATOES")
    mainicon1 = tk.PhotoImage(file="icon1.png")
    root1.wm_iconphoto(True, (mainicon1))
    root1.configure(bg = Red1, cursor = "star")
    root1.thing1 = tk.Frame(root1, bg = Red2)
    root1.thing1.place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight = 0.9, anchor = 'center')

    search1 = tk.StringVar()
    search2 = tk.Entry(root1.thing1, textvariable=search1, font=("Menlo", 18))
    search2.place(x=150, y=40, width=900, height=40)
    search3 = tk.Button(root1.thing1, text="SEARCH", font = ("Menlo"), command=lambda: article(search1.get(), iflog))
    search3.place(x=1055, y=43, width=100, height=34)

    def loginf():
        global iflog
        if iflog:
            id2 = usergetter.get()
            password = passwordgetter.get()
            for uid, data in loginsdict.items():
                if data[0] == id2 and data[1] == password:
                    iflog = uid
                    loginframe.destroy()
                    home1()
                    Movies1()
                    TV1()
                    events1()
                    greet = tk.Label(root1.thing1, text=(data[0]), fg="yellow", bg = Red2, font=("Menlo", 16))
                    greet.place(x=1275, y=43, width=100, height=34)
        else:
            greet = tk.Label(root1.thing1, text=(data[0]), fg="yellow", bg = Red2, font=("Menlo", 16))
            greet.place(x=1275, y=43, width=100, height=34)

    loginframe = tk.Frame(root1.thing1, bg=Red2, width=500, height=100)
    loginframe.place(relx=0.7, y=10)
    usergetter = tk.Entry(loginframe, fg = 'black', bg = 'yellow', font=("Menlo", 12))
    usergetter.place(x=0, y = 33, width = 100, height = 34)
    passwordgetter = tk.Entry(loginframe, fg = 'yellow', bg = 'black', font=("Menlo", 12))
    passwordgetter.place(x=125, y = 33, width = 100, height = 34)
    loginrgskj = tk.Button(loginframe, font=("Menlo"), text="LOGIN", command=loginf)
    loginrgskj.place(x=250, y = 33, width = 100, height = 34)
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Black.TNotebook", background="black", borderwidth=0)
    tabs1 = ttk.Notebook(root1.thing1, style = 'Black.TNotebook')
    tabs1.place(x = 0, y = 120, relwidth = 1, relheight = 0.85)
    
    hometab = tk.Frame(tabs1, bg="black")
    moviestab = tk.Frame(tabs1, bg="black")
    tvtab = tk.Frame(tabs1, bg="black")
    eventstab = tk.Frame(tabs1, bg="black")
    Abouttab = tk.Frame(tabs1, bg="black")
    
    tabs1.add(hometab, text = "Home")
    tabs1.add(moviestab, text = "Movies")
    tabs1.add(tvtab, text = "TV")
    tabs1.add(eventstab, text = "Current Events")
    tabs1.add(Abouttab, text = "About")

    logotop = Image.open("logobglessinv.png")
    logotop = logotop.resize((100, 100))
    logotop1 = ImageTk.PhotoImage(logotop)
    logotop2 = tk.Label(root1.thing1, image = logotop1, bg = Red2)
    logotop2.image = logotop1
    logotop2.place(x = 30, y = 10)

    def home1():
        newshome = tk.LabelFrame(hometab, text = "News", fg = "white", font = ("Menlo", 32), bg='#241415')
        newshome.place(relx = 0.05, rely = 0.05, relwidth = 0.4, relheight = 0.2)
        for newstext in news:
            tk.Label(newshome, text = newstext, fg = "yellow", font = ("Menlo", 18)).pack(pady = 0.1)

        promohome = tk.LabelFrame(hometab, text = "Offers", fg = "white", font = ("Menlo", 32), bg='#241415')
        promohome.place(relx = 0.55, rely = 0.01, relwidth = 0.4, relheight = 0.24)
        tk.Label(promohome, text = "1. Celebrating Women: Tickets 40% off on Women's Day \n 2. 10% discount on tickets with code MAR08", 
                fg = "yellow", font = ("Menlo", 18), bg='#241415').pack(pady = 2)
        if iflog:
            pointstext = ("You have "+ str(loginsdict[iflog][4]) + " reward points")
            tk.Label(promohome, text = pointstext, fg = "yellow", font = ("Menlo", 18), bg='#241415').pack(pady = 2)

        watchlisthome = tk.LabelFrame(hometab, text = "Watchlist", fg = "white", font = ("Menlo", 32), bg='#241415')
        watchlisthome.place(relx = 0.05, rely = 0.3, relwidth = 0.9, relheight = 0.6)
        if iflog:
            for movies2 in loginsdict[iflog][3]:
                tk.Label(watchlisthome, text = movies2, fg = "yellow", font = ("Menlo", 32), bg='#241415').pack(pady = 1)
        else:
            tk.Label(watchlisthome, text = "LOGIN for Watchlist", fg = "yellow", font = ("Menlo", 32), bg='#241415').pack(pady = 1)
    home1()

    def Movies1():        
        top10 = tk.LabelFrame(moviestab, text = "TOP 10", fg = "white", font = ("Menlo", 32), bg='#241415')
        top10.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.3)

        watchlistmovies = tk.LabelFrame(moviestab, text = "Watchlist", fg = "white", font = ("Menlo", 32), bg='#241415')
        watchlistmovies.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.3)

        mustwatches = tk.LabelFrame(moviestab, text = "Must Watch", fg = "white", font = ("Menlo", 32), bg='#241415')
        mustwatches.place(relx = 0.05, rely = 0.75, relwidth = 0.9, relheight = 0.3)
        def fetcher1(endpoint, frame):
            link3 = f"https://api.themoviedb.org/3/{endpoint}?api_key={API1}&language=en-US&page=1"
            capture = (requests.get(link3).json()).get('results', [])[:6]
            for h in capture:
                name = h.get('title')
                poster = h.get('poster_path')
                if poster:
                    pull = requests.get(f"https://image.tmdb.org/t/p/w200{poster}").content
                    pull1 = Image.open(BytesIO(pull)).resize((100, 160))
                    pull2 = ImageTk.PhotoImage(pull1)
                    cell = tk.Button(frame, image=pull2, command=lambda n=name: article(n, iflog), bg="black", bd = 3, relief="ridge", highlightthickness=2, highlightbackground="white")
                    cell.image = pull2
                    cell.pack(side="left", padx=10, pady=5)

        fetcher1("movie/popular", top10)
        fetcher1("movie/top_rated", mustwatches)
    Movies1()
    
    def TV1():        
        top10 = tk.LabelFrame(tvtab, text = "TOP 10", fg = "white", font = ("Menlo", 32), bg='#241415')
        top10.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.3)

        watchlistmovies = tk.LabelFrame(tvtab, text = "Watchlist", fg = "white", font = ("Menlo", 32), bg='#241415')
        watchlistmovies.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.3)

        mustwatches = tk.LabelFrame(tvtab, text = "Must Watch", fg = "white", font = ("Menlo", 32), bg='#241415')
        mustwatches.place(relx = 0.05, rely = 0.75, relwidth = 0.9, relheight = 0.3)
        def fetcher2(endpoint, frame):
            link3 = f"https://api.themoviedb.org/3/{endpoint}?api_key={API1}&language=en-US&page=1"
            capture = (requests.get(link3).json()).get('results', [])[:6]
            for h in capture:
                name = h.get('name')
                poster = h.get('poster_path')
                if poster:
                    pull = requests.get(f"https://image.tmdb.org/t/p/w200{poster}").content
                    pull1 = Image.open(BytesIO(pull)).resize((100, 160))
                    pull2 = ImageTk.PhotoImage(pull1)
                    cell = tk.Button(frame, image=pull2, command=lambda n=name: article(n, iflog), bg="black", bd = 3, relief="ridge", highlightthickness=2, highlightbackground="white")
                    cell.image = pull2
                    cell.pack(side="left", padx=10, pady=5)
        fetcher2("tv/popular", top10)
        fetcher2("tv/top_rated", mustwatches)        
    TV1()

    def events1():        
        WorldCupFIFA = tk.LabelFrame(eventstab, text = "World Cup FIFA", fg = "white", font = ("Menlo", 32), bg='#241415')
        WorldCupFIFA.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.3)

        Formula1 = tk.LabelFrame(eventstab, text = "FORMULA 1", fg = "white", font = ("Menlo", 32), bg='#241415')
        Formula1.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.3)

        Politics = tk.LabelFrame(eventstab, text = "Live World News and Politics", fg = "white", font = ("Menlo", 32), bg='#241415')
        Politics.place(relx = 0.05, rely = 0.75, relwidth = 0.9, relheight = 0.3)
    events1()

    def Aboutpage():
        desc2 = tk.Label(Abouttab, text = "\n\n Mock Movie Database/Theater booking software based off of 'Rotten Tomatoes' written in Python\n with the help of TMDB which is where all movie info and posters are from.\n Minimal assistance from Google getting the gears turning but otherwise, it's not vibecoded.\n Done as hobby project by Darsh R.", fg = "white", font = ("Menlo", 28), bg='#241415').pack(pady = 10)
    Aboutpage()

#loading()
home()

