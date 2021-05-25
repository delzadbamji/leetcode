select employee_id,
case when (employee_id%2=1 and name not like 'M%') then salary
 else 0 end as bonus
from Employees
order by employee_id;

# Runtime: 561 ms, faster than 100.00% of MySQL online submissions for Calculate Special Bonus.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Calculate Special Bonus.
