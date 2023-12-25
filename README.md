
# Text Summarizer Project

Text Summarizer takes a large document/paragraph and then uses an NLP model to generate a short paragraph.

This is a complete end-to-end Natural Language Processing machine learning project. APIs are developed for text summarization and training the model.

## 📷 Demo
![Screenshot 2023-12-25 184236](https://github.com/krishanwalia30/Text-Summarizer/assets/101003187/b1b3a403-bef0-493b-9eca-018358e78666)

## 🎆 Screen Recording
https://github.com/krishanwalia30/Text-Summarizer/assets/101003187/0d59bded-c444-48dc-bd0b-1e27673f0626



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
