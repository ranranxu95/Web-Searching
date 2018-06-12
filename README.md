# Web-Searching

## Environment
python 3.x<br>
MongoDB (db version 3.x)<br>
&nbsp;  username: LHY<br>
&nbsp;  password: 9713<br>
NodeJs 10.x<br>
bootstrap<br>
koa2<br>

## 	Execution
run spider: cd finance_spider/ && ./start.sh

Website Demo:<br> 
1.cd NewsAggregationWebsiteKoa2 && npm install <br>
2.cd PhoenixNews && python3 main.py <br>
3.cd NewsAggregationWebsiteKoa2 && npm start <br>
4.surf on http://localhost:3000/ to view website demo

## Update Record
0612-LHY-Now the front-end read data from MongDB, we need XRC to modify it to read data from MySQL<br>
0611-LHY-Website demo running<br>
0611-LHY-Needs to connect to DB and develop searching function

## Project Description
In this project, you are asked to build a simple financial news website. All your data should be crawled from the following websites. These are some Chinese financial news websites. Note that for each website we give, you need to crawl all the news starting from year 2015 (including 2015) up to now.

## Data format
Your data should be stored in plain text format. Each line should be a json of one document. For each document json should be like, doc= {“content”: “xxx”, “source”: “xxx”, “time”: “xxx”, “title”: “xxx”, “url”: “xxx”}.


## Project requirements
0. (Basic) For each website we give, you need to crawl all the news starting from year 2015 (including 2015) up to now.
1. (about 30% scores) Support several search methods. Firstly, user can just input some keywords, you need to search these keywords in the whole database and return a list of news. Secondly, user can choose search in the title or search in everywhere. Thirdly, users can limit which year of news they want when doing search. 
2. (about 20% scores) Manually design or automatic generate proper categories and classify the crawled news into those categories. 
3. (about 30% scores) Support news recommendation. After reading one or more piece of news, you need to find topics which are interesting for this user and recommend some piece of news. 
4. (about 20% scores) Your system should work in real-times. This means when one of the above websites publish new articles, you can catch them into your system with little delay. 
5. (Bonus) Allow users to track some topics. When your system finds some latest articles, which are related to one of these topics, you need to generate a new web page which arranges these related articles in a good manner. Then you need to send this generated web page to user’s email. 

## Task allocation
| Name        |       Task  |
| --------   |  :----: |
| LCY       | Spider Module<br> English Project Document(Word Version)<br> Requirement0<br> R4<br>         |
| LHY        | Website Module<br>English Project Document(Word Version)<br>   R1<br> R2<br>          |
| XRC        | Database Module<br>English Project Document(Word Version)<br>  R3<br> R5<br>      |



## Chinese financial news
http://www.eastmoney.com  
东方财富网  <br> 
http://finance.sina.com.cn   
新浪财经  <br> 
http://www.10jqka.com.cn  
同花顺财经  <br> 
http://finance.qq.com  
腾讯财经  <br> 
http://www.cnstock.com  
中国证券网  <br> 
http://business.sohu.com  
搜狐财经 <br>  


