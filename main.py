import pyrebase
def firesender(datatobesent):
    config ={
    "apiKey" : "AIzaSyCZ4ZLvcVeX6xHFf8NZZCIGhcYxveBYxmg",
    "authDomain": "connectingfiretopy.firebaseapp.com",
    "projectId": "connectingfiretopy",
    "databaseURL":"https://connectingfiretopy-default-rtdb.firebaseio.com/",
    "storageBucket": "connectingfiretopy.appspot.com",
    "messagingSenderId": "626052815508",
    "appId": "1:626052815508:web:527067a2b69a69ea9df281",
    "measurementId": "G-40C6V8W7DV"
    }
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    data = {"Age":21,"Name":"Emily","Likes Pizza":True}

    #creating data
    #database.push(data)
    #database.child("Users").child("Firstperson").set(data)

    #reading data
    #emily = database.child("Users").child("Firstperson").get()
    #print(emily.val())

    #how to update data
    database.child("Users").child("Firstperson").update({"Name":datatobesent})

    #removing data
    #deleting one value
    #database.child("Users").child("Firstperson").child("Age").remove()

    #deleting a whole node 
    #database.child("Users").child("Firstperson").remove()