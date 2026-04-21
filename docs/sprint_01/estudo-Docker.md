1. O que é Docker?
Docker é uma ferramenta que empacota sua aplicação junto com tudo que ela precisa, garantindo que ela funcione em qualquer lugar.

2. Container vs Máquina Virtual
Máquina Virtual simula um computador inteiro, com sistema operacional completo. É pesada e demora para iniciar.

O Container compartilha o sistema operacional da máquina hospedeira, carregando apenas o necessário. É leve e inicia em segundos.

3. Os termos que você precisa entender
Imagem: é a receita do bolo. Ela contém todas as instruções e ingredientes necessários para criar um container. Você não altera a imagem diretamente, ela é um modelo.

Container: é o bolo pronto. Ele é criado a partir de uma imagem e é onde sua aplicação realmente roda. Você pode criar vários containers a partir de uma mesma imagem.

Dockerfile: é o arquivo de texto onde você escreve a receita. Nele você define qual sistema usar, quais arquivos copiar, quais comandos executar, etc.

Dockerhub: é o repositório público de imagens. Funciona como uma loja de receitas prontas. Lá você encontra imagens de bancos de dados, linguagens de programação, servidores, etc.

Docker Engine: é o motor que faz tudo funcionar. Ele lê suas instruções e cria containers.

4. Como funciona na prática (fluxo básico)
Você descreve um Dockerfile com as instruções que sua aplicação precisa.
A partir desse arquivo, você constrói uma imagem.
A partir dessa imagem, você cria e roda um container.
Se você quiser, pode enviar essa imagem para o Docker Hub para várias pessoas usarem.

5. Boas Práticas
Usar imagens leves para não desperdiçar recursos.

Não rodar aplicações como administrador dentro do container por questões de segurança.

Manter o Dockerfile o mais simples possível.

Ignorar arquivos desnecessários na hora de criar uma imagem.

Sempre versionar suas imagens para ter controle do que está rodando.

Referências
Documentação Oficial do Docker -https://docs.docker.com/get-started/
O que é Docker? - https://www.redhat.com/pt-br/topics/containers/what-is-docker
Docker em 22 Minutos - https://www.youtube.com/watch?v=KczhlcwEXJ4