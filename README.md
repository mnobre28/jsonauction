Abordagem:
O sistema mantêm os dados dos leilões disponíveis em memória. Quando um usuário realiza uma nova oferta (bid) pelo commando /bid o sistema atualiza as informações em memória, e em seguida salva em disco no arquivo records.json. Esse arquivo persiste no final da execução, permitindo que as ações continuem ao resumir o programa.

Arquitetura:
O projeto está divido entre: 
	o arquivo contendo o app e seus requests possíveis em app.py, por via de simplicidade. 
	A pasta testes, com os testes de API e os testes de funcionalidade da classe auxiliar auction_manager.
	A classe auction_manager, que gerencia a manipulação de dados em memória e os salva na pasta files.
	Por último a própria pasta files, que contém records.json. Esse arquivo mantêm as informações salvas entre execuções do aplicativo.

Executando testes:
Acesse o diretório jsonauction, e então execute o comando python -m unittest discover -s tests -t tests
Para os testes de API, é necessário que um servidor esteja disponível.

Executando a aplicação:
Inicie o start.sh. Isso irá rodar a aplicação no servidor local. Utilize um aplicativo para enviar requisições:
- GET: /stats
	Retorna o histórico de leilões e ofertas.
- POST: /bid
	Requer um arquivo json. Registra uma nova oferta de compra e salva as informações.