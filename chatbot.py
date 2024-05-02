#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.chat.util import Chat,reflections


# In[2]:


sets = [
    [
        r"(.*)Robot",
        ["hi Human, how can I help you "]
    ],
    [
        r"(.*)question",
        ["I am here for your help"]
    ],
    
    [
        r"(.*)developed ",
        ["Eng. Malik Aleem Raza created me using Python"]
    ],
    [
        r"(.*)alive ",
        ["I am Robot, I am just a computer program . Created by Eng.Aleem"]
    ],
    
    
    [
        r"(.*)name(.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is AI Robot, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Eng. Malik Aleem Raza  created me using Python's NLTK library ","Its top secret........... ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Lahore , Pakistan',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Imran Khan"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
    
]


# In[4]:


print(reflections)


# In[5]:


my_reflections ={
    "go"        :"gone",
    "hello"     :"hey there"
}


# In[6]:


chat=Chat(sets,reflections)


# In[7]:


print(chat)


# In[8]:


chat.converse()


# In[ ]:




