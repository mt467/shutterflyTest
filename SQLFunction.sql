SELECT customer_id, customerTotalValueAllWeeks(customer_id) from customer;


-- --------------------------------------------------------------------------------
-- Routine DDL
-- Mahdieh Taher-Shutterfly Take Home Excerise
-- Note: comments before and after the routine body will not be stored by the server
-- --------------------------------------------------------------------------------
DELIMITER $$

CREATE DEFINER=`root`@`localhost` FUNCTION `customerTotalValueAllWeeks`(customerId VARCHAR(50)) RETURNS float
    DETERMINISTIC
BEGIN

DECLARE totalValue FLOAT;
DECLARE totalWeeks INT;
DECLARE totalOrderAmount FLOAT;
DECLARE totalVisits INT;
DECLARE avgTotalValue FLOAT;
DECLARE maxEventDate DATETIME;
DECLARE minEventDate DATETIME;
DECLARE dummyDate DATETIME;
DECLARE isFirstTimeUsingDummyDate BOOLEAN;

SET isFirstTimeUsingDummyDate=true;
SET totalValue=0;
SET totalWeeks=0;
SET avgTotalValue=0;
SET totalOrderAmount=0;
SET totalVisits=0;

SET maxEventDate = ( SELECT MAX(DATE_FORMAT(STR_TO_DATE(event_time,'%Y-%m-%dT%H:%i:%s.%fZ'),'%Y-%m-%d %H:%i:%s'))
FROM
    site_visit 
WHERE customer_id=customerId);

IF maxEventDate IS NOT NULL THEN

SET minEventDate = ( SELECT MIN(DATE_FORMAT(STR_TO_DATE(event_time,'%Y-%m-%dT%H:%i:%s.%fZ'),'%Y-%m-%d %H:%i:%s'))
FROM
    site_visit 
WHERE customer_id=customerId);

/* if minEventDate is not empty ofcourse!*/
SET dummyDate = minEventDate;

WHILE (dummyDate<=maxEventDate) DO

SET totalOrderAmount = (SELECT (ordert.total_amount) 
FROM order_t ordert
WHERE ordert.customer_id=customerId
AND YEARWEEK(DATE_FORMAT(STR_TO_DATE(event_time,'%Y-%m-%dT%H:%i:%s.%fZ'),'%Y-%m-%d %H:%i:%s')) = YEARWEEK(dummyDate));

SET totalVisits= (SELECT COUNT(page_id)
FROM site_visit
WHERE customer_id=customerId
AND YEARWEEK(DATE_FORMAT(STR_TO_DATE(event_time,'%Y-%m-%dT%H:%i:%s.%fZ'),'%Y-%m-%d %H:%i:%s')) = YEARWEEK(dummyDate));

/* totalvalue of this particular week */
SET totalValue=totalValue + (totalOrderAmount*totalVisits);

/* check if dummydate being used for the first time to calculate how many days should be added*/
IF (isFirstTimeUsingDummyDate) THEN
SET dummyDate=DATE_ADD(dummyDate,INTERVAL 7-(DAYOFWEEK(dummyDate)) DAY);
SET isFirstTimeUsingDummyDate=false;
ELSE
SET dummyDate=DATE_ADD(dummyDate,INTERVAL 7 DAY);
END IF;

SET totalWeeks=totalWeeks+1;

END WHILE;

SET avgTotalValue=ROUND((totalValue/totalWeeks),2);

END IF;

RETURN avgTotalValue;

END