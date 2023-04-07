# Write your MySQL query statement below
SELECT Email FROM ( 
    select Email, count(Email) as num
    from Person
    group by Email
) as Statistic WHERE num > 1