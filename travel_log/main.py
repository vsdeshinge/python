travel_log = []

def add_new_country(country,visits,places):
    maggy={}
    maggy["country"]=country
    maggy["visits"]=visits
    maggy["cities"]=places
    travel_log.append(maggy)

mahasrhi=False
while not mahasrhi:
    places=[]
    country=input("enter a country name you visited")
    times_visited=int(input("Number of times visited"))
    done=False
    while not done:
        m=input("Enter a Places")
        if m=="done":
            done=True
            break
        places.append(m)
    add_new_country(country, times_visited, places)
    a=input('Are you want to insert new log "yes","no"')
    if a=="no":
        mahasrhi=True
print(travel_log)