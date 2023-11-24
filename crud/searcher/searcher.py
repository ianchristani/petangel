from ..models import EventModel

def eventSearcher(user) -> list:
    # splitting the events
    events = EventModel.objects.all()
    foundEvents = events.exclude(author = user)
    lostEvents = events.filter(author = user)

    # aux list
    auxlist = []
      
    # there will be just one pet here in one of the for loops (site's not spaming policy)
    for lostPet in lostEvents:    
        for foundPet in foundEvents:
            # from lost to found
            if lostPet.lost == True and foundPet.found == False:
                try:
                    if foundPet.neighborhood == lostPet.neighborhood and foundPet.date >= lostPet.date and foundPet.type == lostPet.type:
                        auxlist.append(foundPet)
                except:
                    print("no result was found")
                return auxlist
            # from found to lost
            if lostPet.lost == False and foundPet.found == False:
                try:
                    if foundPet.neighborhood == lostPet.neighborhood and foundPet.date <= lostPet.date and foundPet.type == lostPet.type:
                        auxlist.append(foundPet)
                except:
                    print("no result was found")
                return auxlist