# RDPWrap Update
### Um script em python para atualizar o arquivo RDPWrap.ini para manter múltiplas conexões remotas ativas

* O script depende do [RDPWrapper do stascorp](https://github.com/stascorp/rdpwrap/) (Ou algum fork) para de fato ativar multiplas conexões.
* O script foi baseado no autoupdate do https://github.com/asmtron/rdpwrap/ e apenas utiliza de alguns links no github de terceiros para baixar a atualização.
* O arquivo [rdpwrap.ini](https://github.com/MarkusLuan/rdpwrap_update/blob/master/rdpwrap.ini) foi gerado pelo script e adicionado uma configuração funcional para a versão 10.0.19041.6456 do Windows.

### Execução
Caso possua o [Python 3](https://www.python.org/) ou deseje executar pelo código fonte...
* Faça o download do zip
* Abra o prompt de comando (cmd) ou powershell
* Execute o seguinte comando
```bash
pip install -r requirements.txt
python update.py
```

Para executar sem o python...
* Faça o download do zip
* Execute o update.exe

### Soluções de problemas
Caso mesmo após atualizar o RDPWrap ainda não funcione, tente pesquisar no Google por "RDPWrap.ini 'versão do Windows'", substituindo o 'versão do Windows' pela correspondente (por exemplo, "RDPWrap.ini 10.0.19041.6456") e se encontrar em algum forum algum trecho como
```ini
[10.0.19041.6456]
SingleUserPatch.x64=1
SingleUserOffset.x64=1842B
SingleUserCode.x64=mov_eax_1_nop_2
DefPolicyPatch.x64=1
DefPolicyOffset.x64=1F415
DefPolicyCode.x64=CDefPolicy_Query_eax_rcx
LocalOnlyPatch.x64=1
LocalOnlyOffset.x64=91A61
LocalOnlyCode.x64=jmpshort
SLInitHook.x64=1
SLInitOffset.x64=2902C
SLInitFunc.x64=New_CSLQuery_Initialize

[10.0.19041.6456-SLInit]
bServerSku.x64=125098
bRemoteConnAllowed.x64=1250AC
bFUSEnabled.x64=1250B8
bAppServerAllowed.x64=1250A0
bMultimonAllowed.x64=1250B0
lMaxUserSessions.x64=12509C
ulMaxDebugSessions.x64=1250B4
bInitialized.x64=125094
```
Insira no seu arquivo rdpwrap.ini e execute novamente o script. Caso não encontre, infelizmente terá que esperar algum desenvolvedor ajustar as configurações ou voltar a versão do Windows para uma compativel, porém não recomendo por questões de segurança.

### Links que o script faz as consultas
O Script faz consulta pelo RPDWrap através do [links.json](https://github.com/MarkusLuan/rdpwrap_update/blob/master/links.json) que contem os seguintes repositórios git:
* [rdpwrap.ini de asmtron](https://raw.githubusercontent.com/asmtron/rdpwrap/master/res/rdpwrap.ini)
* [rdpwrap.ini de sebaxakerhtc](https://raw.githubusercontent.com/sebaxakerhtc/rdpwrap.ini/master/rdpwrap.ini)
* [rdpwrap.ini de affinityv](https://raw.githubusercontent.com/affinityv/INI-RDPWRAP/master/rdpwrap.ini)
* [rdpwrap.ini de DrDrrae](https://raw.githubusercontent.com/DrDrrae/rdpwrap/master/res/rdpwrap.ini)
