import pyautogui
from time import sleep
from faker import Faker
import pyperclip

# ESTAMOS TRABALHANDO EM FAZER PARA O PRIME VIDEO E TODAS AS ASSINATURAS QUE TEM NELE TAMBEM ISSO 
# PODE DEMORAR UM POUCO JA QUE TEMOS QUE MEXER NA API DO 2CAPTCH PARA RESOLVER OS CAPTCHAR DA AMAZON



fake = Faker()

first_name = fake.first_name()
    
last_name = fake.last_name()

email = f"{first_name}{last_name}@hotmail.com".lower()
senha = "" # aqui voce vai colcoar a senha que deseja para sua conta

################################
# Na parte de Baixo voce tem que colcoar os dados de um cartao para fazer a ativacao
# Nao recomendamos usar o cartao fisico ou o cartao  digital para essa automacao use 
# Um cartao temporario que certos bancos possuem que voce pode apagar ele ou ele se
# auto apaga depois de  24 horas.
################################
nomecartao = "" 
numerocartao = ""
cvv = ""
cpf = ""


################################
# como se trata de uma automacao e nao do selenium acredito que dependendo da resolucao
# do seu monitor ira ter conflitos/ para resolver qualquer futuros erros irei deixar um
# aqruivo para pegar as posicoes dos botoes  deixei o codigo todo comentado para facilitar 
# no futuro iremos usar a biblioteca selenium para deixar o   programa para todos os tipos
# de plataforma
################################


# Conteúdo do login e senha
login_content = f"login: {email}\nsenha: {senha}"

# Salvar o conteúdo em um arquivo de texto
with open("login_Crunch.txt", "w") as file:
    file.write(login_content)

# Espera 2 segundos antes de começar
sleep(2)

# Abre o menu Executar (Windows + R)
pyautogui.hotkey('winleft', 'r')
sleep(1)

# Digita o nome do navegador (ex: chrome) e pressiona Enter
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(1)
pyautogui.hotkey('winleft', 'right')
#espera o navegador abrir
sleep(3)
#escolher como usuario visitante
pyautogui.click(x=1405, y=1338)
sleep(2)
pyautogui.hotkey('winleft', 'right')
sleep(2)
#pesquisa esse site
pyautogui.write('https://www.crunchyroll.com/pt-br/premium?referrer=newweb_organic_header&return_url=https%3A%2F%2Fwww.crunchyroll.com%2Fpt-br%2F%3Fsrsltid%3DAfmBOoq31Tkmm7-fSJPHHPNDMgZPJz1pUGa4H-gLzAYBaf-jL3f1Nz7g#plans')
sleep(1)
pyautogui.press('enter')
sleep(10)
#aqqui ele clica no botao de testar 7 dias gratis
pyautogui.click(x=1921, y=575)
sleep(5)
#aqui ele clica no prompt do email
pyautogui.click(x=1887, y=511)
sleep(2)
#escreve o email
pyautogui.write(email)
sleep(2)
#dar entender pra aparecer o prompt da senha
pyautogui.press('enter')
sleep(2)

#aqui ele clica no prompt da senha
pyautogui.click(x=1816, y=570)
sleep(2)

#escreve a senha
pyautogui.write(senha)
sleep(2)

#dar enter pra logar
pyautogui.press('enter')
sleep(20)

#aqui ele clica no botao de adicionar um novo cartao
pyautogui.click(x=1741, y=483)
sleep(1)

#aqui ele clica no prompt do nome do cartao
pyautogui.write(nomecartao)
sleep(1)

#aqui ele clica no prompt do numero do cartao
pyautogui.click(x=1644, y=537)
sleep(1)

#aqui ele clica no prompt do numero do cartao 2
pyperclip.copy(numerocartao)
#aqui ele cola o cartao no prompt do numero do cartao e necessario que ele cole
pyautogui.hotkey("ctrl", "v")
sleep(1)

#aqui ele clica no aba pra descer e poder de escolher o mes do vencimento
pyautogui.click(x=1662, y=588)
sleep(1)

#aqui ele clica no aba pra descer e poder de escolher o mes do vencimento
pyautogui.click(x=1664, y=668)
sleep(1)

#aqui ele clica no aba pra descer e poder de escolher o ano do vencimento
pyautogui.click(x=1876, y=583)
sleep(1)
#aqui ele clica no aba pra descer e poder de escolher o ANO do vencimento
pyautogui.click(x=1855, y=832)
sleep(1)
#aqui ele cliva no prompt do cvv
pyautogui.click(x=2100, y=587)
sleep(1)

#aqui ele escreve o cvv do cartao
pyautogui.write(cvv)
sleep(3)
#aqui ele cliva no prompt do cpf
pyautogui.click(x=2120, y=661)
sleep(3)
#aqui ele cola o cartao no prompt do cpf e necessario que ele cole
pyperclip.copy(cpf)
pyautogui.hotkey("ctrl", "v")
sleep(4)


