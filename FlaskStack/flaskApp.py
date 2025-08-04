from flask import Flask, request, render_template, send_file
import LPGd
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/Home', methods=['GET', 'POST'])
def home_page():
   return render_template('form.html')

@app.route('/Library', methods=['GET', 'POST'])
def library_page():
   return render_template('library.html')

@app.route('/About', methods=['GET', 'POST'])
def about_page():
   return render_template('about.html')

@app.route('/Graphs', methods=['GET', 'POST'])
def graphs():
   form = request.form.to_dict(flat=False)

   #Call Solver
   df = LPGd.LPG(form)

   #Load Data Frame
   df['x'] = pd.to_numeric(df['x'])
   df['y'] = pd.to_numeric(df['y'])
   df['z'] = pd.to_numeric(df['z'])

   #Create Graphs
   plot_3d = px.scatter_3d(df, x='x', y='y', z='z')
   plot_front = px.scatter(df, x='x', y='z')
   plot_top = px.scatter(df, x='x', y='y')

   #Change marker sizes
   plot_3d.update_traces(marker=dict(size=2))
   plot_front.update_traces(marker=dict(size=4))
   plot_top.update_traces(marker=dict(size=4))

   #Convert Graphs to HTML
   graph_json_3d = plot_3d.to_html(full_html=True, include_plotlyjs='cdn') 
   graph_json_front = plot_front.to_html(full_html=True, include_plotlyjs='cdn')
   graph_json_top = plot_top.to_html(full_html=True, include_plotlyjs='cdn')

   return render_template('graphs.html', form=form, graph_json_3d=graph_json_3d, 
                        graph_json_front=graph_json_front, graph_json_top=graph_json_top, )