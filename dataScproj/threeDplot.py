# importing plotly and adding credentials to it
import plotly 
plotly.tools.set_credentials_file(username='ramranganath', api_key='inio3xGd28QAvAzeErTq')
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import trace

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')
df.head()



data = []
clusters = []
colors = ['rgb(228, 26,28)','rgb(55,126,184)', 'rgb(77,175,74)']

for i in range(len(df['Name'].unique())):
    name = df['Name'].unique()[i]
    color = colors[i]
    
    x = df[df['Name']== name]['SepalLength']
    y = df[df['Name']== name]['SepalWidth']
    z = df[df['Name']== name]['PetalLength']
    
    
    trace = dict(
        name =name,
        x =x, y=y, z=z,
        mode = 'markers',
        marker = dict(size =3, color =color, line=dict(width=1)))
    data.append(trace)
    
layout = dict(
    width=800,
    height=550,
    autosize=False,
    title='Iris Dataset',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255,255)',
            zerolinecolor='rgb(255,255,255)',
            showbackground=True,
            backgroundcolor='rgb(230,230,230)'
            ),
        yaxis=dict(
            gridcolor='rgb(255, 255,255)',
            zerolinecolor='rgb(255,255,255)',
            showbackground=True,
            backgroundcolor='rgb(230,230,230)'
            ),
        zaxis=dict(
            gridcolor='rgb(255, 255,255)',
            zerolinecolor='rgb(255,255,255)',
            showbackground=True,
            backgroundcolor='rgb(230,230,230)'
            ),
        aspectratio = dict( x=1, y=1, z=0.7 ),
        aspectmode = 'manual'        
    ),
)

fig = dict(data=data, layout=layout)

# IPython notebook
# py.iplot(fig, filename='pandas-3d-iris', validate=False)

url = py.plot(fig, filename='pandas-3d-iris', validate=False)
    
 # pairwise scatter plot : pair polt 
 # Dis adv : 1. can be used when num of features are high
 # 2. Cannot visualize higher dimensional patterns in 3-D and 4-D
 # Only possible to vies in 2-D patterens with all variables.
 
 ###plt.close();
 ###sns.set_style("whitegrid");
 ###sns.pairplot(iris, hue="species", size=3);
 ###plt.show()
 
 # NOTE: the diagonal elements are PDFs for each feature. PDFs are explained
    
    