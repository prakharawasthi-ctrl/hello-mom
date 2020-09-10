from twilio.rest import Client 
 
account_sid = 'ACc73d9e54962cf061fa1204c81c7b1899' 
auth_token = '3ec53b82d3c102bb3051e975b1075aec' 
client = Client(account_sid, auth_token) 
 
def send_it():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body="hello Madam I am bot ",      
                              to='whatsapp:+917398873505' 
                          ) 
 
    print(message.sid)