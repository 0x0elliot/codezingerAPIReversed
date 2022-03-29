from requests import Session
from . import URL

class Classes:
    URL = URL
    def __init__(self, session: Session):
        # Leaving space in the future
        # To let myself fetch classes
        self.session = session
    
    def fetchLabsInClass(self, class_id: str):
        data = dict(
            searchData=dict(
                problemId=""
            ),
            deviceSpecificProblemConfiguration=dict(
                os="Windows",
                browser="Chrome",
                userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v2011273942716413555 t3369586550842097326 ath1fb31b7a altpriv cvcv=2 smf=0",
            )
        )

        r = self.session.put(
            self.URL + "student/assignments/" + class_id,
            data=data
        )
        labs = r.json()[0]
        return labs
    
    def labFolderGenerator(self, class_id: str):
        # Generator to return details of each 
        # Lab folder

        labs = self.fetchLabsInClass(
            class_id
        )
        for i in labs.get("chapterList"):
            yield i
    
    def labAssignmentGenerator(self, class_id):
        # Generator to return details of each 
        # Lab in the folder

        folders = self.labFolderGenerator(class_id)
        while True:
            try:
                assignment = folders.get("chapterList")
                yield assignment
            except StopIteration:
                break
    
    
    

        

            

        


    
