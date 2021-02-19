
# coding: utf-8

# # while loops
# 
# The **while** statement in Python is one of most general ways to perform iteration.
#  A **while** statement will repeatedly execute a single statement or group of 
# statements as long as the condition is true. The reason it is called a 'loop' 
# is because the code statements are looped through over and over again until the condition is no longer met.
# 
# The general format of a while loop is:
# 
#     while test:
#         code statement
#     else:
#         final code statements
# 
# Let’s look at a few simple while loops in action. 
# https://www.learnpython.org/en/Loops

# In[2]:


x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1


# Notice how many times the print statements occurred and how the while loop kept going until the True condition was 
# met, which occurred once x==10. Its important to note that once this occurred the code stopped. 
# Lets see how we could add an else statement:

# In[3]:


x = 0

while x < 10:
    print ('x is currently: ',x)
    print (' x is still less than 10, adding 1 to x')
    x+=1
    
else:
    print ('All Done!')


# #break, continue, pass
# 
# We can use break, continue, and pass statements in our loops to add additional functionality for various cases. 
# The three statements are defined by:
# 
#     break: Breaks out of the current closest enclosing loop.
#     continue: Goes to the top of the closest enclosing loop.
#     pass: Does nothing at all.
#     
#     
# Thinking about **break** and **continue** statements, the general format of the while loop looks like this:
# 
#     while test: 
#         code statement
#         if test: 
#             break
#         if test: 
#             continue 
#     else:
# 
# **break** and **continue** statements can appear anywhere inside the loop’s body,but we will usually 
# put them further nested in conjunction with an **if** statement to perform an action based on some condition.
# 
# Lets go ahead and look at some examples!

# In[6]:


x = 0

while x < 10:
    print ('x is currently: ',x)
    print (' x is still less than 10, adding 1 to x')
    x+=1
    if x ==3:
        print ('x==3')
    else:
        print ('continuing...')
        continue


# Note how we have a printed statement when x==3, and a continue being printed out as we 
# continue through the outer while loop. Let's put in a break once x ==3 and see if the result makes sense:

# In[7]:


x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x ==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue


# Note how the other else statement wasn't reached and continuing was never printed!
# 
# After these brief but simple examples, you should feel comfortable using while statements in your code.
# 
# **A word of caution however! It is possible to create an infinitely running loop with while 
# statements. For example:**

# In[ ]:


# DO NOT RUN THIS CODE!!!! 
while True:
    print ('Uh Oh infinite Loop!')



customers = [
    dict(id=1, total=200, coupon_code='F20'), # F20: fixed, $20
    dict(id=2, total=150, coupon_code='P30'), # P30: percent, 30%
    dict(id=3, total=100, coupon_code='P50'), # P50: percent, 50%
    dict(id=4, total=110, coupon_code='F15'), # F15: fixed, $15
]
for customer in customers:
    code = customer['coupon_code']
    if code == 'F20':
        customer['discount'] = 20.0
    elif code == 'F15':
        customer['discount'] = 15.0
    elif code == 'P30':
        customer['discount'] = customer['total'] * 0.3
    elif code == 'P50':
        customer['discount'] = customer['total'] * 0.5
    else:
        customer['discount'] = 0.0
for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])


