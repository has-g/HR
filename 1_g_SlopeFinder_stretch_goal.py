'''
Stretch goals:
1) The above problem was for solving a static diagram. Can we move from static polygon to a generic polygon,
i.e. input is long list of co-ordinates, and have the program construct all lines from those points?
Assumption: optimised for speed, not space


(2,6)           (5,6)
A  ----------- B
\                *
 \                     * E (7,5)
  \
   \                 *
   C ----------- D
   (3,4)         (6,4)

'''

def calculate_gradient(t1, t2):
   d_y = t2[1] - t1[1]
   d_x = t2[0] - t1[0]
   # same point
   if t1 == t2: return 'samePoint'

   # line parallel to y axis - avoiding division by zero
   if d_x == 0: return 'undefined'
   # *1.00 multiplication to force python 2.* to not floor the division
   #return (round(((d_y * 1.00)/float(d_x)), 2))
   m = round((float(d_y)/float(d_x)), 2)
   return m


all_coordinates = {'A': (2, 6),
                  'B': (5, 6),
                  'C': (3, 4),
                  'D': (6, 4),
                  'E': (7, 5)
                  }

#=========== few other test cases
FigureA = {'A': (1, 8),
          'B': (3, 8),
          'C': (3, 6),
          'D': (2, 5),
          'E': (1, 6)
          }

FigureB = {'A': (3, 4),
          'B': (5, 4),
          'C': (6, 3),
          'D': (5, 2),
          'E': (3, 2),
          'F': (2, 3)
          }

FigureC = {'A': (5, 9),
          'B': (7, 6),
          'C': (5, 6)
          }

FigureNone = {}

FigureSamePoint = {'A': (7, 6),
                  'B': (7, 6),
                  'C': (5, 6)
                  }

# Total number of lines from 5 points = 5C2 combinations = 5!/(3! * 2!) = 10
# while writing out the lines in 'input', noticed the sequence followed was:
# A looped over B,C,D,E = AB, AC, AD, AE
# then B looped over C, D, E = BC, BD, BE
# then C looped over D, E and so on
#
# that gave me all combinations

# strategy: created a list of just vertices from dictionary for better readability, although not strictly required
# looped twice one from A-E (complexity O(n)), starting with A with inside loop going from B-E (complexity O(n-1)
# overall complexity = quadratic = O(n*n)
# created dictionary inside the loop

def construct_all_permutations_of_lines(mydict):
   vertices = []
   outputdict = {}
   for k,v in mydict.items():
       vertices.append(k)

   #print(vertices)
   count = 0
   for i in vertices[count:]:
       for j in vertices[count + 1:]:
           str = i + j
           outputdict[str] = [mydict[i], mydict[j]]
       count += 1
   return outputdict

def find_matching_gradiets(all_coordinates):
   input_dict = construct_all_permutations_of_lines(all_coordinates)
   output = {}
   for k, v in input_dict.items():
       m = calculate_gradient(v[0], v[1])
       #print(str(m))
       if output.get(m) == None:
           output[m] = [k]
       else:
           output[m].append(k)
   return output

print(find_matching_gradiets(all_coordinates))
print("A = " + str(find_matching_gradiets(FigureA)))
print("B = " + str(find_matching_gradiets(FigureB)))
print("C = " + str(find_matching_gradiets(FigureC)))
print("None = " + str(find_matching_gradiets(FigureNone)))
print("SamePoint = " + str(find_matching_gradiets(FigureSamePoint)))


# {-0.5: ['BE', 'AD'], 0.0: ['AB', 'CD'], 0.25: ['CE'], 1.0: ['CB', 'ED'], -0.2: ['AE'], -2.0: ['BD', 'AC']}
# A = {0.0: ['AB', 'CE'], 1.0: ['BE', 'CD'], 3.0: ['BD'], 'undefined': ['AE', 'CB'], -3.0: ['AD'], -1.0: ['AC', 'ED']}
# B = {0.0: ['AB', 'CF', 'ED'], 1.0: ['BE', 'AF', 'CD'], 'undefined': ['BD', 'AE'], 0.33: ['CE', 'BF'], -0.33: ['AC', 'DF'], -1.0: ['AD', 'CB', 'EF']}
# C = {0.0: ['CB'], -1.5: ['AB'], 'undefined': ['AC']}
# None = {}
# SamePoint = {0.0: ['CB', 'AC'], 'samePoint': ['AB']}


