

import difflib

string_list = ['ape', 'apple', 'peach', 'puppy']
user_input = str(input("Enter a new string: "))
lst = []
def find_similar_strings():
    
    for i in string_list:
        print(i, user_input)
        matches = difflib.SequenceMatcher(a=i , b=user_input).ratio()
        print(matches)
        lst.append(matches)
    
    print(lst)
    print('The first one:',lst[-1]) 
    print('The second one:',lst[-2]) 
    print('The third one:',lst[-3])  
find_similar_strings()



from ultralytics import YOLO

model = YOLO("C:\\Users\\garshasp\Documents\\yolov8m.pt")

print("start")

model.train(data="C:\\Users\\garshasp\\Desktop\\data.yaml", epochs=30)


print("finished")