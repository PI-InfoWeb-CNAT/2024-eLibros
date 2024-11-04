# Projeto eLibros - Especificação de caso de uso

##  Acessar livro

### Histórico da Revisão 
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 16/09/2024 | **1.00** | Primeira versão  | Gabriel Campos |


### 1. Resumo 
Esse caso de uso permite ao usuário acessar a página de um livro.

### 2. Atores 
- Cliente e Visitante

### 3. Pré-condições
Não há
  
### 4. Pós-condições
Após a execução deste caso de uso, espera que o sistema:
- Mostre a página do livro acessado ao usuário

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
|  Ator  | Sistema |
|:-------|:------- |
|1. Na página de acervo, o usuário clica na aba referente a "pesquisar" e escreve o que deseja pesquisar| --- |
| --- |2. O sistema busca o texto no acervo e mostra os livros compatíveis | 


#### 5.2. Fluxo de exceção

##### 5.2.1 Não há livro ou autor com o nome pesquisado no acervo
|  Ator  | Sistema |
|:-------|:------- |
|---| --- |
| --- |2. O sistema avisa que no seu acervo não há livro ou autor com o livro  | 

### 6. Protótipos de Interface

![image](https://github.com/user-attachments/assets/92b62e4b-dabb-4d57-a8c9-5a376691735c)
![image](https://github.com/user-attachments/assets/161f4c98-73f4-4af6-81bb-9b21db9ed512)



### 7. Diagrama de classe de domínio usados neste caso de uso

A ser desenvolvido.

### 8. Dicionário de dados

#### 8.1. Livro
- Capa - Arquivo de imagem
- Título - Uma cadeia de caracteres alfabéticos tamanho 100
- Autor - Uma cadeia de caracteres alfabéticos tamanho 100

### 9. Regras de negócio

#### 9.1 Livro
- Capa - Arquivo de imagem de amanho máximo de 8 MB em algum dos seguintes formatos: PNG, JPG, JPEG, SVG, WEBP
