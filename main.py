from tkinter import *

import tkintermapview

root = Tk()
root.geometry('1200x760')
root.title ("map book MK")



ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektow = Frame(root)
ramka_mapa = Frame(root)
ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)   #colorspam= rozciagnięcie
ramka_mapa.grid(row=2, column=0,columnspan=2)


# ramka_lista_obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text="lista użytkowników")
label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektów = Listbox(ramka_lista_obiektow, width=50, height=10)
listbox_lista_obiektów.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu = Button(ramka_lista_obiektow,text="Pokaż szczegóły")
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow,text="Usuń użytkownika")
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow,text="Edytuj użytkownika")
button_edytuj_obiekt.grid(row=2, column=2)

#ramka_formularz
label_formularz = Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name = Label(ramka_formularz, text="Imie")
label_name.grid(row=1, column=0,sticky=W)
label_surname = Label(ramka_formularz, text="Nawisko")
label_surname.grid(row=2, column=0,sticky=W)
label_locaction = Label(ramka_formularz, text="Miejscowość ")
label_locaction.grid(row=3, column=0,sticky=W)
label_post = Label(ramka_formularz, text="Ilość postów ")
label_post.grid(row=4, column=0)

entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_surname = Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_locaction = Entry(ramka_formularz)
entry_locaction.grid(row=3, column=1)
entry_post = Entry(ramka_formularz)
entry_post.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text="Dodaj użytkownika")
button_dodaj_obiekt.grid(row=5, column=0 , columnspan=2)

#ramka_szczegoly_obiektu
label_szczegoly_obiektow = Label(ramka_szczegoly_obiektow, text="Szczegóły obiektu")
label_szczegoly_obiektow.grid(row=0, column=0)
label_szczegoly_name = Label(ramka_szczegoly_obiektow, text="Imie" )
label_szczegoly_name.grid(row=1, column=0)
label_szczegoly_name_wartosc = Label(ramka_szczegoly_obiektow, text="...." )
label_szczegoly_name_wartosc.grid(row=1, column=1)
label_szczegoly_surname = Label(ramka_szczegoly_obiektow, text="Nazwisko" )
label_szczegoly_surname.grid(row=1, column=2)
label_szczegoly_surname_wartosc = Label(ramka_szczegoly_obiektow, text="...." )
label_szczegoly_surname_wartosc.grid(row=1, column=3)
label_szczegoly_location = Label(ramka_szczegoly_obiektow, text="Miejscowość" )
label_szczegoly_location.grid(row=1, column=4)
label_szczegoly_location_wartosc = Label(ramka_szczegoly_obiektow, text="...." )
label_szczegoly_location_wartosc.grid(row=1, column=5)
label_szczegoly_post = Label(ramka_szczegoly_obiektow, text="Posty" )
label_szczegoly_post.grid(row=1, column=6)
label_szczegoly_post_wartosc = Label(ramka_szczegoly_obiektow, text="...." )
label_szczegoly_post_wartosc.grid(row=1, column=7)

#ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)









#my_label = Label(root, text="Mapbook SD")
#my_label.grid(column=0, row=0)
#my_button = Button(root,text="Kliknij",command=my_function)
#my_button.grid(column=0, row=1)





root.mainloop()
