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
+-----------------+                +------------------------+
|  Test Program   |                | Product Description    |
|                 |                | Microservice           |
+-----------------+                +------------------------+
         |                                   |
         | 1. Write request to               |
         |    description-service.txt        |
         |---------------------------------->|
         |                                   |
         | 2. Check for new requests         |
         |<----------------------------------|
         |                                   |
         | 3. Read request                   |
         |---------------------------------->|
         |                                   |
         | 4. Process request and find       |
         |    product description            |
         |---------------------------------->|
         |                                   |
         | 5. Write response to              |
         |    description-response.txt       |
         |<----------------------------------|
         |                                   |
         | 6. Read response from             |
         |    description-response.txt       |
         |---------------------------------->|
         |                                   |
         | 7. Display response               |
         |<----------------------------------|
         |                                   |
