from pyscript import document

def berechne_summe(event):
    try:
        zahl1 = float(document.querySelector("#zahl1").value)
        zahl2 = float(document.querySelector("#zahl2").value)
        summe = zahl1 + zahl2
        document.querySelector("#ergebnis").innerText = f"Die Summe ist: {summe}"
    except:
        document.querySelector("#ergebnis").innerText = "Ungültige Eingabe!"