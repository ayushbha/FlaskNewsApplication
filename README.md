# FlaskNewsApplication

## Project Description

### About
Creating a website using Google News API to display news from various sources and allow users to search for news based on parameters such as:

 - Keywords
 - Publish Date Range
 - Genre
 - Source

### External libraries and APIs

 - Google News API
 - d-3 cloud library

### Front-end Technologies

 - HTML
 - CSS
 - Javascript
 - AJAX

### Back-end Technologies

 - Flask (Python)
 
 ### Home Page
The home page has a carousel that shows the latest news from all sources. This news is fetched from the Google News API. The home page also features a word cloud of top 30 most frequently appearing words in news titles. 
The home page also displays the top 5 news articles from Fox News and CNN which are fetched using Google News API. 
The button on the left is used to toggle between the home page and the search page. 

 ![Home Page](https://res.cloudinary.com/rajshah/image/upload/v1591919658/68747470733a2f2f692e6962622e636f2f6e73716e4b584a2f53637265656e2d53686f742d323032302d30352d31302d61742d32322d35302d35332e706e67_mce8lf.png
)
 
### Search Page
The search page has a form which lets users search for articles based on various parameters. Search results are displayed as cards. User can use the "Show More" and "Show Less" button to display more or less search results. On clicking each card, it expands showing additional details about a particular news articles. It also has a link which takes the user to the news website having that article. 


![Search Page](https://res.cloudinary.com/rajshah/image/upload/v1591919651/68747470733a2f2f692e6962622e636f2f3776714e5278792f53637265656e2d53686f742d323032302d30352d31302d61742d32322d35312d31352e706e67_k9osrp.png)

## Project Flow

### Fetching Data

 - Flask makes calls to the Google News API endpoint to fetch and process data.
 - AJAX is used to make asynchronous calls to Flask backend to fetch the processed data. 
 - The JSON response obtained via AJAX is processed and displayed. 
 
 ### Run code
 - Clone this github repository
 - Create your own Google News API-KEY and replace it with the "YOUR-API-KEY" in application.py
 - Start the virtual environment
 - Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`.
 - Run `python application.py` to start the server


***Here is a link to a video showing the complete functioning:*** [https://www.youtube.com/watch?v=AX00rwq-qQc&feature=youtu.be](https://www.youtube.com/watch?v=AX00rwq-qQc&feature=youtu.be)
