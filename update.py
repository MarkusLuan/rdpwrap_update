import collections
import json
import configparser
import os
import tempfile
import time
from typing import List, Dict, Any

import requests

def get_ini(url: str):
    print(f"Obtendo RDPWrap.ini de {url}...")
    res = requests.get(url, timeout=200)

    if res.status_code == 200:
        print("RDPWrap.ini baixado com sucesso!")
        return res.text
    else:
        raise Exception (f"Não foi possivel baixar o RDPWrap.ini!\n{res.text}")

def read_ini(rdp_ini: str):
    ini_parser = configparser.ConfigParser(strict=False)

    if os.path.isfile(rdp_ini):
        ini_parser.read(rdp_ini, encoding="utf-8")
    else:
        ini_parser.read_string(rdp_ini)

    version = ini_parser["Main"]["Updated"].replace("-", ".")

    return {
        "version": version,
        "link": None,
        "ini": {
            section: dict(ini_parser.items(section))
            for section in ini_parser.sections()
        }
    }

def update ():
    links = []
    with open("links.json", "r", encoding="utf-8") as f:
        links = json.load(f)

    tmp_dir = tempfile.TemporaryDirectory(".rdp_ini")
    
    list_rdp_ini: List[Dict[str, Any]] = []
    for link in links:
        try:
            rdp_ini = get_ini(link)
            rdp_dict = read_ini(rdp_ini)
            rdp_dict["link"] = link
            list_rdp_ini.append(rdp_dict)

            with open(f"{tmp_dir.name}/rdpwrap.{rdp_dict['version']}.ini", "w", encoding="utf-8") as f:
                f.write(rdp_ini)

        except Exception as e:
            print(f"Ocorreu um erro: {e}!")
    print()

    print("Gerando backup...")
    list_rdp_ini = sorted(list_rdp_ini, key=lambda x: x["version"], reverse=False)
    list_rdp_ini_files = [f"{tmp_dir.name}/rdpwrap.{rdp['version']}.ini" for rdp in list_rdp_ini]
    if os.path.isfile("rdpwrap.ini"):
        list_rdp_ini_files = ["rdpwrap.ini"] + list_rdp_ini_files
        os.system("copy rdpwrap.ini rdpwrap.old.ini")
    
    print("Mesclando rdpwrap.inis...")
    ini_parser = configparser.ConfigParser(strict=False, dict_type=collections.OrderedDict)
    ini_parser.read(list_rdp_ini_files)

    ini_parser._sections = collections.OrderedDict(sorted(ini_parser._sections.items(), key=lambda t: t[0], reverse=True))
    
    with open ("rdpwrap.ini", "w", encoding="utf-8") as f:
        ini_parser.write(f)
    print("Arquivo RDPWrap.ini atualizado com sucesso!")

def restart_service ():
    print("Parando o serviço do TermService (RDP)...")
    os.system("net stop termservice")
    time.sleep(2)

    print("Iniciando o serviço do TermService (RDP)...")
    if os.system("net start termservice") == 0:
        print("O serviço foi reiniciado com sucesso!")
    else:
        print("Algum erro impediu que o serviço fosse reiniciado!")

if __name__ == "__main__":
    update()
    # restart_service()