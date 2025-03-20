--1. Select employee details  of dept number 10 or 30

--8. Write a query to fetch ALL the  employee details along with 
--department name, department location, irrespective of employee existance in the department.
select * from emp_table E, dept_table D where E.DeptNo = D.DeptNo;

--9. Write an update statement to increase the employee salary by 10 %
update emp_table set Sal = Sal+(Sal*10/100);
select Ename,Sal from emp_table;

--10. Write a statement to delete employees belong to Chennai location.
delete from emp_table where DeptNo in(select DeptNo from dept_table where Loc = 'Chennai');


--11. Get Employee Name and gross salary (sal + comission) 
SELECT Ename AS EmployeeName, Sal + ISNULL(Commission, 0) AS GrossSalary
FROM emp_table;

--12. Increase the data length of the column Ename of Emp table from  100 to 250 using ALTER statement
alter table emp_table modify Ename varchar(250);

--13. Write query to get current datetime
select current_timestamp();

--14. Write a statement to create STUDENT table, with related 5 columns
create table student(student_id int primary key,
first_name varchar(20) not null,
last_name varchar(20),
dob date,
gender char(1),
branch varchar(20)
);

--15.  Write a query to fetch number of employees in who is getting salary more than 10000
SELECT COUNT(*) AS NumOfEmployees
FROM emp_table
WHERE Sal > 10000;


--16. Write a query to fetch minimum salary, maximum salary and average salary from emp table.
SELECT MIN(Sal) AS MinSalary, MAX(Sal) AS MaxSalary, AVG(Sal) AS AvgSalary
FROM emp_table;

--17. Write a query to fetch number of employees in each location
SELECT Loc, COUNT(*) AS NumOfEmployees
FROM dept_table D
JOIN emp_table E ON D.DeptNo = E.DeptNo
GROUP BY Loc;


--18. Write a query to display emplyee names in descending order
select Ename from emp_table order by Ename desc;

--19. Write a statement to create a new table(EMP_BKP) from the existing EMP table 
create table emp_bkp as select * from emp_table;

--20. Write a query to fetch first 3 characters from employee name appended with salary.
select concat(substring(Ename,1,3),Sal) from emp_table;

--21. Get the details of the employees whose name starts with S
select * from emp_table where Ename like 'S%';

--22. Get the details of the employees who works in Bangalore location
select e.* from emp_table e join dept_table d on e.DeptNo = d.DeptNo
where d.Loc="Bangalore";

--23.  Write the query to get the employee details whose name started within  any letter between  A and K
select * from emp_table where Ename like '[A-K]%';

--24. Write a query in SQL to display the employees whose manager name is Stefen 
select e1.* from emp_table e1
join emp_table e2 on e1.mgr=e2.EmpNo where e2.Ename="Stefen";

--25. Write a query in SQL to list the name of the managers who is having maximum number of employees working under him
select mgr
from(
    select mgr, count(*) as ecount
    from emp_table
    group by mgr
    order by ecount desc
    limit 1
) as MaxEmployees
join emp_table e on MaxEmployees.mgr = e.EmpNo;

--27. Write a query to list all details of all the managers
select * from emp_table where EmpNo in(select distinct mgr from 
emp_table27 where mgr is not null);
