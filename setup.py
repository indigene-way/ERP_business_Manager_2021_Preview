"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "MyGrocery",
    version = "2.0.0 Classic Pack 7 DAYS DEMO",
    description = "Buisiness Manager Solution, Gestionnaire de Superete et point de vente et prise en charge de caisse...",
    executables = [Executable("MyManagerSys_DEMO.py")]
)