package algoritmi_za_nizove_i_arrayliste;

import java.util.ArrayList;
import java.util.Arrays;

public class OsnovniAlgoritmi {

	public static Object[] pocetniNiz = new Object[] {"Neki string1", "Neki string2", "Neki string3", "element", "element", "element", 10, 11, 12};
	
	public static void dodajElement1 (Object element) {  //nema sta da vraca jer ce se element dodati svakako
		Object[] noviNiz = new Object[pocetniNiz.length + 1];
		for(int i = 0; i < pocetniNiz.length; i++) {
			noviNiz[i] = pocetniNiz[i];
		}
		noviNiz[noviNiz.length - 1] = element;
		pocetniNiz = noviNiz;
	}
	
	public static boolean ukloniElement1 (Object element) {
		for(int i = 0; i < pocetniNiz.length; i++) {
			if(pocetniNiz[i].equals(element)) {
				for(int c = i; c < pocetniNiz.length - 1; c++) {  //ide do length - 1, jer posle njega nemamo nista levo!!!
					pocetniNiz[c] = pocetniNiz[c + 1];
				}
				Object[] noviNiz = new Object[pocetniNiz.length - 1];
				for(int c = 0; c < noviNiz.length; c++) {
					noviNiz[c] = pocetniNiz[c];
				}
				pocetniNiz = noviNiz;
				return true;
			}
		}
		System.out.println("Element ne postoji!!");
		return false;
	}
	
	public static void dodajElement2 (Object element) {
		ArrayList<Object> lista = new ArrayList<Object> (Arrays.asList(pocetniNiz));
		lista.add(element);
		pocetniNiz = lista.toArray(pocetniNiz);
	}
	
	public static boolean ukloniElement2 (Object element) {  
		for(int i = 0; i < pocetniNiz.length; i++) {  
			if(pocetniNiz[i].equals(element)) {    //ova provera uopste nije bila potrebna, mogao sam samo staviti void i onda prvi for i if ne bi trebali
				ArrayList<Object> lista = new ArrayList<Object>(Arrays.asList(pocetniNiz));
				lista.remove(element);
				pocetniNiz = lista.toArray(pocetniNiz);
				
				Object[] noviNiz = new Object[pocetniNiz.length - 1];
				for(int c = 0; c < noviNiz.length; c++) {
					noviNiz[c] = pocetniNiz[c];
				}
				pocetniNiz = noviNiz;
				return true;
			}
		}
		System.out.println("Element ne postoji!!");
		return false;
	}
	
	public static void ukloniSveIste (Object element) {
		for(int i = 0; i < pocetniNiz.length; i++) {
			while(pocetniNiz[i].equals(element)) {
				ukloniElement1(element);
			}
		}
	}
	
	public static void ukloniSve() {
		pocetniNiz = new Object[0];   //samo stavim da ima 0 elemenata
	}

	// ovo su samo osnovni algoritmi, bez dodatnih provera (koji bi trebalo da ima)
	// vecina je slicna onima iz klase DinamickiNiz (projekat vezbe 8, paket zad2)
	
	public static void main(String[] args) {
		
		System.out.println("Niz: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println("**********************************************************");
		
		OsnovniAlgoritmi.dodajElement1("Kupus");
		System.out.println("Niz nakon prvog dodavanja elementa je: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println();
		
		OsnovniAlgoritmi.ukloniElement1(11);
		System.out.println("Niz nakon prvog uklanjanja elementa je: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println();
			
		OsnovniAlgoritmi.dodajElement2(152427);
		System.out.println("Niz nakon drugog dodavanja elementa je: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println();
		
		OsnovniAlgoritmi.ukloniElement2("Neki string1");
		System.out.println("Niz nakon drugog uklanjanja elementa je: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println();
		
		OsnovniAlgoritmi.ukloniElement2("Neki string3");
		System.out.println("Niz nakon treceg uklanjanja elementa je: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println();
		
		OsnovniAlgoritmi.ukloniSveIste("element");
		System.out.println("Niz nakon cetvrtog uklanjanja elementa je: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println();
		
		OsnovniAlgoritmi.ukloniSve();
		System.out.println("Niz nakon petog uklanjanja elementa je: " + "\n" + Arrays.toString(pocetniNiz));
		System.out.println();
		
		
		/*
		  Kako se ubacuju elementi u niz?
		  
		  1. Imam neki pocetniNiz
		  2. Napravim noviNiz koji ima duzinu pocetniNiz.length + 1
		  3. Preko for petlje prodjem kroz pocetni niz, i novi niz ubacim sve elemente pocetnog niza. ---> (noviNiz[i] = pocetniNiz[i]
		  4. Izvan petlje... stavim element koji treba da se doda u noviNiz ---> noviNiz[noviNiz.length - 1] = element
		  5. Pocetnom nizu dodelim vrednost novog niza ---> pocetniNiz = noviNiz (mogu i ovde da stavim element na poslednj indeks)
		  
		  Kako se brisu elementi iz niza?
		  
		  1. Imam neki pocetniNiz                    																									for(int i = pocetak; i < pocetniNiz.length - 1; i++)  idem do length - 1 !!!!!!!!										
		  2. Ako znam poziciju elementa, for petljom prodjem kroz niz i od te pozicije (pozicije elementa koji hocu da obrisem) pa do kraja pomerim sve na levo ---> pocetniNiz[i] = pocetniNiz[i + 1]
		  4. Napravim noviNiz koji ima duzinu pocetniNiz.length - 1
		  5. Preko for petlje prodjem kroz novi niz, i u njega ubacim sve elemente pocetnog niza. ---> (noviNiz[i] = pocetniNiz[i]
		  6. Pocetnom nizu dodelim vrednost novog niza ---> pocetniNiz = noviNiz
		  
		  // sve ovo sam gore radio sa ArralList-ama jer je lakse i ima manje koda
		  // iskoristim niz koji treba da se menja, od njega napravim listu, uradim sta treba i ponovo ga vratim u niz
		  
		  */
		

	}

}
