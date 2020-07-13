The following code will read in the data:

data = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@wine.csv",
                  index_col=0)
                  
data.head()
