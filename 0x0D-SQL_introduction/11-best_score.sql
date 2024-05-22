-- list the score than is >= 10
-- score is listed descending order
SELECT score, name
  FROM second_table
  WHERE score >= 10
  ORDER BY score DESC;
