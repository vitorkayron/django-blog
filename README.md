Usuário =
    class banco:
        Nome, email, senha, 
        "foto"
         - Comentar, "Filtrar",

    class post:
        title = max_lenght(),
        author = foreingkey (users),
        content = text(),
        created_on = Datefield(),
    

