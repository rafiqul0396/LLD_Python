

accounts=[]


def transfer(source:int,destination:int,amount:int)->None:
    # step 1: get the source account
    source_account=get_account(source)

    #step 2 : update the source account
    update_account(source_account,-amount)
    
    #step 3 : open destination account 
    dest_account=get_account(destination)

    # step 4: update the destination account 
    update_account(dest_account,amount)




def get_account(id:int)->dict:
    return list(filter((lambda account:account['id']==id),accounts))[0]

def update_account(account:dict,delta:int)->None:
    account['balance']+=delta



if __name__ == '__main__':

    accounts.append({'id':1,'name':'Alice','balance':500})
    accounts.append({'id':2,'name':'Bob','balance':1000})
    transfer(2,1,500)
    print(accounts)


