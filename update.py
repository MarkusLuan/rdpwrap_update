import json
import configparser
from typing import Dict, Any

import requests

def get_ini(url: str):
    print(f"Obtendo RDPWrap.ini de {url}...")
    res = requests.get(url, timeout=200)

    if res.status_code == 200:
        print("RDPWrap.ini baixado com sucesso!")
        return res.text
    else:
        raise Exception (f"Não foi possivel baixar o RDPWrap.ini!\n{res.text}")

def update ():
    links = []
    with open("links.json", "r", encoding="utf-8") as f:
        links = json.load(f)
    
    list_rdp_ini: Dict[str, Dict[str, Any]] = {}

    a = 1
    for link in links:
        try:
            rdp_ini = get_ini(link)

            ini_parser = configparser.ConfigParser(strict=False)
            ini_parser.read_string(rdp_ini)

            version = ini_parser["Main"]["Updated"].replace("-", ".")

            list_rdp_ini[link] = {
                "version": version,
                "ini": {
                    section: dict(ini_parser.items(section))
                    for section in ini_parser.sections()
                }
            }

            with open(f"rdpwrap.{version}.ini", "w", encoding="utf-8") as f:
                f.write(rdp_ini)

        except Exception as e:
            print(f"Ocorreu um erro: {e}!")
        a+=1
    
    print(list_rdp_ini)

if __name__ == "__main__":
    update()