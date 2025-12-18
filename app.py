from flask import Flask,render_template,request,redirect,url_for,session
import mysql.connector
import os

#global var
year=[]
app=Flask(__name__)
app.secret_key='123'

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        league=request.form.get('leagues')
        return render_template("index.html",league=league)

@app.route("/EPL",methods=['GET','POST'])
def league_1():
    if request.method=='GET':
        return render_template("league_epl.html")
  

@app.route("/league_teams",methods=['GET','POST'])
def league_teams():
    if request.method=='POST':
        year=request.form.get('seasons')
        sql=get_con()
        query=ret_team_season_query(year)
        teams=exec_select(sql,query)
        session['teams']=teams
        session['year']=year
        teams = session.get('teams', [])
     
        teams=[str(team).replace("'"," ").replace(","," ").replace("("," ").replace(")"," ").strip() for team in teams]
        session.pop('teams', None)
        return render_template("league_teams.html", teams=teams,title=year)
            
@app.route("/stats",methods=['GET','POST'])
def stats():
    team=request.form.get("seasons")
    year=session['year']
    for i in range(14,24):
        z=2000+i
        if str(year).startswith(str(z)):
            str_year=str(i)
            str_z=str(z)
    tables=['team_attackspeed_stats_','team_situation_stats_','team_result_stats_','team_timing_stats_','team_shotzone_stats_','team_formation_stats_','team_gamestate_stats_']
    
    try:
        sql=get_con()
    except:
        print("error")
    query=f"SELECT id FROM teams WHERE name='{team}' and  `{year}`=1"    
    id=exec_select(sql,query)
    idz=str(id[0]).replace(")"," ").replace("("," ").replace(","," ").strip()
    data = {}
    i = 1
    
    # Loop through each table and collect data
    for table in tables:
        # Build the query based on the year condition
        if str_year != '23':
            table_name = f"{table}{str_year}"
        else:
            table_name = f"{table}{str_z}"
        
        # Construct the query
        query = f"SELECT * FROM {table_name} WHERE id={idz}"
        
        # Execute the query and store the result
        stat = exec_select(sql, query)
        
        # Only add to data if stat has results
        if stat:
            data[i] = stat
        else:
            data[i] = None  
        
        i += 1
    path=get_image(idz)
   
    return render_template("stats.html",team=team,data=data,path=path,year=year)

@app.route("/Laliga",methods=['GET','POST'])
def league_2():
    return render_template("league.html")

@app.route("/Bundesliga",methods=['GET','POST'])
def league_3():
    return render_template("league.html")

@app.route("/SerieA",methods=['GET','POST'])
def league_4():
    return render_template("league.html")

def get_con():
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Formysql",
    database="stats"
    )

    return conn
if __name__=='__main__':
    app.run(debug=True)

def ret_team_season_query(season):
    query=f"SELECT name FROM teams WHERE `{season}`=1"
    return query


@app.context_processor
def calc_year():
    year=[]
    for i in range(2014,2024):
        x=str(i)+'/'+str(i+1)
        year.append(x)
    return dict(year=year)

def exec_select(sql,query):
    mycursor=sql.cursor()
    mycursor.execute(query)
    resultset=mycursor.fetchall()
    return resultset


def get_image(name):
    extensions = ['.png', '.jpg', '.jpeg', '.svg', '.webp']
    for ext in extensions:
        image_path = f"./static/images/{name}{ext}"
        if os.path.exists(image_path):
            return image_path