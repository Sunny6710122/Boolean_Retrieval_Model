# Boolean Retrieval Model in Information Retrieval 📖🔍
This repository contains the implementation of a **Boolean Retrieval Model** for Information Retrieval (IR). The project was developed as **Programming Assignment No. 1** for the Information Retrieval (CS4051) course in Spring 2024.

## Objective 🎯

The primary objective was to understand and implement indexing techniques for efficient query retrieval from a document collection. Specifically, this involved creating an **inverted index** and a **positional index** to support Boolean Model operations in IR.

## Key Features 🌟

- **Preprocessing Pipeline**: 🛠️ Implemented tokenization, case folding, stop-words removal, and stemming (using the Porter Stemmer) to extract meaningful features from the research papers dataset.
- **Index Creation**: 📂 Built inverted and positional indexes to facilitate efficient determination of document-term relationships and term proximities.
- **Query Processing**: 🔍 Developed a simplified Boolean IR model capable of handling three-term queries with Boolean operators (**AND, OR, NOT**) and supporting positional queries.
- **Assumptions**: Made basic assumptions of the Boolean Retrieval Model, such as term presence/absence in documents, equal evidential value of terms, and Boolean query operations.

## Implementation Details ⚙️

- **Command-Line Interface**: Provided for executing and evaluating queries.
- **Example Queries**: Supported the processing of 10 example queries as part of the assignment.

## Files 📂

- **Dataset**: `ResearchPapers.zip` containing 20 research papers.
- **Stop-Words List**: File for stop-words removal during preprocessing.

## Technologies Used 🛠️

- **Programming Language**: Python 🐍
- **Libraries**: `nltk`, `numpy`, and `customtkinter`

## How to Run Files? 🚀

1. **Prepare the Environment**:
   - Ensure the directory contains a folder named `ResearchPapers` with all corpus documents.
   - Include a file named `Stopword-List.txt` listing all stopwords.

2. **Install Dependencies**:
   - Run the following command to install necessary packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Install `customtkinter` for the GUI:
     ```bash
     pip install customtkinter
     ```

3. **Run the Application**:
   - Launch the GUI:
     ```bash
     python maincode.py
     ```
   - The GUI may take a few seconds to load. Use it to search for Boolean queries, including proximity queries.

## Future Improvements 🌱

- **Intuitive GUI**: Enhance the graphical user interface for better demonstration and interaction.
- **Additional Features**: Add support for more complex query operations and incorporate frequency counts in the indexing process.

---

Feel free to explore and test the Boolean Retrieval Model! 📖✨
