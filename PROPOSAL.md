## Proposal for Travel-Itinerary

This proposal addresses several issues in the Travel-Itinerary repository to improve its security, maintainability, and deployment.

**C1: Add Dockerfile**
A Dockerfile will be added to containerize the application, making it easier to deploy and run in different environments. This ensures consistency and simplifies the deployment process.

**C2: Create .env.example**
A `.env.example` file will be created to provide a template for environment variables. This will help users configure the application correctly and avoid hardcoding sensitive information.

**C3: Remove Hardcoded Secrets**
The hardcoded secrets in `app.py` will be removed and replaced with environment variables. This will improve the security of the application by preventing sensitive information from being exposed in the code.
