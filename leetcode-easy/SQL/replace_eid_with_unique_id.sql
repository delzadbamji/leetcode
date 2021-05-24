select unique_id,name
from Employees as e left join EmployeeUNI as eu on eu.id=e.id
where eu.unique_id is NULL or eu.unique_id is not null