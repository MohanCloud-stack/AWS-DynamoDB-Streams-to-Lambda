import json


def lambda_handler(event, context):
    # TODO implement
    print(".......................")
    try:
        # 1.iterate over each record
        for record in event["Records"]:
            # 2 handle the events
            if record["eventName"] == 'INSERT':
                handle_insert(record)
            elif record["eventName"] == 'MODIFY':
                handle_modify(record)
            elif record["eventName"] == 'REMOVE':
                handle_remove(record)
        print("..........................")
    except Exception as e:
        print(e)
        print('.................')
        return "Oops!!"

def handle_insert(record):
    print('handling insert event')
    #3a Get New Image content
    newImage=record['dynamodb']['NewImage']
    #3b parse the values
    newPlayerId=newImage['playerId']['S']
    #3c print it out 
    print('New Row added with PlayerId='+newPlayerId)

    print('Done handling Insert Event')

def handle_modify(remove):

    print('handling modifed events')
    #3a parse the old image and score
    oldImage=record['dynamodb']['OldImage']
    oldScore=oldImage['score']['N']

    #3b parse oldimage and 
    newImage=record['dynamodb']['NewImage']
    newScore=record['score']['N']
    
    if oldScore!=newScore:
        print('Scores changed - oldScore=' +  str(oldScore)+', newScore='+ str(newScore))  


    print('done handling modify events')

def handle_remove(record):
    