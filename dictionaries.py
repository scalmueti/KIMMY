import random

jobsDic = {
        "FFWorker":[random.randint(500,1000), "Fast Food Worker"],
        "Barista":[random.randint(500,1000), "Barista"],
        "Waiter":[random.randint(500,1000), "Waiter"],
        "SecGuard":[random.randint(1000,2500), "Security Guard"],
        "Teacher":[random.randint(1000,2500), "Teacher"],
        "Plumber":[random.randint(2500,5000), "Plumber"],
        "SalesA":[random.randint(5000,7500), "Sales Associate"],
        "NurseA":[random.randint(5000,7500), "Nurse Associate"],
        "IT Manger":[random.randint(10000,15000), "IT Manager"],
        "SoftDev":[random.randint(10000,15000), "Software Developer"],
        "Surgeon":[random.randint(25000,50000), "Surgeon"],
        "Lawyer":[random.randint(25000,50000), "Lawyer"]
}

bankImgDic = {
    "0-1000":"https://raw.githubusercontent.com/scalmueti/KIMMY/refs/heads/master/assets/bankImages/0-1000_money.png",
    "1000-5000":"https://raw.githubusercontent.com/scalmueti/KIMMY/refs/heads/master/assets/bankImages/1000-5000_money.png",
    "5000-10000":"https://raw.githubusercontent.com/scalmueti/KIMMY/refs/heads/master/assets/bankImages/5000-10000_money.png",
    "10000-100000":"https://raw.githubusercontent.com/scalmueti/KIMMY/refs/heads/master/assets/bankImages/10000-100000_money.png",
    "100000+":"https://raw.githubusercontent.com/scalmueti/KIMMY/refs/heads/master/assets/bankImages/100000+_money.png"
}

commandsList = [
    "hello","bye","bank","pay","daily","work","cash","job","steal","apply","help","prefix"
]