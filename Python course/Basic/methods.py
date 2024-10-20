def call():
    print('I am calling someone')
    return 'Call done'



class phone:
    price=12000
    color='Blue'#ATRIBUTES
    brand='samsung'
    features=['camera','speaker']
    
    def call(self):#methods
        print('Calling one Person')
    
    def send_sms(self,phone,sms):
        text=f'sending SMS to: {phone} ans massage:{sms}'
        return text

my_phone=phone()
print(my_phone.features)
my_phone.call()
result=my_phone.send_sms(1232,'I forgot')
print(result)