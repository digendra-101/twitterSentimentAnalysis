import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import matplotlib.pyplot as plt
import nltk
nltk.download('vader_lexicon')


from streamlit_extras.add_vertical_space import add_vertical_space


# Read the CSV file into a DataFrame

with st.sidebar:
    st.title(" 👋😄Hello To My App")
    st.markdown('''
        ## About
        - This software lets you perform sentiment analysis on tweets from twitter.
        - Built with Streamlit, Python, nltk,pandas.
    ''')
    add_vertical_space(5)
    st.write("Made with ❤️ By Digendre Gendre")

def main():
    st.header("Upload your Data Below")
    

    tweets = st.file_uploader("Upload your tweets here",type="csv")
    analyzer = SentimentIntensityAnalyzer()
    # Drop the 'category' column
    if tweets is not None:
        df = pd.read_csv(tweets)


        #df.drop(columns=['category'], inplace=True)

    # Now df contains the data without the 'category' column
    #print(df.head())  # Check the first few rows of the DataFrame

    # Initialize sentiment analyzer
        #analyzer = SentimentIntensityAnalyzer()

    # Lists to store positive, negative, and neutral tweets
        positive_tweets = []
        negative_tweets = []
        neutral_tweets = []

# Function to analyze sentiment of a tweet
        def analyze_sentiment(text):
            sentiment = analyzer.polarity_scores(text)
            if sentiment['compound'] >= 0.05:
                return "positive"
            elif sentiment['compound'] <= -0.05:
                return "negative"
            else:
                return "neutral"

# Iterate over the rows of the DataFrame
        for index, row in df[:100].iterrows():
        # Check if the tweet text is not NaN
            if isinstance(row['text'], str):
                sentiment = analyze_sentiment(row['text'])  # Access the 'clean_text' column
        # Add tweet to appropriate list
                if sentiment == "positive":
                    positive_tweets.append(row['text'])
                elif sentiment == "negative":
                    negative_tweets.append(row['text'])
                else:
                    neutral_tweets.append(row['text'])

    # print(f"Positive tweets: {len(positive_tweets)}")
    # print(f"Negative tweets: {len(negative_tweets)}")
    # print(f"Neutral tweets: {len(neutral_tweets)}")

        total_data =len(df[:100])
    # print(total_data)
        total_positive_tweets = len(positive_tweets)
        total_negetive_tweets = len(negative_tweets)
        total_nutaral_tweets = len(neutral_tweets)

                        

        positive_percentage = (total_positive_tweets/total_data)*100
        negative_percentage = (total_negetive_tweets/total_data)*100
        neutral_percentage = (total_nutaral_tweets/total_data)*100

        st.write("percentage of positive tweets: ",positive_percentage,"%")
        st.write("percentage of negetive tweets: ",negative_percentage,"%")
        st.write("percentage of nutaral tweets: ",neutral_percentage,"%")

        chart_type = st.selectbox('Select Chart Type', ['--Choose an option--','pi-Chart', 'Bar Chart'],placeholder="Choose an option")
        if chart_type == "pi-Chart":
            # Display pie chart
            labels = ['Positive', 'Negative', 'Neutral']
            sizes = [positive_percentage, negative_percentage, neutral_percentage]
            explode = (0.1, 0, 0)  # explode 1st slice
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)

        elif chart_type =="Bar Chart":
             # Display bar chart
            st.subheader('Bar Chart')
            data = {'Sentiment': ['Positive', 'Negative', 'Neutral'],
                    'Percentage': [positive_percentage, negative_percentage, neutral_percentage]}
            bar_df = pd.DataFrame(data)
            st.bar_chart(bar_df.set_index('Sentiment')) 

       
          
              
        


if __name__ == '__main__':
    main()    
