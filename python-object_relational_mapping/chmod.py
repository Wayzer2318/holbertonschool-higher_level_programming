import os
import sys

def chmod_777(filename):
    try:
        # Vérifier si le fichier existe
        if os.path.exists(filename):
            # Changer les permissions du fichier en 0o777 (décimal)
            os.chmod(filename, 0o777)
            print(f"Les permissions du fichier '{filename}' ont été modifiées à 777.")
        else:
            print(f"Le fichier '{filename}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <nom_du_fichier>")
        sys.exit(1)

    fichier_a_chmod = sys.argv[1]
    chmod_777(fichier_a_chmod)
