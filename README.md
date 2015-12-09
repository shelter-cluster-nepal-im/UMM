###Links and Documentation###

**Map**
A POC version of a map showing locations of data submissions is available here: http://nepalsheltercluster.org/umm/map.html

**Documentation**
A broad view of the UMM vision is avaiable here:


###API setup###


**Eve**

http://python-eve.org/quickstart.html


**Mongo DB**

http://docs.mongodb.org/manual/tutorial/install-mongodb-on-amazon/
* add db: http://www.tutorialspoint.com/mongodb/mongodb_create_database.htm and admin user

`db.createUser({user:"admin", pwd:"secret_password", roles:[{role:"root", db:"admin"}]})`

* add mongo UN/pw for admin and regular: http://petrkout.com/linux/installing-mongodb-2-6-and-setting-up-root-user-login/ (mongod.conf instead of mongodb.conf)

`mongo
 use ummapi
 b.createUser( { "user" : "name","pwd": "pass","roles" : [ "readWrite"] })`
 
 *Auth username/pw encoder/decoder:  https://www.base64encode.org/
 


http://stackoverflow.com/questions/18520203/connectionexception-connecting-a-eve-rest-api-to-a-mongodb-instance
