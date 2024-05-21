import time


def main():
    while True:
        # Prompt the user to enter a product ID or name
        product_request = input("Enter the product ID or name (or press Enter to exit): ")

        # Exit the loop if the input is empty
        if not product_request:
            print("Exiting the program.")
            break

        # Write the request to the input file
        with open('description-service.txt', 'w') as request_file:
            request_file.write(product_request)

        # Wait for the microservice to process the request
        time.sleep(2)

        # Read the response from the output file
        with open('description-response.txt', 'r') as response_file:
            response = response_file.read()

        print(f'Response from microservice: {response}')


if __name__ == "__main__":
    main()
