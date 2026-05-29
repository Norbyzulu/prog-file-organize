"""
File Organizer Progetto:

Requisiti:
1. Gestire gli argomenti da linea di comando (sys.argv).
2. Esplorare la directory usando pathlib/os.
3. Spostare i file nella cartella corretta usando un dizionario di mappatura.

BUG ALERT: Ci sono 2 bug nascosti nel codice esistente. Trovali e correggili!
"""

import sys
from pathlib import Path

# DIZIONARIO DI MAPPATURA (Estensione -> Nome Cartella)
# TO-DO: se ci sono più tipi di file, aggiungili nel dizionario
ESTENSIONI_MAPPA = {
    '.pdf': 'Documenti',
    '.docx': 'Documenti',
    '.txt': 'Documenti',
    '.jpg': 'Immagini',
    '.png': 'Immagini',
    '.mp3': 'Musica',
    '.zip': 'Archivi'
}

def inizializza_cartelle(cartella_base: Path):
    """
    Crea le sottocartelle di destinazione se non esistono già.
    Usa i valori del dizionario ESTENSIONI_MAPPA.
    """
    print("Inizializzazione cartelle in corso...")
    # Estraiamo i nomi delle cartelle uniche dal dizionario
    cartelle_da_creare = set(ESTENSIONI_MAPPA.values())
    
    for nome_cartella in cartelle_da_creare:
        percorso_cartella = cartella_base / nome_cartella
        # TO-DO RISOLTO: Usa pathlib per creare la cartella se non esiste (suggerimento: .mkdir())
        if percorso_cartella.exists():
            continue
        percorso_cartella.mkdir()

def organizza_file(cartella_target: Path):
    """
    Scansiona la cartella target e sposta i file in base alla loro estensione.
    """
    # BUG 1 RISOLTO: C'è un problema nel modo in cui iteriamo sui file. 
    # Così come è scritto, rischiamo di scansionare ricorsivamente anche le cartelle appena create!
    for elemento in cartella_target.glob('*'):
        
        # Saltiamo le directory, vogliamo solo i file
        if elemento.is_dir():
            continue
            
        estensione = elemento.suffix.lower()
        
        # Controlliamo se l'estensione è presente nel nostro dizionario
        if estensione in ESTENSIONI_MAPPA:
            nome_cartella_dest = ESTENSIONI_MAPPA[estensione]
            nuovo_percorso = cartella_target / nome_cartella_dest / elemento.name
            
            print(f"Spostamento di {elemento.name} in {nome_cartella_dest}...")
            
            # TO-DO: Spostare fisicamente il file nel 'nuovo_percorso'
            # Suggerimento: si può usare os.rename() oppure il metodo di pathlib elemento.rename()
            elemento.rename(nuovo_percorso)
        else:
            # TO-DO (Opzionale): Gestire i file con estensioni sconosciute 
            # (es. metterli in una cartella 'Altro')
            pass

def main():
    """
    Funzione principale che gestisce l'input dell'utente da terminale.
    Uso previsto: python organizer.py /percorso/della/cartella
    """
    
    # Controllo degli argomenti passati da linea di comando
    # BUG 2 RISOLTO: Il controllo sulla lunghezza di sys.argv è errato per verificare la presenza di un argomento.
    if len(sys.argv) < 2:
        print("Errore: Devi specificare il percorso di una cartella!")
        print("Uso: python organizer.py <percorso_cartella>")
        sys.exit(1)
        
    # Prendiamo il percorso passato come argomento
    percorso_inserito = sys.argv[1]
    cartella_da_organizzare = Path(percorso_inserito)
    
    # TO-DO: Verificare se la cartella esiste veramente ed è una directory valida.
    # Se non esiste, stampare un errore e uscire con sys.exit(1).
    
    print(f"Avvio organizzazione nella cartella: {cartella_da_organizzare.absolute()}")
    
    # Esecuzione delle funzioni
    inizializza_cartelle(cartella_da_organizzare)
    organizza_file(cartella_da_organizzare)
    
    print("Organizzazione completata con successo!")

if __name__ == "__main__":
    main()