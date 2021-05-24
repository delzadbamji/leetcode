
select name, sum(amount) as balance
from Users u join Transactions t on u.account=t.account
group by u.name
having sum(amount)>10000