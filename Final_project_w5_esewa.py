#!/usr/bin/env python
# coding: utf-8

# # Data Analysis 
# 
# ## Importing Necessary libraries

# In[45]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# ## Importing the Dataset

# In[46]:


df = pd.read_csv(r"C:\Users\KIIT0001\Downloads\archive\SalesForCourse_quizz_table.csv")
df.head()


# In[47]:


df.describe()


# In[48]:


df.info()


# ## Checking null values 

# In[49]:


df.isnull().sum()


# ## Removing year and month since both included in Date and unnamed column1 since  alot of null values 

# In[50]:


df.drop(['Column1','Year','Month'], axis=1, inplace=True)



# In[52]:


df.head()


# In[53]:


for col in df.columns:
    if df[col].dtype == 'object':  # Assuming object type columns might have dates
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass  # If conversion fails, the column remains unchanged

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['number'])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Create and display the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()


# ### Removing high correlatioins 

# In[54]:


df.drop(['Unit Price', 'Revenue'], axis=1, inplace=True)


# In[55]:


df.head()


# ## Boolean encoding column : Costumer Gender (Feature Engineering)

# In[56]:


df=pd.get_dummies(df,columns=['Customer Gender'],drop_first=True)
df.head()


# In[57]:


plt.figure(figsize=(10, 6))
sns.countplot(x='Customer Gender_M', data=df, palette=['Pink', 'skyblue'])
plt.title('Distribution of Customer Gender')
plt.xlabel('Gender is male')
plt.ylabel('Count')
plt.show()


# In[61]:


grouped = df.groupby(['Country', 'Product Category']).size().reset_index(name='Count')

# Generate separate pie charts for each country
for country in grouped['Country'].unique():
    country_data = grouped[grouped['Country'] == country]

    plt.figure(figsize=(6, 6))
    plt.pie(country_data['Count'], labels=country_data['Product Category'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title(f'Category Distribution in {country}')
    plt.show()


# In[62]:


print(df['Sub Category'].unique())  


# In[70]:


sns.histplot(df['Customer Age'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Customer Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# In[72]:


category_sales = df.groupby('Sub Category')['Customer Age'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=category_sales.index, y=category_sales.values)

plt.title('Famous Sub Category by customers age')
plt.xlabel('Sub Category')
plt.ylabel('Customer Age')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ## Customer gender and Popularity of various Sub Categories Comparison

# In[66]:


grouped = df.groupby(['Customer Gender_M', 'Sub Category']).size().reset_index(name='Count')

plt.figure(figsize=(12, 6))
sns.barplot(x='Customer Gender_M', y='Count', hue='Sub Category', data=grouped, palette='tab10')


plt.title('Popularity of Sub Categories Across Customer Genders')
plt.xlabel('Customer Gender_M')
plt.ylabel('Count')


plt.xticks(rotation=45)
plt.tight_layout()


plt.show()


# In[67]:


country_quantity = df.groupby('Country')['Quantity'].sum().reset_index()


plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='Quantity', data=country_quantity, palette='tab10')

plt.title('Total Quantity Sold in Each Country Comparison')
plt.xlabel('Country')
plt.ylabel('Quantity')



plt.tight_layout()


plt.show()


# In[68]:


df['Date'] = pd.to_datetime(df['Date'])

date_quantity = df.groupby('Date')['Quantity'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Quantity', data=date_quantity, linestyle='solid', color='skyblue')

plt.title('Quantity Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Total Quantity')

plt.tight_layout()
plt.show()


# In[ ]:




