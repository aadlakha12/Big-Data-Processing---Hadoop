# Hadoop

#### Part 1: Word Count 
A MapReduce algorithm to produce count of every word in the gutenberg document.

#### Part 2: NGrams

A MapReduce algorithm to produce modified tri-grams around the key words, after replacing the key word with ‘$’ using the gutenberg dataset.

Example:
cat was sitting on a roof ---> if the key word was ‘sitting’ ---> the modified tri-grams would be
cat_was_$, was_$_on,$_on_a,
The key words to look for in the gutenberg dataset are ‘science’, ‘sea’ , ‘fire’.

The algorithm after producing these modified tri-grams, return the 10 most occurred modified tri-gram in the dataset.

#### Part 3: Inverted Index

A MapReduce algorithm to produce inverted index for the gutenberg dataset.

An inverted index (also referred to as a postings file or inverted file) is a database index storing a mapping from content, such as words or numbers, to its locations in a set of documents in the Gutenberg folder.

#### Part 4: Relational Join

Using the Dataset in the assignment folder, implemented a MapReduce algorithm to join two datasets using a primary key.

#### Part 5: K-NN Algorithm

Using the train and test set provided in the assignment, implemented KNN
algorithm using MapReduce.

KNN algorithm is a supervised machine learning algorithm that be used to address both classification and regression problems. It assumes that similar things are near to each other. It works based on the concept of similarity and assigns the label based on highest vote for the chosen ‘k’ neighbors.
