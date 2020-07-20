import pymysql
import pyexcel

client = pymysql.connect(               
    host = 'localhost',                  #là máy tính của mình
    user = 'root',                       #là username của chính mình, thường là root
    password = 'Caprice245#'
)

records = pyexcel.get_records(file_name = "athlete_events.csv")

cursor = client.cursor()

# cursor.execute('CREATE DATABASE olympics') 

cursor.execute('''CREATE TABLE IF NOT EXISTS olympics.athletes(
    id INTEGER(100),
    name VARCHAR(255),
    sex VARCHAR(100),
    height VARCHAR(100),
    weight VARCHAR(100)
)''')     

cursor.execute('''CREATE TABLE IF NOT EXISTS olympics.games(
    title VARCHAR(255),
    year INTEGER(100),
    season VARCHAR(100)
)''')    

cursor.execute('''CREATE TABLE IF NOT EXISTS olympics.sports(
    sport VARCHAR(255),
    event VARCHAR(255) PRIMARY KEY
)''') 

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS olympics.athlete_age_medal(
        id INTEGER(100) PRIMARY KEY AUTO_INCREMENT,
        id_athletes INTEGER(100) REFERENCES olympics.athletes(id),
        title_olympic VARCHAR(255) REFERENCES olympics.games(title),
        event VARCHAR(255) REFERENCES olympics.sports(event),
        sport VARCHAR(255),
        age VARCHAR(100),
        medal VARCHAR(255)
       )
    '''
)

cursor.execute('''CREATE TABLE IF NOT EXISTS olympics.athletes_nationality(
    id_athlete INTEGER(100),
    name VARCHAR(255),
    country VARCHAR(255)
)''')   


# for r in records:
#     name = r['Name'].replace('"', '\'').replace('`', '\'')
#     cursor.execute(
#     f'''
#     INSERT INTO olympics.athletes(id, name, sex, height, weight)
#     VALUES ({int(r['ID'])}, "{name}", "{r['Sex']}", "{r['Height']}", "{r['Weight']}")
#     '''
# )

# for r in records:
#     cursor.execute(
#     f'''
#     INSERT INTO olympics.games(title, year, season)
#     VALUES ("{(r['Games'])}", {(r['Year'])}, "{r['Season']}")
#     '''
# )

# for r in records:
#     cursor.execute(
#         f'''
#         SELECT * FROM olympics.sports WHERE event = "{r['Event']}"
#         '''
#         )
#     event_found = cursor.fetchone()
#     if not event_found:
#         cursor.execute(
#             f'''
#             INSERT INTO olympics.sports(sport, event)
#             VALUES ("{(r['Sport'])}", "{r['Event']}")
#             '''
#             )


# for r in records:
#     cursor.execute(
#     f'''
#     INSERT INTO olympics.athlete_age_medal(id_athletes, title_olympic, event, sport, age, medal)
#     VALUES ({(r['ID'])}, "{(r['Games'])}", "{r['Event']}", "{r['Sport']}", "{(r['Age'])}", "{r['Medal']}")
#     '''
#     )


for r in records:
    name = r['Name'].replace('"', '\'').replace('`', '\'')
    cursor.execute(
    f'''
    INSERT INTO olympics.athletes_nationality(id_athlete, name, country)
    VALUES ({(r['ID'])}, "{name}", "{r['Country']}")
    '''
    )




client.commit()    
