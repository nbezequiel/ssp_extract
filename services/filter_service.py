from model import Occurrence
from utils.constants import DEPARTMENTS_QUANTITY, YEAR, DEPARTMENT

class Filter:

    def __init__(self):
        self._years = []
        self._departments = []
        self._last_year = None
        self._is_number = lambda x: x.text.isnumeric() 
        super().__init__()

    ## remove 
    def is_finished(self):
        number = Occurrence.objects.distinct(DEPARTMENT)
        if number == DEPARTMENTS_QUANTITY:
            return True
        return False

    def _iterate_year(self, elements, latest):
        return list(filter(lambda it: int(it.text) < int(latest), elements))
    
    def _get_latest(self):
        return Occurrence.objects.order_by('-id').first()

    def _get_all_elements(self, elements):
        return list(map(lambda f: f.text, elements))
    
    def _count_departments_by_year(self, year):
        return Occurrence.objects(year = year).distinct(DEPARTMENT);

    def _filter_departments(self, elements, department):
        filtered_list = list(filter(lambda it: it.text == department, elements))
        index = elements.index(filtered_list[0]) + 1
        if index != 119:
            return elements[index:]
        else:
            return elements[0:]

    def _filter_years(self, elements, year):
        return list(filter(lambda it: int(it.text) <= int(year), elements))
    
    def _as_text_list(self, filtered):
        return list(map(lambda f: f.text, filtered))
    
    def _filter_by_type(self, elements, latest, node, count_departments):
        if  count_departments == 119 and node.desc == YEAR:
            return self._iterate_year(elements, latest.year)
        elif node.desc == YEAR:
                return self._filter_years(elements, latest.year)
        elif node.desc == DEPARTMENT:
                return self._filter_departments(elements, latest.department_name)
        else:
            raise Exception()

    def filter(self, elements, node):    
        latest = self._get_latest()
        filtered = []
        
        if latest == None:
            return self._get_all_elements(elements)

        count_depart = len(self._count_departments_by_year(latest.year))
        
        filtered = self._filter_by_type(elements, latest, node, count_depart)
        
        return self._as_text_list(filtered)