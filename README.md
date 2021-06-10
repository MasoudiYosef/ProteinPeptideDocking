# ProteinPeptideDocking
Source codes for protein-peptide docking

After downloading the files, please follow these steps to run the codes:

  1- Extract the .zip file
  
  2- From the poses folder, copy the dataset into the main directory containing the algorithms codes and, then, extract it
  
  3- For runnning the algorithms, you need to one of the python programming language's versions such as "python 3.1" or higher versions
  
  4- Please check that the numpy module has been installed and exist for python. If not, you can install the module using the following command in CMD:
  
      pip install numpy
      
  5- Open the algorithm.py file, determine the input file and the algorithm, like the following figure
      
      ![Image 1]("https://github.com/MasoudiYosef/ProteinPeptideDocking/blob/main/MainFile.jpg")
      
  6- Press F5 to run the source code
  
  7- During the execution, the electrostaic, van der waals, solvation, and hydrogen bond energies are appeared in the python shell for every iteration of the algorithm's steps (please the following figure)
  
     <img src="https://github.com/MasoudiYosef/ProteinPeptideDocking/blob/main/Help.jpg">
  
  8- To determine the 3D predicted poses of the given peptide's atoms, go to the poses folder. A .txt file has been created for the chosen peptide. After opening it, go to the end of file and observe the latest predicted poses (please the following figure)
  
      <img src="https://github.com/MasoudiYosef/ProteinPeptideDocking/blob/main/Help1.jpg">
  
  9- To further parameter regulation, refer to the algorithms file (e.g., Trader.py) and change the noc and noi parameters, as shown in the following figure
  
      <img src="https://github.com/MasoudiYosef/ProteinPeptideDocking/blob/main/Help2.jpg">
      
Here is also a youtube link which describe how you can run the source codes:
 
  <a href="https://youtu.be/CPCUYPhJOe4"> Please click to redirect to the viodeo page </a>
