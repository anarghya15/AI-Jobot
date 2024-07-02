# Dataset path
dataset_path = './data/25_cleaned_job_descriptions_shorter.csv'

# Parameters
vocab_size = 1000
max_length = 1000
batch_size = 50
nb_epoch = 50

# Model Parameters
dense = 512
dropout = 0.1
labels = 30
activation_function = 'relu'
last_activation_function = 'softmax'

# Complile Parameters
optimizer = 'adam'  # or 'sgd'
loss = 'categorical_crossentropy'

# Model fit
validation_split = 0.1
verbose = 1
