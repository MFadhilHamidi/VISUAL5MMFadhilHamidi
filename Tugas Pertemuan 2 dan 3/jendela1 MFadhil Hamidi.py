import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#ffffff")
window= sg.Window(title="Profile",layout=[
    [sg.Text("SELAMAT DATANG DI KELAS", font=("Arial",25,"italic","bold","underline"))],
    [sg.Text("NPM : 2210010243")],
                                                  [sg.Text("Nama : Muhammad Fadhil Hamidi")],
                                                  [sg.Text("Kelas : 5M Reguler Banjarmasin")],
                                                  [sg.Text("Matkul : Pemrograman Visual 3")]],size=(510,200), font=("Times", 18))
window()
window.close()