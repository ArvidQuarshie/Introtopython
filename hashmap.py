def new(num_buckets=256):
    """ Initializes a map with the given number of buckets. """
    aMap[]
    for i in range(0,num_buckets):
        aMap.append([])
        return aMap

def hash_key(aMap,key):
    #given a key this will create a number then convert it into an index for the
    #aMaps buckets
    return hash(key) %len(aMap)
def get_bucket(aMap,key):
    #given a key ,find the bucket where it would go
    bucket_id=hash_key(aMap,key)
    return aMap[bucket_id]
def get_slot(aMap,key,default=None):
    """ Returns the index , key and value of a slot found in a bucket
       return -key and default (None if not set) when not found """
    bucket=get_bucket(aMap,key)
    for i, kv in enumerate(bucket):
        k,v =kv
        if key==k:
            return i,k,v
        return -1,key,default
def get(aMap,key,default=None):
    #gets the value in a bucket for the given key or default
    i,k,v=get_slot(aMap,key,default)
    return v
def set(aMap,key,value):
    #sets the key to the value, replacing any existing value
    bucket=get_bucket(aMap,key)
    i,k,v=get_slot(aMap,key)
    if i>=0:
        #the key exists replace it
        bucket[i]=(key,value)
    else:
        #the key does not ,append to create it
        bucket.append((key,value))
def delete(aMap,key):
    """deletes the given key from the map"""
    bucket=get_bucket(aMap,key)
    for i in xrange(len(bucket)):
        k,v=bucket[i]
        if key==k:
            del bucket[i]
            break
def list(aMap):
    """prints out what is in the map """
    for bucket in aMap:
        if bucket:
            for k,v in bucket:
                print k,v

