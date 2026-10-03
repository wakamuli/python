student_data={"id1":{"name":"x", "class":"8", "subject_integration": "chem,maths,physics" },
              "id2":{"name":"z", "class":"8", "subject_integration": "chem,maths,physics"},
              "id3":{"name":"a", "class":"8", "subject_integration": "chem,maths,physics"},
              "id4":{"name":"x", "class":"8", "subject_integration": "chem,maths,physics"}}


result={}
seen=[]

for student_id , details in student_data.items():
    unique_key=(details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen:
        seen.append(unique_key)
        result[student_id]=details

for k, v in result.items():
    print(k,  ":",    v)

