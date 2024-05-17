import tarfile

# Specify the path to the tar.gz file
tar_file = 'P:\\code\\sentiment_analysis_movie_calssifier\\aclImdb_v1.tar.gz'

# Open the tar.gz file for reading
with tarfile.open(tar_file, 'r:gz') as tar:
    # Extract all files from the archive
    tar.extractall()
    print('Files extracted successfully.')