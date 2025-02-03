# Projeto eLibros - Especificação de caso de uso

##  Criar conta

### Histórico da Revisão 
|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 15/08/2024 | **1.00** | Primeira versão  | Os Integradores |
| 06/09/2024 | **1.10** | Atualização dicionário de dados | Cortez |
| 04/11/2024 | **1.20** | Adição de protótipo de interface  | Gabriel Campos |
| 02/02/2024 | **1.30** | Atualização dicionário de dados adição diagrama de classe  | Gabriel Campos |



### 1. Resumo 
Este caso de uso permite ao visitante a criação de conta no eLibros.

### 2. Atores 
- Visitante

### 3. Pré-condições
São pré-condições para iniciar este caso de uso:
- Visitante não deve possuir cadastro na loja, ou seja, se tentar logar com um email de sua posse e senha, a autenticação e autorização aos recursos falhará.

### 4. Pós-condições
Após a execução deste caso de uso, espera-se que:
- Cliente possa efetuar compra, ter acesso aos livros salvos no carrinho entre sessões...

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
|  Ator  | Sistema |
|:-------|:------- |
|1. Visitante clica no botão "Cadastrar"  | --- |
| ---                                     | 2. Sistema redireciona para interface de cadastro | 
|3. Visitante fornece email e senha | --- |
| --- | 4. Conta é criada com sucesso |

#### 5.2. Fluxo de exceção

**EX:**

##### 5.2.1 Valor em branco
|  Ator  | Sistema |
|:-------|:------- |
|3. Visitante não preenche um ou mais campos de dados | --- |
|--- |4. O sistema exibe mensagem de aviso "Campo não pode ser vazio" |

### 6. Protótipos de Interface
![image](https://github.com/user-attachments/assets/cde27ad3-2665-4ef3-b754-056fbc2b4abe)
![image](https://github.com/user-attachments/assets/47a82928-38d6-41da-9d0e-2a9e8b1c8e19)



### 7. Diagrama de classe de domínio usados neste caso de uso
![image](https://github.com/user-attachments/assets/568f2d0f-9b43-4653-ab07-7a74d4855a13)


### 8. Dicionário de dados

#### 8.1. Cliente
![image](https://github.com/user-attachments/assets/35fd7419-27a9-412f-a754-e597731b94b9)


### 9. Regras de negócio
-   E-mail - Um conjunto de caracteres (com exceção dos caracteres especiais, sendo permitido apenas o ponto) seguidos, respectivamente, por um arroba, outro conjunto de letras e um ou mais domínios de topo
-   Senha - Mínimo de 8 caracteres; pelo menos uma letra maiúscula e minúscula; um número; um caractere especial
