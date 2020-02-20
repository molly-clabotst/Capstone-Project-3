# DISPLAY DATA
def display(data, first = False):

    # Displaying search results
    if data.exists() == False and first==False:
        print(f'\nSorry there was no entry\n')
    for dPoint in data:
        if first == False:
            print(dPoint)
        else:
            print(f'\n{dPoint.name} is contactable at {dPoint.email}\n')