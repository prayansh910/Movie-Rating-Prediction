

##Identify missing values:
df.isnull().sum()


df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})')

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

df['Year']=df['Year'].fillna(df['Year'].median())

df['Genre']=df['Genre'].fillna('Unknown')

df['Duration'] = df['Duration'].astype(str).str.extract('(\d{2,3})')  # Extracts 2–3 digit number

df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

df['Rating'] = df['Rating'].fillna(df['Rating'].median())

df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')

df['Votes'] = df['Votes'].fillna(df['Votes'].median())

df['Director'] = df['Director'].fillna('Unknown')
df['Actor 1'] = df['Actor 1'].fillna('Unknown')
df['Actor 2'] = df['Actor 2'].fillna('Unknown')
df['Actor 3'] = df['Actor 3'].fillna('Unknown')
