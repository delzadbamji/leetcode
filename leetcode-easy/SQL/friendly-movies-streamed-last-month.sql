select distinct c.title
from TVProgram as tv join Content as c on c.content_id=tv.content_id
where Kids_content="Y" and content_type="Movies" and program_date between "2020-06-01" and "2020-06-30" 
