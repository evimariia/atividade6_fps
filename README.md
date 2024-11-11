# Atividade 6 - Fundamentos de Programação de Sistemas
## Formulário de saudação com CGI

Neste projeto construiu-se um formulário web que captura o nome do usuário e exibe uma mensagem de saudação. Para isso foi utilizado HTML para construir o formulário e um script Bash CGI para processar a entrada e gerar a resposta.

[Clique aqui para assistir um vídeo exemplificando a execução](https://drive.google.com/file/d/14R-mPJ1bo5HEP5mjRyjaMs058UuMStJr/view?usp=drive_link)

### Estrutura do Projeto

- **form.html**: Página inicial do projeto, onde o usuário insere o nome.
- **saudacao.cgi**: Script CGI em Bash que recebe o nome inserido, processa a informação e exibe uma saudação personalizada.

### Pré-requisitos

Para rodar este projeto, é necessário:

- Um servidor web com suporte a CGI;
- Acesso ao terminal para configurar permissões e o ambiente CGI;
- Permissão de execução para o script `saudacao.cgi`.

## Configuração de CGI no Ubuntu com Apache

Para configurar o **Common Gateway Interface (CGI)** no Ubuntu, usando o servidor web **Apache**, siga o passo a passo. 

### Pré-requisitos

- Ubuntu com privilégios de superusuário (root ou sudo);
- Apache instalado.

### Passo a Passo para Configuração

#### 1. Instalar o Apache

Se o Apache ainda não estiver instalado, execute os comandos abaixo:

```bash
sudo apt update
sudo apt install apache2
```

#### 2. Habilitar o Módulo CGI no Apache

Para que o Apache suporte scripts CGI, é necessário habilitar o módulo `mod_cgi`:

```bash
sudo a2enmod cgi
```

Reinicie o Apache para aplicar as alterações:

```bash
sudo systemctl restart apache2
```

#### 3. Configurar o Diretório para Scripts CGI

Por padrão, o Apache usa o diretório `/usr/lib/cgi-bin/` para scripts CGI. Edite o arquivo de configuração do Apache para garantir que este diretório esteja configurado corretamente:

```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```

No arquivo, adicione a linha abaixo dentro do bloco `<VirtualHost>`:

```apache
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
```

#### 4. Permitir Execução de CGI no Diretório

Ainda no arquivo de configuração, defina as permissões para que o Apache possa executar scripts CGI dentro do diretório:

```apache
<Directory "/usr/lib/cgi-bin">
    Options +ExecCGI
    AddHandler cgi-script .cgi .pl .sh
    Require all granted
</Directory>
```
#### 5. Mover os Arquivos para os Diretórios Corretos
sudo mv index.html /var/www/html/

sudo mv saudacao.cgi /usr/lib/cgi-bin/

#### 6. Tornar o Script Executável

Dê permissão de execução ao script criado:

```bash
sudo chmod +x /usr/lib/cgi-bin/saudacao.cgi
```

#### 7. Reiniciar o Apache

Para aplicar todas as configurações, reinicie o Apache:

```bash
sudo systemctl restart apache2
```

#### 8. Executar o Script CGI

```
sudo /usr/lib/cgi-bin/saudacao.cgi

```


#### 9. Verificar Logs de Erro (Opcional)

Se o script não funcionar como esperado, consulte o log de erros do Apache para mais informações:

```bash
sudo tail -f /var/log/apache2/error.log
```

### 10. Executar o form.html
Abra o navegador e acesse a página HTML:
http://localhost/form.html
