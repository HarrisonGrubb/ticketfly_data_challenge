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

I've built a model based on the information availalbe, but honestly it's not very good. Rurther demographic / previous shopping information would likely help to create a more powerful model. Additionally, I would request a larger sample size, to have a deeper statistical significance behind the click prediction model. 

## Q3

Question: By how much do you think your model would improve click through rate ( defined as # of users who click on the link / total users who received the email). How would you test that?

Response: Again, I would not place an emphasis on the model built with the currently available information. While date time, user country and user past purchases are helpful fields, I would have more faith in a more complete model. 

Fortunately, click optimization is a thoroughly researched field. Before acting on models, I would recommend re-designing the study and better understanding the product's needs. While re-designing, I'd recommend focusing on a funnel approach, to holistically understand the process from email send to customer purchase. 

## Q4 

Question: Did you find any interesting pattern on how the email campaign performed for different
segments of users? Explain.

Response: 

Again, I'm not comfortable putting an emphasis on results from these preliminary models. However, the learnings from 
this preliminary work could help drive the next iteration of data gathering and modeling, and help drive this campaign 
towards customer purchases. 