# Product Description Microservice

## Overview
The Product Description Microservice reads product IDs or names from an input file (`description-service.txt`), fetches the corresponding description from a CSV file (`products.csv`), and writes the result to an output file (`description-response.txt`).

## Communication Contract

### Request Data
To request data from the product description microservice, write the product ID or name to `description-service.txt`.

        with open('description-service.txt', 'w') as request_file:
            request_file.write(product_request)

### Receive Data
To receive data, read the product description from `description-response.txt`. The file will contain the product description or an error message.

        with open('description-response.txt', 'r') as response_file:
            response = response_file.read()

## UML Sequence Diagram

![Screenshot_21-5-2024_23012_online visual-paradigm com](https://github.com/ancisoj/microserviceA/assets/138057884/20cb7ab5-b81a-4323-80ad-4dd722683d60)
