
# coding: utf-8

# In[ ]:


def piglatin(word):
    '''
    type a single word (as a string) to translate into pig latin
    '''
    if word[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
        return(word + 'ay')
    else:
        return(word[1:] + word[0] + 'ay')

