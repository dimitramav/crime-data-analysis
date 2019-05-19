import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import folium
from folium.plugins import MarkerCluster

figure_size = (11.7,8.27)

def plot_number_of_crimes(df, plot_x, horizontal=False):
	sns.set(rc={'figure.figsize':figure_size})

	series = df.groupby([plot_x]).size()
	df = pd.DataFrame({plot_x:series.index, 'total_crimes':series.values})
	if (horizontal):
		plot = sns.barplot(x="total_crimes", y=plot_x, data=df, color="c")
	else:
		plot = sns.barplot(x=plot_x, y="total_crimes", data=df)
	plt.show()

def plot_2d(X,x_label,y_label):
	sns.set(rc={'figure.figsize':figure_size})
	sns.scatterplot(x=x_label, y=y_label ,data=X)
	plt.show()

def kmeans_plot_2d(X,clusters):
	sns.set(rc={'figure.figsize':figure_size})
	kmeans = KMeans(n_clusters=clusters)
	kmeans.fit(X)
	kmeans.predict(X)
	plt.scatter(X[:,0], X[:,1], c=kmeans.labels_.astype(float), cmap = "plasma")
	plt.show()

def plot_3d(X,x_label,y_label,z_label,title,labels=None):
	fig = plt.figure(1, figsize=figure_size)
	ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
	ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, cmap="plasma", edgecolor='k')
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	ax.set_zlabel(z_label)
	plt.title(title, fontsize=14)
	plt.show()

def kmeans_plot_3d(X,clusters,x_label,y_label,z_label,title):
	kmeans = KMeans(n_clusters=clusters)
	kmeans.fit(X)
	kmeans.predict(X)
	plot_3d(X,x_label,y_label,z_label,title,kmeans.labels_.astype(float))

def interactive_map(mean_location, location):

	icon_create_function = """\
	function(cluster) {
		return L.divIcon({
		html: '<b>' + cluster.getChildCount() + '</b>',
		className: 'marker-cluster marker-cluster-large',
		iconSize: new L.Point(20, 20)
		});
	}"""

	popups = ['lon:{}<br>lat:{}'.format(lon, lat) for (lat, lon) in location]

	m = folium.Map(
		location=mean_location,
		tiles='Cartodb Positron',
		zoom_start=10
	)

	marker_cluster = MarkerCluster(
		locations=location, popups=popups,
		overlay=True,
		control=True,
		icon_create_function=icon_create_function
	)

	marker_cluster.add_to(m)
	folium.LayerControl().add_to(m)

	return m