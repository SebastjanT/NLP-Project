# NLP-Project

This repository contains the project files for Project 1: Literacy situation models knowledge base creation.

## Table of contents

* [Report](#report)
* [Running the code](#running-the-code)
* [Data](#data)
  * [IMapBook](#imapbook-dataset)
  * [Gutenberg](#gutenberg-dataset)
* [Methods](#methods)
  * [Basic Text Analysis](#basic-text-analysis)
  * [NER](#named-entity-recognition)
  * [sentiment](#sentiment-analysis)


## Report

The report is available at in the root of the repository [Report (Literacy_situation_models_knowledge_base_creation)](./Literacy_situation_models_knowledge_base_creation.pdf).

## Running the code

To run the raw named entity recognition script clone this repository and excute the following commands:
```
cd ./NLP-PROJECT/ner
python ner.py
```

Replace the `python` command with `python3` if you are on Linux or MacOS.


To run the sentiment analysis code and the accompanying ner (to generate the correct output) all that needs to be done is set the correct variables to where the data is stored.

All the notebooks were ran in Google Colaboratory on a GPU instance, with the data in the folder `NLP-Project` and having the same substructure as the GitHub repository.

Variables in notebooks with paths to set:
* ner.ipynb - `common_words_filepath`, `base_datadir`,
* sentiment-roBERTa.ipynb - two `path` variables

## Data

The datasets and texts (short-stories) that we used for our project are available in the [./data](./data) directory.

### IMapBook dataset

This is the dataset containing the provided 7 short stories.

Two folders with the result of the NER and Sentiment analysis are now present in the dataset folder.

### Gutenberg dataset

Additional dataset of short stories.

Two folders with the result of the NER and Sentiment analysis are now present in the dataset folder.

## Methods

Here is a short summary of the methods used.

### Basic Text Analysis

We have perfomed basic text analysis on the IMapBook dataset of short-stories.
The analysis inculdes the # of tokens, # of tokens after removing stop words, plot of top 10 most frequent words and context analysis of the most frequent word.
The results are available in the [Jupyter-Notebook](./basic_text_analysis/imapbook_text_analysis.ipynb).

### Named entity recognition

Since our plan was to determine what characters appear in these stories, a good starting point was the NER (Named Entity Recognition) technique. With this approach, we were be able to determine all named entities in a given short story.

The code that produces a desired output for the sentiment analysis and it's results can be seen in the [Jupyter-Notebook](./sentiment/ner.ipynb).

### Sentiment Analysis

A proof of concept that sentiment analysis can provide valuable information if paired with NER for protagonist and antagonist detection.
The analysis inculdes a custom output of the NER algorithm (that includes the immediate sentences of the NE). And a Huggingface default pipline Sentiment analysis for ever character (most frequent 4) of every short story.
The results are available in the Jupyter-Notebook `./sentiment/sentiment.ipynb` in the branch `sentiment`.

In the `master` branch we expanded on the sentiment analysis approach. We used a different model to evaluate the sentiment of the 4 most frequent characters in the short stories.

We have also included analysis of 6 different levels of context.

The results are available in the [Jupyter-Notebook](./sentiment/sentiment-roBERTa.ipynb).