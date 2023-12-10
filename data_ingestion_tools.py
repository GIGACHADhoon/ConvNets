import gzip
import idx2numpy

class data_ingestion_tools:
    # Function to read images and labels from IDX files
    def read_idx_file(self,file_path):
        with gzip.open(file_path, 'rb') as f:
            data = idx2numpy.convert_from_file(f)
        return data