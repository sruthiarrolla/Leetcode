# Write your MySQL query statement below
SELECT E.name as Employee
FROM Employee E 
JOIN Employee as m ON E.managerId=m.id
WHERE E.salary>m.salary;
