from db_loging import Connection_Database,get_data,get_display_name
import datetime
def get_data_country(Name):
    result = get_display_name(Name.lower())
    title = result[0]
    dataname=result[1]
    result = get_data(dataname)
    values_infected = [0,0,0,0,0,0,0,0,0,0,0,0]
    values_dead = [0,0,0,0,0,0,0,0,0,0,0,0]
    for row in result:
        insertion = row[1].strftime("%m")
        #datee = datetime.datetime.strptime(insertion, "%Y-%m-%d")
        month = (int)(insertion)
        infected = row[2]
        dead = row[3]
        values_infected[month-1] += infected
        values_dead[month-1] += dead
    maxInfected = max(values_infected)
    maxDead = max(values_dead)
    country={'name':title,'values_infected':values_infected,'values_dead':values_dead,"max_infected":maxInfected,"max_dead":maxDead}
    print(country)
    return country