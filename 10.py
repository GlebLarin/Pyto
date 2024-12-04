import numpy as np
def process_matrices(input_filename, output_filename):
    """
    Reads matrices from an input file, processes them, and writes the results to an output file.
    """
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        matrices = []
        current_matrix = []
        for line in lines:
            line = line.strip()  
            if line == '':  
                if current_matrix:
                    matrices.append(np.array(current_matrix, dtype=float))
                    current_matrix = []
            else:
                row = [float(x) for x in line.split()] 
                current_matrix.append(row)

        if current_matrix:
          matrices.append(np.array(current_matrix, dtype=float))
        results = []
        if len(matrices) >=2:
          for i in range(0, len(matrices), 2):
              if i + 1 < len(matrices):
                  try:
                      result = matrices[i] + matrices[i+1] Change as needed.
                      results.append(result)
                  except ValueError: 
                      print(f"Error: Matrices {i+1} and {i+2} have incompatible shapes for addition.")
                      return  
        with open(output_filename, 'w') as outfile:
            for matrix in results:
                for row in matrix:
                  outfile.write(' '.join(map(str, row)) + '\n')
                outfile.write('\n') 
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except ValueError as e:
        print(f"Error during processing: {e}")
input_filename = "YourFullName_YourGroup_vvod.txt"
output_filename = "YourFullName_YourGroup_vivod.txt"
process_matrices(input_filename, output_filename)