-- To find the number of types of tigers in the taxonomy table of the dataset and the "ncbi_id" of the Sumatran Tiger:

SELECT COUNT(DISTINCT species) AS num_tigers, ncbi_id
FROM taxonomy
WHERE genus = 'Panthera'
  AND species IN ('tigris', 'altaica', 'sumatrae', 'amoyensis', 'jacksoni')
GROUP BY ncbi_id
HAVING species = 'sumatrae';
