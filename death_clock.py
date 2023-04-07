import streamlit as st
import pickle
import numpy as np

def death_clock():
    st.title("Death Clock")
    st.subheader("How long do you have left to live?")

    st.write("This app will tell you how long you have left to live.")


    def make_prediction(sex, highest_qualification, rural, disability_status, is_water_filter, chew, smoke, alcohol, treatment_source): 
                 
        with open("model.pkl", "rb") as f:
            clf  = pickle.load(f)
            
            preds = clf.predict(np.array([[sex, highest_qualification, rural, disability_status, is_water_filter, chew, smoke, alcohol, treatment_source]]))
        return preds
    
    with st.form("my_form"):
        st.write("Entet your Details")
        age = st.number_input("Age", min_value=0, max_value=150, value=25, key="age")
        sex = st.radio("Sex", ('male', 'female'), key="sex")
        if sex == 'male':
            sex = 1
        else:
            sex = 2

        highest_qualification = st.number_input("Highest_qualification", min_value=0, max_value=150, value=3, key="hq")
        rural = st.radio("select your area", ('Rual', 'Urban'), key="rural")
        if rural == 'Rural':
            rural = 1
        else:
            rural = 2

        disability_sts = st.number_input("disability_sts", min_value=0, max_value=150, value=4, key="disability_sts")

        is_water_quality = st.radio("is water filtered ?", ('Yes', 'No'), key="water_quality" )
        if is_water_quality == 'Yes':
            is_water_quality = 1
        else:
            is_water_quality = 2

        chew = st.number_input("do you chew tobacco ? ", min_value=0, max_value=150, value=3, key="chew")
        smoke = st.number_input("do you smoke", min_value=0, max_value=150, value=25, key="smoke")

        alcohol = st.number_input("do you consume alcohol", min_value=0, max_value=150, value=2, key="alochol")
        treatment_src = st.number_input("what is the treatment source?", min_value=0, max_value=150, value=3, key="treatment_src")
        

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
    

    if submitted:
        st.write(age, sex,rural,disability_sts,is_water_quality,chew,smoke,alcohol)
        res = make_prediction(sex, highest_qualification, rural, disability_sts, is_water_quality, chew, smoke, alcohol, treatment_src)
        
        st.write("Predicted years", res[0])


    st.markdown("""
# death

# User Information
Please fill out the following information to the best of your knowledge:

## Age:  
Enter your age in years. For example, 25.

## Sex:  
Select your sex from the following options: Male, Female, Other.

## Highest Qualification: 
- Illiterate-0,
- Literate Without formal education-1,
- Literate With formal education-Below primary-2,
- Literate With formal education-Primary-3,
- Literate With formal education-Middle-4,
- Literate With formal education-Secondary/Matric (Class-X)-5,
- Literate With formal education-Hr. Secondary/Sr. Secondary/Pre-university(Class XII)-6,
- Literate With formal education - Graduate/ B.Tech/ B.B.A/ MBBS/ Equivalent-7,
- Literate With formal education-Post Grad/ M.Tech/ M.B.A/ MD/ Equivalent or higher-8, 
- Literate With formal education-Non-technical/ Technical diploma or certificate not equivalent to a degree-9 completed from the following options: No Formal Education, Primary School, Secondary School, Tertiary Education.

## Rural: Select whether you live in a rural area or not from the following options: Yes, No.
- Rural-1, Urban-2

## Disability Status: Select whether you have a disability or not from the following options: Yes, No.
- Mental-1,
- Visual-2,
- Hearing-3,
- Speech-4,
- Locomotor-5,
- Multiple-6,
- No Disability-0 
- (Others--7 :used in First & Second updation Survey only: details for Codes 0 to 6 remained same during the First & Second updation Survey ) 
  
## Is Water Filter Available?:  
Select whether a water filter is available at your place of residence or not from the following options: Yes, No.

## Chew:  
Select whether you chew tobacco or not from the following options: Yes, No.

## Smoke: 
Select whether you smoke or not from the following options: Yes, No.

## Alcohol: 
Select whether you drink alcohol or not from the following options: Yes, No.

# Treatment Source: 
## Select the source from which you would seek medical treatment from the following options
- Government Sub Center-01,
- Government PHC-02, 
- Government CHC-03,     
- Government  UHC/UHP/UFWC-04,     
- Government  Dispensary/Clinic-05,      
- Government Hospital-06,
- Government AYUSH Hospital/Clinic-07,
- Private Dispensary/Clinic-08,
- Private Hospital-09,
- Private AYUSH Hospital/Clinic-10,
- NGO or Trust Hosp/Clinic-11,
- At Home-12,
- Others-99,
- No Medical attention-00
""")




    
