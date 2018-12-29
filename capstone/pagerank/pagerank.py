import sqlite3

conn = sqlite3.connect("db_spider.sqlite")
cur = conn.cursor()

#Find the IDs that send out page rank:
#we are only interested in pages that have in and out links
cur.execute("SELECT DISTINCT FROM_ID FROM LINKS")
from_ids = list()
for row in cur:
    from_ids.append(row[0])

#Find the IDs that receive page rank
to_ids = list()
links = list()
cur.execute("SELECT DISTINCT FROM_ID, TO_ID FROM LINKS")
for row in cur:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id:          #don't consider links between a page pointing to itself
        continue
    if from_id not in from_ids:   #don't consider if the from_id is not yet in my from_ids list
        continue
    if to_id not in from_ids:     #don't consider pages pointing to pages not in my from_ids list
        continue

    #keep links that are between pages we have already retrieved
    links.append(row)

    #Keep only strongly connected components (Graph Theory)
    if to_id not in to_ids:
        to_ids.append(to_id)

#Get latest page ranks for strongly connected component
prev_ranks = dict()
for node in from_ids:
    cur.execute("SELECT NEW_RANK FROM PAGES WHERE ID = ?", (node, ) )
    row = cur.fetchone()
    prev_ranks[node] = row[0]       #dictionary like {PK/from_id/node: NEW_RANK}

#How many iterations we want to run
sval = input("Insert number of iterations: ")
if len(sval) < 1:
    sval = 52           #according to Google paper
# many = 1
many = int(sval)

#Sanity check
if len(prev_ranks) < 1:
    print("Nothing to page rank. Check data.")
    quit()

#Lets do Page Rank in memory so it is really fast
for i in range(many):
#In each iteration, compute the new page ranks
    #print(prev_ranks.items()[ : 5])
    next_ranks = dict()
    total = 0.0
    #Loop through the previous ranks
    for (node, old_rank) in list(prev_ranks.items()):       #prev_ranks = {PK/from_id/node: NEW_RANK which will be the old}
    #Compute for each PK/node
        total = total + old_rank
    #Set new_rank to 0 for each PK/node
        next_ranks[node] = 0.0
    #print(total)


    #Find the number of outbound links for each page item
    #and sent the page rank down each
    for (node, old_rank) in list(prev_ranks.items()):      #prev_ranks = {PK/from_id/node: NEW_RANK which will be the old}
        # print(node, old_rank)
        give_ids = list()       #these are the IDs we are going to give it to
        for (from_id, to_id) in links:
            if from_id != node:     #we don't want to consider links between the node and itself
                continue
            # print("    ", from_id, to_id)
            if to_id not in to_ids:
                continue
            give_ids.append(to_id)  #list of IDs the current node is going to share its goodness
        if (len(give_ids) < 1):
            continue

        #Compute how much goodness the node is going to flow outbound, based on its previous/current rank
        amount = old_rank / len(give_ids)           #len(give_ids): number of outbound links
        # print(node, old_rank, amount, give_ids)

        #Loop through all the IDs receiving goodness from current node
        for id in give_ids:
            #add the amount of page rank to each one
            next_ranks[id] = next_ranks[id] + amount


    newtot = 0
    #Now we calculate the new total
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank


    #evaporation: to avoid the PageRank algorithm being trapped in dysfunctional shapes
    #takes a fraction away from everyone and gives it back to everybody else
    evap = (total - newtot) / len(next_ranks)

    #print(newtot, evap)
    for node in next_ranks:
        next_ranks[node] = next_ranks[node] + evap

    newtot = 0
    for (node, next_rank) in list(next_ranks.items()):
        newtot = newtot + next_rank

    #Compute the per-page average chance from old rank to new rank
    #As indication of convergence of the algorithm
    totdiff = 0
    for (node, old_rank) in list(prev_ranks.items()):       #this is going to tell us the stability of the pagerank
        new_rank = next_ranks[node]                         #the more it changes between iterations, the least stable
        diff = abs(old_rank - new_rank)
        totdiff = totdiff + diff

    #Average difference in Page Rank
    avediff = totdiff / len(prev_ranks)
    print(i + 1, avediff)

    #rotate: the new ranks become old ranks
    prev_ranks = next_ranks

    #run the loop again


#The DB is updated only at the very end
#in-memory calculations make loop run extremely fast

#Put the final ranks back into the database
print(list(next_ranks.items())[ : 5])
cur.execute("UPDATE PAGES SET OLD_RANK = NEW_RANK")
for (id, new_rank) in list(next_ranks.items()):
    cur.execute("UPDATE PAGES SET NEW_RANK = ? WHERE ID = ?", (new_rank, id) )
conn.commit()
cur.close()
