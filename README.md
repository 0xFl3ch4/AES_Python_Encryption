# AES_Python_Encryption

Encriptação de ficheiros com AES-CBC 

## Descrição

Este projeto foi desenvolvido por Ricardo Ferreira no âmbito da disciplina de Segurança Informática. 
O objetivo do projeto é criar um programa em Python que permita a encriptação de arquivos utilizando o algoritmo de criptografia AES no modo CBC.

O algoritmo AES (Advanced Encryption Standard) é um algorimo de criptografia simétrica amplamente utilizado para proteger informações confidenciais. O modo CBC (Cipher Block Chaining) é um dos modos de operação do AES e adiciona uma camada extra de segurança à criptografia.

## Funcionalidades

- Encriptação de arquivos utilizando uma palavra-passe como chave de criptografia.
- Utilização do algoritmo AES no modo CBC para garantir a segurança dos dados.
- Desencriptar os arquivos encriptados utilizando a mesma palavra-chave.

## Requisitos do Sistema

- Python 3
- Biblioteca de criptografia Crypto

## Como Usar

1. Clone este repositório para o seu ambiente local.
2. Certifique-se que tem o Python instalado no sistema.
3. Instale a biblioteca Crypto executando o seguinte comando no terminal:
   ```
   pip install Crypto
   ```

4. Execute o programa Python `aes.py` e selecione a opção "E" para encriptar um ficheiro:
   ```
   python aes.py
   ```
5. Siga as instruções fornecidas pelo programa para selecionar o arquivo a ser encriptado e definir a palavra-chave para o mesmo.
6. O arquivo encriptado será salvo com o mesmo nome e um prefixo "enc_" adicionado ao inicio do nome.
7. Execute o programa Python `aes.py` e selecione a opção "D" para desencriptar o ficheiro:
   ```
   python aes.py
   ```
8. Siga as instruções fornecidas pelo programa para selecionar o arquivo encriptado e inserir a palavra-chave utilizada na encriptação.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull.

## Licença

Este projeto é licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Sinta-se à vontade para utilizar, modificar e distribuir o código conforme necessário.
Projecto realizado no ambito da disciplina de Segurança Informática
