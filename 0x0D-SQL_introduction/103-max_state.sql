-- gets states with the highest temperature
SELECT state, MAX(`value`) FROM temperatures GROUP BY state ORDER BY state;
