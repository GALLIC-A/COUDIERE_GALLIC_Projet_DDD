# Ce script permet d'insérer dans la base de données toutes les données que nous avons récoltées dans les CSV lors du module sur le DataCentric.abs
# Il alimente également la table des rôles.
# CEPENDANT, il n'alimente pas les tables user, il faudra donc s'inscrire depuis l'application ou créer un superuser depuis Django Administration.

import os
import subprocess

def check_db_exists():
    return os.path.exists("db.sqlite3")
def run_sql_file(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            sql_commands = f.read()
        import sqlite3
        conn=sqlite3.connect("db.sqlite3")
        cursor=conn.cursor()
        cursor.executescript(sql_commands)
        conn.commit()
        conn.close()
        print(f"[OK] Données insérées depuis {file_path}")
    except Exception as e:
        print(f"[ERREUR] Impossible d'insérer les données depuis {file_path} : {e}")

def main():
    print("=== Initialisation de la base de données ===")
    if not check_db_exists():
        print("[ERREUR] Le fichier db.sqlite3 n'existe pas. Avez-vous exécuté les migrations ?")
        return
    done = input("Avez-vous déjà exécuté les migrations (voir le README pour plus de détail) ? (y/N) ").strip().lower()
    if done == 'y':
        print("Insertion des données...")
        run_sql_file("inserts.sql")
        run_sql_file("insert_default_roles.sql")
    else:
        input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
