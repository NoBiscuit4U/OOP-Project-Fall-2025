import csv
import io

class _CSVFunctions:
    """
    Private class for basic functions used by the functions in CSVData
    """
    def __init__(self,columns,rows):
        self.columns=columns
        self.rows=rows

    def columnValues(self,targetColumn=""):
        output=[]
        i=0

        for column in self.columns:
            if(targetColumn==column):
                for row in self.rows:
                    if(row!=self.rows[0]):
                        if(row):
                            output.append((row[i]))
            else:
                i+=1
        
        return output
    
class CSVData:
    """
    Class for manipulating and pulling information from csv files.

    Params
    -------------------------------------------------------------------------------
    csvFile: Requires the directory of a csvFile to be passed in.

    -------------------------------------------------------------------------------
    """
    def __init__(self,csv_data,encoding=""):
        self.csvFile=csv_data
        self.encoding=encoding
        
        if csv_data!=None:
            if encoding=="":
                with io.BytesIO.read(csv) as f:
                    reader=list(csv.reader(f))
                    rows=reader.copy()
            else:
                with io.BytesIO.read(csv_data,flags=0) as f:
                    reader=list(csv.reader(f))
                    rows=reader.copy()

            self.rows=rows
            self.rowCount=len(rows)

            if len(rows)!=0:
                self.columns=rows[0]
                self.columnCount=len(rows[0])
                self.csvFuncs=_CSVFunctions(self.columns,self.rows)

    def getColumnValues(self,targetColumn=""):
        """
        Returns the columns values.

        Params
        -------------------------------------------------------------------------------
        targetColumn: Requires the name of the column with the desired values to be passed in.

        -------------------------------------------------------------------------------
        """
        return self.csvFuncs.columnValues(targetColumn)
    
    def getColumnIndex(self,targetColumn=""):
        """
        Returns array index of the target column

        Params
        -------------------------------------------------------------------------------
        targetColumn: Desired column index

        -------------------------------------------------------------------------------
        """
        for i in range(len(self.columns)):
            if(targetColumn==self.columns[i]):
                return i
        
        return 999
    
    def deleteRows(self,targetRows=[0]):
        """
        Returns a new set of data with only the desired rows.

        Params
        -------------------------------------------------------------------------------
        targetRows: List of rows to remove, uses the index of the row.

        -------------------------------------------------------------------------------
        Also when removing rows a row index of 0 is always the column names.
        """
        outputList=[]

        for row in range(self.rowCount):
            if(any(row==r for r in targetRows)==False):
                outputList.append(self.rows[row])

        return outputList