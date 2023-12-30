import pickle
import joblib
from attr import dataclass
import os


@dataclass
class SyllabusCourse:
    course: dict = {}


a = SyllabusCourse()
a.course = {}


class SaveModel:
    def save(self, obj: SyllabusCourse):
        file = r"C:\Users\princ\OneDrive\Desktop\internship\DataStorage\dictionary.class"
        try:
            my_dictionary = self.return_class(file)
            os.remove(file)
        except Exception as e:
            my_dictionary = SyllabusCourse()
        with open(file, "b+w") as a:
            obj.course.update(my_dictionary.course)
            pickle.dump(obj, a)

    def return_class(self, filename: str = r"C:\Users\princ\OneDrive\Desktop\internship\DataStorage\dictionary.class"):
        try:
            with open(filename, "rb") as a:
                obj = pickle.load(a)
            return obj
        except Exception as e:
            return SyllabusCourse()


