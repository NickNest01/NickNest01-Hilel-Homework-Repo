import csv

# First task - comparing files for duplicates
def deduplicator():
    with (open('./ideas_for_test/work_with_csv/random.csv', 'r') as f1,
        open('./ideas_for_test/work_with_csv/random-michaels.csv', 'r') as f2):
        csv_reader1 = csv.reader(f1)
        csv_reader2 = csv.reader(f2)

        rows1 = list(csv_reader1)
        rows2 = list(csv_reader2)

    all_rows = rows1 + rows2
    unique_rows = set(tuple(row) for row in all_rows)

    unique_rows_list = list(unique_rows)

    assert len(unique_rows) == len(set(unique_rows))

    with open('result_nesterenko.csv', 'w', newline='') as result_file:
        csv_writer = csv.writer(result_file)
        csv_writer.writerows(unique_rows_list)

    print("The 'result_nesterenko.csv' file with distinct values from both documents is created")

deduplicator()
