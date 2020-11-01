import hashlib 

# user inputs (hash, wordlist)
input_hash = input('Enter the hash: ')
wordlist_path = input('Enter path to the wordlist: ')


#open file with error handling for wrong path or not found file
try: 
    wordlist = open(wordlist_path, 'r')
except:
    print(f'invalid path {wordlist_path}')

#variable for not found password in wordlist
password_found = False

for word in wordlist:
    encoded_word = word.encode('utf-8')

    #change word into different hashes
    md5_digest = hashlib.md5(encoded_word.strip()).digest()
    sha1_digest = hashlib.sha1(encoded_word.strip()).digest()
    sha224_digest = hashlib.sha224(encoded_word.strip()).digest()
    sha256_digest = hashlib.sha256(encoded_word.strip()).digest()
    sha384_digest = hashlib.sha384(encoded_word.strip()).digest()
    sha512_digest = hashlib.sha512(encoded_word.strip()).digest()

    #check if password is hash
    if (input_hash == md5_digest) or (input_hash == sha1_digest) or (input_hash == sha224_digest) or (input_hash == sha256_digest) or (input_hash == sha384_digest) or (input_hash == sha512_digest):
        print(f'Password was found: {input_hash} | {word}')
        password_found = False
        break

if not password_found:
    print(f'This wordlist {wordlist_path} was useless')
