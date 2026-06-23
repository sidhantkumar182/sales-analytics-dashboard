-- Total Sales
SELECT SUM(Sales) AS TotalSales
FROM sales_data;

-- Sales By Region
SELECT Region, SUM(Sales) AS Revenue
FROM sales_data
GROUP BY Region;

-- Top Product
SELECT Product, SUM(Sales) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC;

-- Average Profit
SELECT AVG(Profit) AS AvgProfit
FROM sales_data;
