/*
183. 从不订购的客户
SQL架构
某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

Customers 表：

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders 表：

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
例如给定上述表格，你的查询应返回：

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
通过次数63,465提交次数95,282
*/

#左联结
SELECT Customers.Name as Customers
FROM Customers
left join Orders
ON Customers.id = Orders.CustomerId 
where Orders.id is null

#NOT IN
SELECT Name AS Customers 
FROM Customers 
WHERE Id NOT IN (
  SELECT CustomerId FROM Orders GROUP BY CustomerId
);