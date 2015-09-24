ummmmmmmm

###API setup###


**Eve**

http://python-eve.org/quickstart.html


**Mongo DB**

http://docs.mongodb.org/manual/tutorial/install-mongodb-on-amazon/
* add mongo UN/pw for admin and regular: http://petrkout.com/linux/installing-mongodb-2-6-and-setting-up-root-user-login/ (mongod.conf instead of mongodb.conf)
`mongo
 use ummapi
 b.createUser( { "user" : "name","pwd": "pass","roles" : [ "readWrite"] })`
* add db: http://www.tutorialspoint.com/mongodb/mongodb_create_database.htm

`a`

http://stackoverflow.com/questions/18520203/connectionexception-connecting-a-eve-rest-api-to-a-mongodb-instance
