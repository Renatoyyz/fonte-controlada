# Projeto Fonte Controlada MAEDA

Um projeto para controle de fontes externas permitindo ciclagem de saídas

## Pré-requisitos para o sistema

Para montar um ambiente de desenvolvimento python:

```text
Python 3.8 ou superior
pip 20.0 ou superior
virtualenv 20.4 ou superior
```

Criando o ambiente virtual:

```text
python -m venv <nome-ambiente>
```

Ativar o embiente:

```text
source nome_ambiente/bin/activate
```

Com o ambiente ativado instalamos as dependências:

```text
pip install -r requirements.txt
```

Para atualizar o arquivo requirements.txt cada vez que for atualizando pacotes:

```text
pip freeze > requirements.txt
```

## Para instalar o PyQt5

O PyQt tem que ser instalado via pacote

```text
sudo apt-get update
sudo apt-get install qt5-default
sudo apt-get install qtcreator
sudo apt install pyqt5-dev-tools pyqt5-dev
```

Depois de instalado globalmente:

```text
ln -s /usr/lib/python3/dist-packages/PyQt5/ myenv/lib/python3.11/site-packages/PyQt5
```

Onde 'myenv' é o ambiente que foi criado.
Isso garante que o ambiente virtual acesse o pacote instalado globalmente.
Esses passos servem para o raspberry, em outros sistemas o PyQt5 pode ser instalado via pip

## Com o pacote PyQt5 instalado e o Qt Designer instalado

Com o Qt Designer desenvolva a tela com extensão .ui e em seguida, no direório salvo execute o comando:

```text
pyuic5 -x arquivo.ui -o arquivo.py
```

Para gerar recursos de imagens no PyQt5:

```text
pyrcc5 nome_do_recurso.qrc -o nome_do_arquivo.py
```

Esse arquivo .qrc é gerado no QT Designer e com o comando pyrcc5 faz-se a conversão para a extensão .py

Fazer comando para que inicie o Raspberry rodando a aplicação:

a) Primeiro, abra o terminal e digite o seguinte comando para criar um arquivo .desktop no diretório autostart:

```text
sudo mousepad /etc/xdg/autostart/display.desktop .
```

Usamos display.desktop como nome de arquivo, mas você pode nomear o arquivo da área de trabalho como quiser.

b) No arquivo .desktop, adicione as seguintes linhas de código:

```text
[Desktop Entry]
Name=choque-termico
Exec=/usr/bin/python /home/maeda/choque-termico/main.py
```

O diretório /usr/bin/pythyon é onde está instalado o python,normalmente no raspberry esse é o local padrão.

```
4 - Instalar o pacote para o LCD:
    a) Faca o clone: git clone https://github.com/goodtft/LCD-show.git
    b) chmod -R 755 LCD-show
    não execute o comando que habilita o LCD ainda
    link com tutorial: http://www.lcdwiki.com/3.5inch_RPi_Display

6 - Agora vá até o diretório onde foi baixado os arquivos do LCD-show:
    a) cd /home/pi/LCD-show/
    b) sudo ./LCD35-show
    executando esse último comando o sistema irá reiniciar agora com o LCD e a aplicação rodando
7 - Para sair do modo LCD-show tem que, com o teclado, apertar crtl+alt e esc ou F1 até aparecer o console, 
    depois digite LCD-hdmi. O sistema vai reiniciar e voltar com o monitor mais a aplicação. Se quiser 
    parar a aplicação abra um terminal - ctrl+alt+T e digite "ps axf" abrirá as execuções. Na coluna 
    comando procure bin/python3 e veja o número do PID em seguida execute sudo kill e o número do PID.
    
8 - Para desativar desligamneto de tela do raspberry
    Abra um terminal e instale o pacote xscreen no raspberry:
       sudo apt-get install xscreenserver
    Fazendo isso vá no menu do raspberry(canto superior esquerdo), preferencias e protetor de tela.
    Quando abrir a janela, vá em modo e desativar protetor de tela
```