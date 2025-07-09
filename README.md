# RAGpipelineWikipediaQA

### Table of contents
* [Introduction](#star2-introduction)
* [Installation](#wrench-installation)
* [How to run](#zap-how-to-run) 
* [Contact](#raising_hand-questions)

## :star2: Introduction

* <p align="justify">Built a RAG system that answers user questions by retrieving and synthesizing information from Wikipedia.</p>
* <p align="justify">Implemented text tokenization, chunking, embedding (using all-mpnet-base-v2), and FAISS for efficient similarity search.</p>
* <p align="justify">Integrated a RoBERTa-base QA model to generate precise answers from retrieved contexts.</p>

![demo](/images/demo.PNG)

Figure: *Some questions and answers about the topic: `Van Thinh Phat fraud case`*

## :wrench: Installation

<p align="justify">Step-by-step instructions to get you running RAGpipelineWikipediaQA:</p>

### 1) Clone this repository to your local machine:

```bash
git clone https://github.com/hoangnguyen2003/RAGpipelineWikipediaQA.git
```

A folder called `RAGpipelineWikipediaQA` should appear.

### 2) Install the required packages:

Make sure that you have Anaconda installed. If not - follow this [miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install).

You can re-create our conda enviroment from `environment.yml` file:

```bash
cd RAGpipelineWikipediaQA
conda env create --file environment.yml
```

<p align="justify">Your conda should start downloading and extracting packages.</p>

### 3) Activate the environment:

Your environment should be called `RAGpipelineWikipediaQA`, and you can activate it now to run the scripts:

```bash
conda activate RAGpipelineWikipediaQA
```

## :zap: How to run 
<p align="justify">Simply run:</p>

```bash
python main.py
```

## :raising_hand: Questions
If you have any questions about the code, please contact Hoang Van Nguyen (hoangvnguyen2003@gmail.com) or open an issue.
