from csp import *
import time
import sys

#ΕΞΗΓΗΣΗ ΑΝΑΠΑΡΑΣΤΑΣΗΣ ΤΩΝ ΚΛΙΚΩΝ 

#Το 1ο κελί που συμμετέχει στην κλίκα είναι αυτό μετά την παρένθεση "(" και το τελευταίο αυτό πριν την παρένθεση ")"
#Μετά το "=" είναι η πράξη που πρέπει να γίνει και μετά την πράξη το αποτέλεσμα
#Για διευκόλυνση δεν βάζω κενά ανάμεσα 
#Πράξεις:
    # + πρόσθεση 
    # - αφαίρεση 
    # / διαίρεση (θα χρησιμοποιήσω // για ακέραια διαίρεση)
    # * πολλαπλασιασμός

#Όταν έχω cliques = ["(1,2)=-1" , "(3,6)=+5" , "(4,7)=/3" , "(5,8)=-1" , "(9,X)=&1"] σημαίνει πχ το "(3,6)=+5" ότι η τιμή του (1,3) + (2,3) = 5
#Αντίστοιχα και τα υπόλοιπα

#Όταν έχω περιορισμό μόνο για ένα κελί που πρέπει να πάρει έναν συγκεκριμένο αριθμό βάζω (αριθμό κελιού,Χ)=&τιμή. Αντι κάποιον
#τελεστή βάζω το & για διευκόλυνση στον κώδικα πχ "(9,X)=&1" σημαίνει οτι το 9ο κελί σε έναν πίνακα 3Χ3 δηλαδή το κελί (3,3) πρέπει 
#αναγκαστικά να πάρει την τιμή 1

#Θεωρώ τα κελιά του πίνακα ως:

#1 2 3 
#4 5 6 
#7 8 9 

#οπότε το κελί πχ (1,1) = 1 , το (2,1) = 4 κτλπ στον παραπάνω πίνακα

#Παραδείγματα με κλίκες για διάφορους πίνακες παρμένα από το http://www.kenkenpuzzle.com/ (Για χρήση στον κώδικα)


#3Χ3 (easiest)
#cliques = ["(1,2)=-1" , "(3,6)=+5" , "(4,7)=/3" , "(5,8)=-1" , "(9,X)=&1"]
# cliques = ["(1,4,5)=*6", "(2,3)=/3", "(6,9)=-1","(7,8)=/2"]
# cliques = ["(1,X)=&1","(2,X)=&2","(3,X)=&3","(4,X)=&3","(5,X)=&1","(6,X)=&2","(7,X)=&2","(8,X)=&3","(9,X)=&1"]

#4Χ4
#easy
# cliques = ["(1,X)=&3","(2,3)=+3","(4,7,8)=*24","(5,6)=+5","(9,13)=-1","(10,11,12)=*12","(14,X)=&3","(15,16)=/2"]
#medium
# cliques = ["(1,5)=-3", "(2,6)=-2", "(3,4)=/2","(7,11)=+3","(8,12)=-1","(9,10,13)=*12","(14,15,16)=*12",]
#hard
# cliques = ["(1,2)=-1", "(3,4,8)=*12", "(5,6,7)=+7","(9,13)=/2","(10,X)=&4","(11,12)=-1","(14,15)=-1","(16,X)=&1"]

#5X5
#easy
#cliques = ["(1,6)=-2", "(2,3,4)=*24", "(5,10)=+6","(7,X)=&5","(8,13)=/2","(9,14)=/2","(11,X)=&5","(12,17,18)=*9","(15,19,20)=*40","(16,21)=/2","(22,23)=-1","(24,25)=+4"]
#medium
# cliques = ["(1,6)=/2", "(2,3)=+9", "(4,5,10)=*24","(7,8,12,13)=*30","(9,X)=&1","(11,16)=-1","(14,15)=-2","(17,18,23)=*8","(19,20)=-4","(21,22)=-2","(24,25)=-2"]
cliques = ["(1,6)=-2", "(2,7)=-3", "(3,4,5)=*6","(8,9)=+9","(10,15)=/2","(11,12)=-1","(13,14)=-4","(16,21)=-3","(17,18,22)=*20","(19,24)=-1","(20,25)=-2","(23,X)=&1"]

#Με αυτή τη συνάρτηση βρίσκουμε από την συμβολοσειρά που έχουμε για να ορίσουμε τις κλίκες
#ποια κελία είναι γείτονες με ποια λόγω των κλικων και βάζουμε σε έναν πίνακα τα ints πλεον 
#αριθμούς. Χρησιμοποιούμε τον χαρακτήρα '|' ώστε να διαχωρίζουμε τις κλίκες .
#Πχ για δοσμένο string cliques = ["(1,2)=-1" , "(3,6)=+5" , "(4,7)=/3" , "(5,8)=-1" , "(9,X)=1"]
#Ο πίνακας που επιστρέφει η συνάρτηση είναι:
#   ['|',1,2,'|',3,6,'|',5,8,'|',9,'|']
def str_to_list(cliques):
    num_of_cliques = len(cliques) 

    neighbors_list = ['|']

    for j in range(0,num_of_cliques):
       
        cl = cliques[j]
    
        i = 0
        sum = ''

        while cl[i] != ')':
            if cl[i] == ',':
                neighbors_list.append(sum)
                sum = ''
            elif cl[i] != '(' and cl[i] != 'X':
                sum = sum + cl[i]   
            i = i + 1
            if cl[i] == ')':
                if sum != '':
                    neighbors_list.append(sum)
                neighbors_list.append('|')

    for x in range(0,len(neighbors_list)):
        if neighbors_list[x] != '|':
            neighbors_list[x] = int(neighbors_list[x])
        
    return neighbors_list  

#Η συνάρτηση αυτή μετατρέπει τα κελία (i,j) στον ακέραιο που του αντιστοιχεί
#Πχ για πίνακα 3Χ3 το (1,1)->1 , (2,1)->4 κτλπ
def from_ij_to_k(A,n):
    
    list_with_i_j = [] #Λίστα με όλα τα κελία με τη σειρά σε μορφή (i,j)

    for i in range(1,n+1):
        for j in range(1,n+1):
            list_with_i_j.append((i,j))

    return list_with_i_j.index(A)+1   


class Kenken(CSP):
    
    def __init__(self,n,cliques): #Ορίσματα είναι το πλάτος του πίνακα και οι κλίκες

        #Πρέπει να οριστούν αφού είναι CSP πρόβλημα
        self.variables = []
        self.domains = {}
        self.neighbors = {} 

        #Βοηθητικά 
        self.n = n
        self.cliques = cliques
        self.cl_n = {}
        #Για σύγκριση αλγορίθμων 
        self.wrong_val = 0

        #Εύρος τιμών -> Domains 

        #Τα κελία παίρνουν τιμές από 1 μέχρι το πλάτος του πίνακα 
        for i in range(1,n+1):
            for j in range(1,n+1):
                self.domains[(i,j)] = list(range(1,n+1))

        #Εύρεση γειτόνων 
        my_list = []
        list_cn = []
        neig_list = str_to_list(cliques)

        for i in range(1,n+1):
            for j in range(1,n+1):
                my_list.append((i,j))

        new_list = []
        list_cn = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                for v in range(0,len(my_list)):
                    
                    #Αν βρίσκονται στην ίδια γραμμή/στήλη
                    if my_list[v][0] == i and my_list[v][1] != j: #Αν βρίσκονται στην ίδια γραμμή αλλά δεν είναι το ίδιο το κελί
                        new_list.append(my_list[v])
                    if my_list[v][1] == j and my_list[v][0] != i: #Αν βρίσκονται στην ίδια στήλη αλλά δεν είναι το ίδιο το κελί
                        
                        new_list.append(my_list[v])
                    
            # Αν βρίσκονται στην ίδια κλίκα 
            #Θεωρώ ότι όλα τα κελία συμμετέχουν σε κλίκες 
            #και ότι κάθε κελί συμμετέχει σε μόνο μία κλίκα 

                #Αντιστοίχηση του (1,1)->1 , (2,1)->4 , (1,2)->2 κοκ
                #neig_list[index2] = 1 και my_list[index] = (1,1)
                index = my_list.index((i,j))
                index2 = neig_list.index(index + 1)
                
                b = index2 - 1 #Κινούμαστε στον πίνακα με τους γείτονες από τη θέση που βρίσκεται το κελί που εξετάζουμε μέχρι
                #να βρούμε '|' άρα δεν θα έχει άλλους γείτονες προς τα πίσω 
                while neig_list[b] != '|':
                    
                    list_cn.append(my_list[neig_list[b]-1])
                    if my_list[neig_list[b]-1] not in new_list: #Δεν θέλουμε ένα κελί να μπει 2 φορές γείτονας σε ένα άλλο
                        new_list.append(my_list[neig_list[b]-1])
                    
                    if b > 0:
                        b = b - 1

                f = index2 + 1 #Κινούμαστε στον πίνακα με τους γείτονες από τη θέση που βρίσκεται το κελί που εξετάζουμε μέχρι
                #να βρούμε '|' άρα δεν θα έχει άλλους γείτονες προς τα μπροστα 
                while neig_list[f] != '|':

                    list_cn.append(my_list[neig_list[f]-1])       
                    if my_list[neig_list[f]-1] not in new_list: #Δεν θέλουμε ένα κελί να μπει 2 φορές γείτονας σε ένα άλλο
                        new_list.append(my_list[neig_list[f]-1])
                    if f < len(neig_list):
                        f = f + 1               

                self.neighbors[(i,j)] = new_list
                self.cl_n[(i,j)] = list_cn

                new_list = []
                list_cn = []

        #Ορισμός των variables 
        #Μια λίστα με [(1,1),(1,2),...,(n,n)]
        self.variables = my_list
        
        CSP.__init__(self,self.variables,self.domains,self.neighbors,self.constraints_func)
        
    def constraints_func(self,A ,a, B,b ):
        
        #Θα κρατάω για κάθε κλίκα με άθροισμα ή πολλαπλασιασμό ένα directory με key:το 1ο κελί(c[1]) που
        #συμμετέχει στην κλίκα και value το μέχρι τώρα άθροισμα που πρέπει να είναι ίσο με result τελικά και 
        #ποια κελία έχουν συμμετάσχει μέχρι τώρα  
        temp_res_add = {}
        temp_res_mult = {}
        

        #Μετατροπή από (i,j) σε k
        new_A = from_ij_to_k(A,self.n)
        new_B = from_ij_to_k(B,self.n)

        #Μετατροπή από int σε string     
        new_A = str(new_A)
        new_B = str(new_B)

        for c in cliques: #Αρχικοποίηση
            temp_res_add[c[1]] = [0]
            temp_res_mult[c[1]] = [0]

        #Αν βρίσκονται στην ίδια γραμμή ή στήλη δεν γίνεται να έχουν την ίδια τιμή 
        if A[0] == B[0] or A[1] == B[1]:
            if a == b : 
                self.wrong_val = self.wrong_val + 1
                return False

        #Έλεγχος αν είναι στην ίδια κλίκα 
        for c in cliques:
            
            temp = ['('] #Μια λίστα με έναν έναν χαρακτήρα από κάθε κλίκα 
            j = 1
            sum = ''
            for i in range(1,len(c)):
                if c[i] == ',' or c[i] == ')':
                    if len(temp) == 1: #Βάζω τον 1ο αριθμό
                        temp.append(sum)
                    else: #Πρέπει να βάλω ένα κόμμα πριν τον αριθμό
                        temp.append(',')
                        temp.append(sum)
                    sum = ''
                else:
                    sum = sum + c[i]
            temp.append(')')
            #Μέχρι εδώ η λίστα temp έχει τη μορφή πχ ['(', '3', ',', '4', ')', '=', '/', '2']
            
            #Δεν χρησιμοποιώ μονο την εντολή list(c) γιατί όταν σαν string c = "(14,15,16)=*12" 
            #το 14 πχ στη λίστα το δείχνει ως [...,'1','4',....] και δεν το θέλουμε έτσι 
            temp2_list = list(c) #Βοηθητική για να βρώ το '=' ώστε να πάρω και το αποτέλεσμα και την πράξη
            eq = temp2_list.index('=') #Βρίσκω την θέση που υπάρχει ο τελεστής '='
            operator = c[eq+1] #Ο τελεστής σύμφωνα με την κλίκα
            # result = c[eq+2] #Το αποτέλεσμα σύμφωνα με την κλίκα
            # result = int(result) #Το αποτέλεσμα που αναμένεται είναι ακέραιος 

            #Προσθέτω στη λίστα και το '=' , τον τελεστή και το αποτέλεσμα 
            temp.append('=')
            temp.append(operator)
            op_pos = temp2_list.index(operator)
            x = op_pos + 1
            sum2 = ''
            while x < len(temp2_list):
                sum2 = sum2 + temp2_list[x]
                if x < len(temp2_list):
                    x = x + 1 

            temp.append(sum2)
            result = int(sum2)
            
            #Αν υπάρχουν και οι 2 μέσα στον πίνακα και δεν είναι στην τελευταια θέση άρα δεν είναι το αποτέλεσμα 
            #αλλά αριθμός κελιού σημαίνει ότι βρίσκονται στην ίδια κλίκα 
            if new_A in temp and new_B in temp and temp.index(new_A) != len(temp)-1 and temp.index(new_B) != len(temp)-1: 
                
                if operator == '/': #Όταν έχω διαίρεση πρέπει το αποτέλεσμα να είναι ίσο με την ακέραια διαίρεση του μεγάλυτερου προς το μικρότερο 
                    
                    maximum = max(a,b)
                    minimum = min(a,b)
                    if result == (maximum // minimum):
                        return True
                    else:
                        self.wrong_val = self.wrong_val + 1
                        return False

                elif operator == '-': #Παίρνω απόλυτη τιμή 
                    
                    if result == abs(a-b):
                        return True
                    else:
                        self.wrong_val = self.wrong_val + 1
                        return False

                elif operator == '+': #Αν το άθροισμα των τιμών είναι μεγαλύτερο από το αποτέλεσμα που απαιτείται είναι λάθος 
                        
                    if (a+b) > result: #Αυτό είναι σίγουρα λάθος
                        self.wrong_val = self.wrong_val + 1
                        return False
                    else:
                        
                        #Γείτονες του Α λόγω κλίκας (αφού βρίσκονται στην ίδια κλίκα έχουν τους ίδιους γείτονες κλίκας οπότε αρκει η διαδικασία να γίνει για το ένα από τα 2)
                        n_listA = self.cl_n.get(A)

                        #(i,j):τιμή για (i,j) που έχουν πάρει τιμές μέχρι τώρα
                        z = kenken.infer_assignment()

                        flag = True
                        flag2 = False
                        countA = 0
                        countB = 0
                        s = a #Αρχικά είναι όσο είναι η τιμή του a (το b θα προστεθεί μετά αφού είναι γείτονας κλίκας του a)
                        for x in n_listA:
                            k = z.get(x)  #Παίρνω την τιμή του κάθε γείτονα που έχει συμμετάσχει στην κλίκα μέχρι τώρα
                            if k == None: #Υπάρχει τουλάχιστον ένας γείτονας που δεν έχει συμμετάσχει ακόμα στην κλίκα
                                if x == B: #Το Β δεν έχει συμμετάσχει ακόμα 
                                    flag2 == True
                                flag == False
                            else:
                                s = s + k #Συνολικό άθροισμα τιμών 
                        if flag == True:
                            if s == result:
                                return True
                        if flag2 == True:
                            s = s + b 
                        if s < result:
                            return True
                        else:
                            self.wrong_val = self.wrong_val + 1
                            return False

                        
                elif operator == '*': #Αν το γινόμενο των τιμών είναι μεγαλύτερο από το αποτέλεσμα που απαιτείται είναι λάθος
                    
                    if (a*b) > result: #Αυτό είναι σίγουρα λάθος
                        self.wrong_val = self.wrong_val + 1
                        return False
                    else:
                            
                    #Γείτονες του Α λόγω κλίκας (αφού βρίσκονται στην ίδια κλίκα έχουν τους ίδιους γείτονες κλίκας οπότε αρκει η διαδικασία να γίνει για το ένα από τα 2)
                        n_listA = self.cl_n.get(A)

                        #(i,j):τιμή για (i,j) που έχουν πάρει τιμές μέχρι τώρα
                        z = kenken.infer_assignment()

                        flag = True
                        flag2 = False
                        countA = 0
                        countB = 0
                        s = a #Αρχικά είναι όσο είναι η τιμή του a (το b θα προστεθεί μετά αφού είναι γείτονας κλίκας του a)
                        
                        for x in n_listA: 
                            k = z.get(x)  #Παίρνω την τιμή του κάθε γείτονα που έχει συμμετάσχει στην κλίκα μέχρι τώρα
                            if k == None: #Υπάρχει τουλάχιστον ένας γείτονας που δεν έχει συμμετάσχει ακόμα στην κλίκα

                                if x == B: #Το Β δεν έχει συμμετάσχει ακόμα
                                    flag2 == True
                                flag == False
                            else:
                                s = s * k #Συνολικό γινόμενο τιμών 
                        
                        if flag == True: #Έχουν συμμετάσχει όλα τα κελία στην κλίκα 
                            if s == result: #Πρέπει πλέον το γινόμενο των τιμών να είναι ίσο με το αναμενόμενο αποτέλεσμα 
                                return True
                        if flag2 == True: #Αν δεν είχε συμμετάσχει ακόμα το B 
                            s = s * b #Συνυπολογίζουμε την τιμή του 
                        if s < result:
                            return True
                        else:
                            self.wrong_val = self.wrong_val + 1
                            return False
                        
            #Αν ένα από τα 2 πρέπει να πάρει συγκεκριμένη τιμή  
            elif operator == '&': #Ο operator είναι το & άρα πρέπει να έχουμε ισότητα είτε για το Α είτε για το Β ανάλογα 
                op_index = temp.index(operator) #Η θέση του & στον πίνακα 
                #Η θέση του κελίου που πρέπει να πάρει συγκεκριμένη τιμή 
                num_pos = op_index - 5 #Είναι πάντα μείον 5 αφού η "ισότητα" είναι για ένα κελί οπότε πάντα έχει τη μορφη (num,X)=&y

                if temp[num_pos] == new_A: #Κοιτάω ποιο από τα 2 ορίσματα είναι αυτό με την συγκεκριμένη τιμή
                    if a == result:
                        return True
                    else:
                        self.wrong_val = self.wrong_val + 1
                        return False
                elif temp[num_pos] == new_B:
                    if b == result:
                        return True
                    else:
                        self.wrong_val = self.wrong_val + 1
                        return False 
            
        return True #Αν δεν έχει επιστραφεί κάτι μέχρι τώρα επιστρέφεται true αφού δεν υπάρχει κάποιο πρόβλημα 

    def display(self, assignment):
        
        print('SOLUTION')
        for i in range(1,self.n+1):
            for j in range(1,self.n+1):
                print('|',end='')
                print(assignment.get((i,j)),end='')  
                print('|',end='')
            print() 
            
if __name__=='__main__': 

    n = input('Give n (length of the square) based on the clique you chose:')
    n = int(n)

    print('..............')
    kenken = Kenken(n, cliques)
    start_time = time.time()
    backtracking_search(kenken)
    print("Algorithm = BT | Time = " + str((time.time() - start_time)) + " | Consistency checks = " + str(kenken.wrong_val) + " | Number of nodes visited = " + str(kenken.nassigns))
    print('..............')

    print('..............')
    kenken = Kenken(n, cliques)
    start_time = time.time()
    backtracking_search(kenken, inference=forward_checking)
    print("Algorithm = FC| Time = " + str((time.time() - start_time)) + " | Consistency checks = " + str(kenken.wrong_val) + " | Number of nodes visited = " + str(kenken.nassigns))
    print('..............')

    kenken.display(kenken.infer_assignment())
