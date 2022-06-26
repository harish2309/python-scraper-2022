# python-scraper-2022
Good


In this article, we will discuss the lxml python library to scrape data from a webpage, which is built on top of the libxml2 XML parsing library written in C. When compared to other python web scraping libraries like BeautifulSoup and Selenium, the lxml package gives an advantage in terms of performance. Reading and writing large XML files takes an indiscernible amount of time, making data processing easier & much faster.

We will be using the lxml library for Web Scraping and the requests library for making HTTP requests in Python. These can be installed in the command line using the pip package installer for Python.

Getting data from an element on the webpage using lxml requires the usage of Xpaths.

![image](https://user-images.githubusercontent.com/36474847/175803768-0af4daaa-0cee-4903-b719-edabae3c6545.png)


To access file 1,

C:/File1
Similarly, To access file 2,

C:/Documents/User1/File2
Now consider a simple web page,


`<html>
<head>
	<title>My page</title>
</head>
<body>
	<h2>Welcome to my page<h2>
	<a href="www.example.com">page</a>
		
<p>This is the first paragraph</p>

	<h2>Hello World</h2>
</body>
</html>`

![image](https://user-images.githubusercontent.com/36474847/175803875-315c1905-77c8-42f7-9e75-ffca8919d07d.png)


`XPath : html/body/p/text()
Result : This is the first paragraph`


For getting a value inside the <href> attribute in the anchor or <a> tag,

`XPath : html/body/a/@href
Result: www.example.com`
For getting the value inside the second <h2> tag,

`XPath : html/body/h2[2]/text()
Result: Hello World`
  
  
 To find the XPath for a particular element on a page:
Right-click the element in the page and click on Inspect.
Right click on the element in the Elements Tab.
Click on copy XPath.
Using LXML
Step-by-step Approach
We will use requests.get to retrieve the web page with our data.
We use html.fromstring to parse the content using the lxml parser.
We create the correct XPath query and use the lxml xpath function to get the required element.
Example 1:

Below is a program based on the above approach which uses a particular URL.
  
  
`# Import required modules
from lxml import html
import requests
  
# Request the page
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
  
# Parsing the page
# (We need to use page.content rather than 
# page.text because html.fromstring implicitly
# expects bytes as input.)
tree = html.fromstring(page.content)  
  
# Get element using XPath
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
print(buyers)`
  
  
  ![image](https://user-images.githubusercontent.com/36474847/175803910-21037196-5392-48ef-a9fd-54e21e403b31.png)

  
  
`# Import required modules
from lxml import html
import requests
  
# Request the page
page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
  
# Parsing the page
tree = html.fromstring(page.content)
  
# Get element using XPath
prices = tree.xpath(
    '//div[@class="col-sm-4 col-lg-4 col-md-4"]/div/div[1]/h4[1]/text()')
print(prices)
  `
  
