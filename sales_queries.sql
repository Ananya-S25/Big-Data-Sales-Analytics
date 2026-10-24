
-- 1. Total revenue
SELECT ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales;

-- 2. Monthly revenue
SELECT YearMonth,
       ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM sales
GROUP BY YearMonth
ORDER BY YearMonth;

-- 3. Top 10 products
SELECT Description,
       ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales
GROUP BY Description
ORDER BY total_revenue DESC
LIMIT 10;

-- 4. Top 10 countries
SELECT Country,
       ROUND(SUM(Revenue), 2) AS total_revenue
FROM sales
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;

-- 5. Top customers
SELECT CustomerID,
       ROUND(SUM(Revenue), 2) AS total_spend,
       COUNT(DISTINCT InvoiceNo) AS total_orders
FROM sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY total_spend DESC
LIMIT 10;
