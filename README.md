
# Chicken Disease Classification Project

Chicken coccidiosis is a common intestinal disease caused by protozoan parasites from the genus Eimeria. Seven species of this genus can affect chickens, each with different pathogenic characteristics and targeting a specific intestinal location. The parasites rapidly multiply, damaging the intestinal lining, preventing chickens from absorbing nutrients from their food. Vaccination, preventative medication, and good flock management practices can help control the disease. 

**The disease is a major menace to the global poultry industry and hampers chicken's productivity and welfare.**

The aim of this machine learning project is to identify the disease of the chicken based on the fecal image of the chicken. The model can determine whether the chicken is infected with Coccidiosis or not, by just analysing the image of the fecal matter of the chicken.




## ⚒️ Workflow

The workflow defines the way the components and pipeline is constructed in the project. The basic workflow followed in this project is as follows:

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Develop app.py



## ⚙️ Tech Stack

**Programming Language:** Python

**Packages used:** Pytorch, FastAPI, Transformers, Pandas, Numpy, Matplotlib, Seaborn, Streamlit, Scipy.



## 💻 How to run?

#### STEPS:

Clone the repository
```python
htts://github.com/krishanwalia30/Text-Summarizer
```

**STEP 01- Create a conda environment after opening teh repository**

```
conda create -n summary python=3.8 -y
```
```python
conda activate summary
```

**STEP 02- Install the requirements.txt**

```python
pip install -r requirements.txt
```
```py
# Finally run the following command
python app.py
```
Now,

```python
Open: http://localhost:8000
```


## 📚  Lessons Learned

* Learned to create an end-to-end machine learning pipeline.
* Created different modules and components for different stages in pipeline development.
* Learned about Transformers
* Learned about Hugging Face API.
* Integrated Hugging Face API within the project for accessing the dataset.
* Learned to use FastAPI.


## 🧮 Features

- Developed APIs
- Model can be trained from the webapp interface as well.
- Prediction API is also made on the webapp.