import csv

def add_to_csv(model, convertbot_count):
    with open('file.csv', 'a', newline='') as csvfile:
        fieldnames = ['Model', 'Convertbot_count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Model': model, 'Convertbot_count': convertbot_count})

# Call the function with the appropriate values
add_to_csv('model_value', 'convertbot_count_value')
