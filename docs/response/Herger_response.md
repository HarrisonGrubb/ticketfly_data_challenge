# Ticketfly Data Challenge
Brendan Herger

13herger@gmail.com

## Q1

Question: What percentage of users opened the email and what percentage clicked on the link within the email?

Response: 

Here's a table showing how many users opened the email, and how many clicked the link:
```
|                    | opened email | did not open email |
|--------------------|--------------|--------------------|
| clicked link       | 149          | 117                |
| did not click link | 133          | 136                |
```

Altogether, 282 people opened the email, and 266 clicked the link. Interestingly, it would appear that 117 users did not open the email, but did click the link. This might suggest an issue with data gathering.
 
## Q2
Question: The head of marketing thinks that it is stupid to send emails to a random subset and in a random way. Based on all the information you have about the emails that were sent, can you build a model to optimize in future email campaigns to maximize the probability of users clicking on the link inside the email?

Response:

It is worth noting that sending emails out randomly is an effective way of gathering data without introducing a bias. 

It would be possible to build a model to predict email opens and clicks from this data, but it would be helpful to know more about the user building out a model. For example, further demographic / previous shopping information would likely help to create a more predictively powerful model.
 
Additionally, I would 

## Q3

Question: By how much do you think your model would improve click through rate ( defined as # of users who click on the link / total users who received the email). How would you test that?

Response: Again, I would not place an emphasis on the model built with the currently available information. While date time, user country and user past purchases are helpful fields, 