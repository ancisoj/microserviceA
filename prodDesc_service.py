import csv
import time

while True:
    # Open and read the input file
    with open('description-service.txt', 'r') as product_file:
        prod_desc_request = product_file.read().strip()

    # Determine if the file has a request for product description
    if prod_desc_request:
        message = "Product not found."

        # Using a CSV file for products where description is in the third column
        with open('products.csv', newline='') as csvfile:
            products_csv = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in products_csv:

                product_id = row[0]
                product_name = row[1]
                product_description = row[2]

                # Check if the request matches product_id or product_name
                if product_id == prod_desc_request or product_name == prod_desc_request:
                    message = f"You've selected this product: {product_description}"
                    break

        # Write description back to output file
        with open('description-response.txt', 'w') as output_file:
            output_file.write(message)

    # Sleep for a short time before checking the input file again
    time.sleep(1)
