import random
import os

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