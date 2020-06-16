import csv


def show_menu():
    print('======== MENU UTAMA ========')
    print('[1] Show Data')
    print('[2] Insert Data')
    print('[3] Edit Data')
    print('[4] Delete Data')
    print('[5] Exit')
    print('======================')

    selected_menu = input('Pilih Menu : ')

    if (selected_menu == '1'):
        show_data()
    else:
        exit()


def back_to_menu():
    input('\n Tekan enter untuk kembali....')
    show_menu()


def show_data():
    data = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, ',')
        for row in csv_reader:
            data.append(row)

    if (len(data) > 0):
        labels = data.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        for daftar in data:
            print(f'{daftar[0]} \t {daftar[1]} \t {daftar[2]}')
    else:
        print('Kosong')
    back_to_menu()


if __name__ == "__main__":
    while True:
        show_menu()
