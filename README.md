# DCS-RecoverJoystickConfig


## COMO USAR!!!!

1 -     Pegue seu id do hardware do seu joystick no sistema**

2 -     Abra o CMD (Prompt de comando)

3 -     Escreva no terminal: `changeHardwareId.exe <LOCAL DA PASTA SAVED GAMES DCS (COM ASPAS DUPLA)> <ID DO SEU NOVO JOYSTICK>`

4 -     Exemplo: `changeHardwareId.exe "C:\Users\felip\Saved Games\DCS.openbeta" B13BE940-DAA6-11e8-8001-444553540000`


## COMO PEGAR O ID DO JOYSTICK

0 -     Insira o seu joystick e abra o DCS, entra em algum modulo e mude alguma config do controle do seu joystick, salva e fecha o DCS

1 -     Na pasta: `C:\Users<SEU USUARIO>\Saved Games\DCS.openbeta"`

2 -     Destro da raiz do DCS(SAVED GAMES), va na pasta `\Config\Input`

3 -     Escolha o modulo que foi modificado

4 -     Na pasta do modulo, va na pasta:  `\joystick`

5 -     Vai ter os arquivos .diff.lua, filtra a lista pra mostrar o arquivo mais recente

6 -     O ID estará no nome desse arquivo,  exemplo: `MetalStrike Pro {A25905C0-036A-11e8-8003-444553540000}.diff,    ID = A25905C0-036A-11e8-8003-44455354000`
