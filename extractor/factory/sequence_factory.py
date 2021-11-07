from model import Node
from services import ReadAction, StoreAction, LoopAction, ClickAction

click = ClickAction()
read = ReadAction()
store = StoreAction()
loop = LoopAction()


years = Node("#conteudo_ddlAnos option", 'years', loop)

departments = Node("#conteudo_ddlDelegacias option",
                      'department', loop)

occurrences = Node("#conteudo_btnMensal", 'occurrences', click)

cities = Node("#conteudo_ddlMunicipios option:nth-child(566)",
                 'cities', click)


table = Node(
    "#conteudo_repAnos_gridDados_0 tr td:nth-child(n+1) ", 'table', read)

year_save = Node("#conteudo_ddlAnos", 'table', store)

dp = Node("#conteudo_ddlDelegacias ", 'dp', store)


dp.child = table
year_save.child = dp
departments.child = year_save
years.child = departments
cities.child = years
occurrences.child = cities
elements = occurrences
