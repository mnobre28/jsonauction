Abordagem:

O sistema mantêm os dados dos leilões disponíveis em memória. Quando um usuário realiza uma nova oferta (bid) pelo commando /bid o sistema atualiza as informações em memória, e em seguida salva em disco no arquivo records.json. Esse arquivo persiste no final da execução, permitindo que as ações continuem ao resumir o programa.