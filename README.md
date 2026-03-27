## 📌 Levantamento de Requisitos

### 🎯 Objetivo do Sistema

Desenvolver um sistema web para controle e acompanhamento de processos, permitindo gerenciar status, prazos e responsáveis, garantindo organização e visibilidade das entregas.

---

### 👥 Usuários do Sistema

* Analistas
* Administradores

---

### ✅ Requisitos Funcionais

#### 📊 Controle Geral

* RF01: O sistema deve exibir o total de processos cadastrados
* RF02: O sistema deve exibir o total de processos entregues
* RF03: O sistema deve exibir o total de processos faltantes
* RF04: O sistema deve exibir se o processo foi enviado ao protocolo
* RF05: O sistema deve exibir a data de envio ao protocolo

---

#### 📁 Cadastro de Processos

* RF06: O sistema deve permitir cadastrar um processo com os seguintes campos:

  * Número do processo
  * Tipo (Acesso ou Energia)
  * Interessado
  * Rodovia
  * Trecho
  * Data de entrada da análise
  * Data de entrega
  * NTI
  * Data de despacho
  * Responsável
  * Observações

---

#### 🔄 Atualização de Processos

* RF07: O sistema deve permitir editar um processo
* RF08: O sistema deve permitir excluir um processo
* RF09: O sistema deve permitir atualizar o status do processo (enviado ao protocolo ou não)

---

#### 🔍 Consulta de Processos

* RF10: O sistema deve permitir visualizar todos os processos cadastrados
* RF11: O sistema deve permitir filtrar processos por:

  * Tipo
  * Responsável
  * Status

---

### ⚙️ Requisitos Não Funcionais

* RNF01: O sistema deve ser acessível via navegador (web)
* RNF02: O sistema deve ser desenvolvido utilizando Python com Flask
* RNF03: O banco de dados deve ser PostgreSQL
* RNF04: O sistema deve suportar múltiplos usuários simultaneamente
* RNF05: O sistema deve ter tempo de resposta inferior a 2 segundos
* RNF06: Os dados devem ser armazenados de forma segura

---

### 📏 Regras de Negócio

* RN01: Um processo só pode ser marcado como "entregue" se tiver data de entrega
* RN02: O número do processo deve ser único
* RN03: Ao marcar como "enviado ao protocolo", o sistema deve registrar automaticamente a data
* RN04: A data de entrega não pode ser anterior à data de entrada da análise

---

### 🚫 Restrições

* Backend: Python (Flask)
* Banco de dados: PostgreSQL
* Interface inicial: HTML/CSS simples
