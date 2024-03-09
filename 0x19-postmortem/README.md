# Car Inventory Management System Outage Post-Mortem 🚗💥

### Oops! We Lost Some Cars! 🙈

## Issue Summary:
- **Duration:** The outage occurred from 10:00 AM to 12:00 PM (UTC) on January 15th, 2024.
- **Impact:** The service outage affected the "Car Inventory Management System," causing users to experience slow response times and errors when querying car makes. Approximately 30% of users were affected by the issue.
- **Root Cause:** The root cause of the outage was traced back to a bug in the query logic, where related cars were not included in the response when querying car makes.

## Timeline:
- **10:00 AM (UTC):** The issue was detected when users reported slow response times and errors when accessing the "Car Inventory Management System."
- **10:15 AM:** Engineers noticed an increase in error logs related to missing car models in the query responses.
- **10:30 AM:** Investigations began into the query logic and database queries to identify the root cause of the issue.
- **11:00 AM:** Initial assumptions suggested a problem with the database schema or query optimization.
- **11:30 AM:** Further debugging revealed that the issue was with the query logic not including related cars for the queried makes.
- **11:45 AM:** The incident was escalated to the development team responsible for the query logic.
- **12:00 PM:** The issue was resolved by fixing the query logic to include related cars in the response for queried makes.

## Root Cause and Resolution:
- **Root Cause:** The root cause of the issue was a logic error in the query code, where related cars were not being fetched and included in the response for queried car makes.
- **Resolution:** The issue was fixed by updating the query logic to properly fetch and include related cars for the queried makes. Unit tests were also added to ensure similar issues are caught in the future.

## Corrective and Preventative Measures:
- **Improvements/Fixes:** 
  - Improve code review processes to catch logic errors before deployment.
  - Enhance testing procedures to cover edge cases and ensure comprehensive test coverage.
- **Tasks to Address the Issue:**
  - Patch the query logic to fix the bug and ensure related cars are included in the response.
  - Implement stricter code review processes to catch similar logic errors in the future.
  - Enhance monitoring and alerting systems to quickly detect and respond to similar issues.

