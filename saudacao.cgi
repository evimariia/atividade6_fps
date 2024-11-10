#!/bin/bash

# Informar ao navegador que é uma resposta HTML
echo "Content-Type: text/html"
echo ""

# Ler o input do formulário enviado via POST
read -r input

# Extrair o valor do campo "nome" enviado no formulário
# O campo nome será codificado como "nome=valor", então usamos cut para capturá-lo
nome=$(echo "$input" | sed 's/^nome=//' | sed 's/+/ /g' | xargs -0 printf '%b\n')

# Gerar a resposta HTML com a saudação personalizada
echo "<!DOCTYPE html>"
echo "<html lang=\"pt-br\">"
echo "<head>"
echo "    <meta charset=\"UTF-8\">"
echo "    <title>Saudação</title>"
echo "</head>"
echo "<body>"
echo "    <h2>Olá, $nome!</h2>"
echo "    <p>Seja bem-vindo(a)!</p>"
echo "</body>"
echo "</html>"
