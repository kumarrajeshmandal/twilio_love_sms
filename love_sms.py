from twilio.rest import Client 
 
account_sid = 'AC592c7a5359f34db44616f78adede1a54' 
auth_token = '1ad4ebd5b14a8fb5404aad58069ef2e8' 
client = Client(account_sid, auth_token) 
def send_love():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='gd nit cuty girl',      
                              to='whatsapp:+919776755924' 
                              #918114618907
                              #919776755924
                          ) 
 
    print(message.sid)