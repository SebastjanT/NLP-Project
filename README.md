# NLP-Project

This repository contains the project files for Project 1: Literacy situation models knowledge base creation.

## Table of contents

* [Report](#report)
* [Data](#data)
  * [IMapBook](#imapbook-dataset)
  * [Gutenberg](#gutenberg-dataset)
* [Methods](#methods)
  * [Basic Text Analysis](#basic-text-analysis)
  * [NER](#named-entity-recognition)
  * [sentiment](#sentiment-analysis)


## Report

The report is available at in the root of the repository [Report (Literacy_situation_models_knowledge_base_creation)](./Literacy_situation_models_knowledge_base_creation.pdf).

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

### Sentiment Analysis

A proof of concept that sentiment analysis can provide valuable information if paired with NER for protagonist and antagonist detection.
The analysis inculdes a custom output of the NER algorithm (that includes the immediate sentences of the NE). And a Huggingface default pipline Sentiment analysis for ever character (most frequent 4) of every short story.
The results are available in the Jupyter-Notebook `./sentiment/sentiment.ipynb` in the branch `sentiment`.