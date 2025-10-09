import pandas as pd


df1 =  pd.read_csv("albumtracktune.csv", encoding="latin-1")
df2 =  pd.read_csv("album.csv", encoding="latin-1")

pd.set_option("display.max_rows", 100) #setting the max row pandas will display to 100, noramally set to 10 or 20 for large data sets

print(df1)
print(df2)

print("This is the album track tune library")
print(df1.head()) # print the first 5
print(df1.tail()) # print last 5
print(df1.shape)
print(df1.info())


print("Tjis is the album libray")
print("These are the first 5 tracks")
print(df2.head()) # print the first 5
print("These are the last 5 tracks")
print(df2.tail()) # print last 5
print(df2.shape)
print(df2.info())
print(df2.describe())


print(df2.isnull())


print(df2.columns)
print("There are :",df2["artist"].nunique())
print("These are there names",(df2["artist"].unique()))#limiting the number of names atm put list to list all of them

print("this is the number of columns:",len(df1))

print(df1.columns)# lists the columns of the track

#the alubum id links the tracks from alubs to the ablums in the 

#2.2

print("The max amount of tracks:",df1["track_num"].max())
print("The max amount of tunes:",df1["tune_num"].max())

print("is the most common tune", df2["title"].mode()[0])





def artist_albubs(artist_name):
    x = df2[df2["artist"].str.contains(artist_name, case= False)]

    print(artist_name, "tunes")
    print(x.shape[0])

    for i, row in x.iterrows():
        print(row['title'])
        
artist_albubs("altan")
artist_albubs("Martin Hayes")
artist_albubs("The Bothy Band")
j = 0
for i, row in df1.iterrows():
    if row["album_id"] == 1 :
        print(row["title"])
        j += 1
        
print("There are",j,"tracks on that alub")
def tunes_album(x):
    tunes = 0
    for i, row in df1.iterrows():
        if row["album_id"] == x :
            album_name = row["album_id"]
            break
    
    for i, row in df1.iterrows():
        if row["album_id"] == x :
            tunes += row["tune_num"]
    print("This is how many tunes are in",tunes,)
tunes_album(1)


#tunes greater than 1
greater_one_tune = df1["tune_num"] > 1
print("there are:",len(df1[greater_one_tune]))


print(df1.groupby("album_id").size())

for i,row


