The following code will read in the data and show you the number of translations:

hamlets = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@hamlets.csv", 
                      index_col=0)
                
hamlets
language	text
1	English	The Tragedie of Hamlet\n ...
2	German	Hamlet, Prinz von Dännemark.\n ...
3	Portuguese	HAMLET\n DRAMA EM ...
