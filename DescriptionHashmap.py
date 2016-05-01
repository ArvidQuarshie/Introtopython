"""
This hashmap is nothing more than "a list of buckets, which are a list of slots, which have key/value pairs in them." Take a minute to break that down to see what I mean:

"a list of buckets..."
In the hashmap function I create the aMap variable which is a list, and then I fill it with other lists...
"which are a list of slots..."
These bucket lists are empty at first, but as we add key/value pairs to the data structure they will fill with "slots" or...
"which have key/value pairs in them."
Meaning each slot inside a bucket contains a (key, value) tuple or "pair".
If this structure still doesn't make sense, take the time to draw it out on paper until you're sure you get it. In fact, doing algorithms manually on paper is a good way to make sure you understand them.

If this structure still doesn't make sense, take the time to draw it out on paper until you're sure you get it. In fact, doing algorithms manually on paper is a good way to make sure you understand them.

Now that you know how the data is structured, you just need to know the algorithm for each operation. An algorithm is the steps you take to do something to or with a data structure. It's the code that makes the data structure work. We'll go through each of these operations using the code, but a general pattern in the hashmap algorithms is this:

Convert a key to an integer using a hashing function: hash_key.
Convert this hash to a bucket number using a % (modulus) operator.
Get this bucket from the aMap list of buckets, and then traverse it to find the slot that contains the key we want.
In the case of set we do this, to replace duplicate keys, or we append to add new ones.

I will now walk through the code for the hashmap so you can understand what's going on, following function by function. Follow along and make sure you understand every line. Write an English comment above each line to make sure you understand what it's doing. This is so deceptively simple that I recommend you take the time to play with any lines of code mentioned in the following description either in the Python shell, or on paper until you get it.

new
First I start by creating a function that makes a hashmap for you, also known as an initializer. What I've done is created an aMap variable that has a list, and then I put num_buckets lists inside it. These buckets will be used to hold the contents of the hashmap as I set them. Later I use len(aMap) in other functions to find out how many buckets there are. Be sure you understand that!
hash_key
This deceptively simple function is the core of how a dict works. What it does is uses the built-in Python hash function to convert a string to a number. Python uses this function for its own dict data structure, and I'm just reusing it. You should fire up a Python console to see how it works. Once I have a number for the key, I then use the % (modulus) operator and the len(aMap) to get a bucket where this key can go. As you should know, the % (modulus) operator will divide any number and give me the remainder. I can also use this as a way of limiting giant numbers to a fixed smaller set of other numbers. If you don't get this then use Python to explore it.
get_bucket
This function then uses hash_key to find the bucket that a key could be in. Since I did % len(aMap) in the hash_key function, I know whatever bucket_id I get will fit into the aMap list. Using the bucket_id I can then get the bucket where the key could be.
get_slot
This function uses get_bucket to get the bucket a key could be in, and then it simply rolls through every element of that bucket until it finds a matching key. Once it does it returns the tuple of (i, k, v) which is the index the key was found in, the key itself, and the value set for that key. You now know enough to see how this data structure works. It takes keys, hashes and modulus them to find a bucket, then searches that bucket to find the item. This effectively cuts the amount of searching necessary to a fraction of what it would be normally.
get
This is a "convenience function" which does what most people want a hashmap to do. It uses get_slot to get the (i, k, v) and then just returns the v (value) only. Make sure you understand how the default variable works, and how the (i, k, v) in get_slot is assigned to the i, k, v variables in get.
set
To set a key/value pair all I need to do is get the bucket, and append the new (key, value) to it so it can be found later. However, I want my hashmap to allow one key at a time. To do that, first I have to find the bucket then check if this key already exists. If it does then I replace it in the bucket with the new one, and if it doesn't then I append. This is actually slower than simply appending, but more likely what a user of hashmap wants. If you wanted to allow multiple values for a key you could simply have get go through every slot in the bucket and return a list of everything it found. This is a good example of tradeoffs in design. The current version is faster on get, but slower on set.
delete
To delete a key, I simply get the bucket and search for the key in it, and delete it from the list. However, because I chose to make set only store one key/value pair I can stop when I have found one. If I had decided to allow multiple values for each key by simply appending I would have also made delete slower because I would have needed to go through every slot on delete just in case it had a key/value pair that matched.
list
The last function is simply a little debug function that prints out what's in the hashmap and should be trivial for you to understand. It just gets each bucket, then goes through each slot in the bucket.
After all of these functions I just have a little bit of testing code that makes sure they work.

Three Levels of Lists
As I mentioned in the discussion, by deciding that set will overwrite (replace) keys with new values, I have made set slower but this assumption makes all of the other functions faster. What if I wanted a hashmap that allowed multiple values for each key but still keep everything fast?

What I need to do then is establish that every slot in a bucket is a list of values. This means that I add a third level of buckets, then slots, then values. This also matches the description of this kind of hashmap because I am saying, "For every key there can be multiple values." Another way to say that is "Every key has a list of values." Since keys go in slots, then slots have lists of values and I'm done.

If you want to take this code further, then change it to support multiple values for each k




"""
