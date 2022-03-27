from twilio.rest import Client 
 
account_sid = 'AC7618fb282a3885a28221ae37b1ef50c8' 
auth_token = 'd19e1459665599617c3aab2bcd707b86' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG356cb41e1db8fd41a1d6cfe23a3a339e', 
                              body='\nWelcome to Quran Radio \n\n Choose a Number to play \n\n1) Quran Kareem\n2) Mahmoud Abdel Hakam\n3) Shiekh Sharawi\n4) Shiekh Gaber\n5) Shiekh Hosary\n6) Shiekh Ref3at\n7) Shiekh Abdel Basat',      
                              to='+13136105280' 
                          ) 
 
print(message.sid)