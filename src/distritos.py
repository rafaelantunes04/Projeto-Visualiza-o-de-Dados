import pandas as pd

DICIONARIO_DISTRITOS = {
    # Distrito de Aveiro
    "Águeda": "Distrito de Aveiro","Albergaria-a-Velha": "Distrito de Aveiro","Anadia": "Distrito de Aveiro",
    "Arouca": "Distrito de Aveiro","Aveiro": "Distrito de Aveiro","Castelo de Paiva": "Distrito de Aveiro",
    "Espinho": "Distrito de Aveiro","Estarreja": "Distrito de Aveiro","Santa Maria da Feira": "Distrito de Aveiro",
    "Ílhavo": "Distrito de Aveiro","Mealhada": "Distrito de Aveiro","Murtosa": "Distrito de Aveiro",
    "Oliveira de Azeméis": "Distrito de Aveiro","Oliveira do Bairro": "Distrito de Aveiro",
    "Ovar": "Distrito de Aveiro","São João da Madeira": "Distrito de Aveiro","Sever do Vouga": "Distrito de Aveiro",
    "Vagos": "Distrito de Aveiro","Vale de Cambra": "Distrito de Aveiro",

    # Distrito de Beja
    "Aljustrel": "Distrito de Beja","Almodôvar": "Distrito de Beja","Alvito": "Distrito de Beja",
    "Barrancos": "Distrito de Beja","Beja": "Distrito de Beja","Castro Verde": "Distrito de Beja",
    "Cuba": "Distrito de Beja","Ferreira do Alentejo": "Distrito de Beja","Mértola": "Distrito de Beja",
    "Moura": "Distrito de Beja","Odemira": "Distrito de Beja","Ourique": "Distrito de Beja",
    "Serpa": "Distrito de Beja","Vidigueira": "Distrito de Beja",

    # Distrito de Braga
    "Amares": "Distrito de Braga","Barcelos": "Distrito de Braga","Braga": "Distrito de Braga",
    "Cabeceiras de Basto": "Distrito de Braga","Celorico de Basto": "Distrito de Braga",
    "Esposende": "Distrito de Braga","Fafe": "Distrito de Braga","Guimarães": "Distrito de Braga",
    "Póvoa de Lanhoso": "Distrito de Braga","Terras de Bouro": "Distrito de Braga","Vieira do Minho": "Distrito de Braga",
    "Vila Nova de Famalicão": "Distrito de Braga","Vila Verde": "Distrito de Braga","Vizela": "Distrito de Braga",

    # Distrito de Bragança
    "Alfândega da Fé": "Distrito de Bragança","Bragança": "Distrito de Bragança","Carrazeda de Ansiães": "Distrito de Bragança",
    "Freixo de Espada à Cinta": "Distrito de Bragança","Macedo de Cavaleiros": "Distrito de Bragança",
    "Miranda do Douro": "Distrito de Bragança","Mirandela": "Distrito de Bragança","Mogadouro": "Distrito de Bragança",
    "Torre de Moncorvo": "Distrito de Bragança","Vila Flor": "Distrito de Bragança","Vimioso": "Distrito de Bragança",
    "Vinhais": "Distrito de Bragança",

    # Distrito de Castelo Branco
    "Belmonte": "Distrito de Castelo Branco","Castelo Branco": "Distrito de Castelo Branco",
    "Covilhã": "Distrito de Castelo Branco","Fundão": "Distrito de Castelo Branco","Idanha-a-Nova": "Distrito de Castelo Branco",
    "Oleiros": "Distrito de Castelo Branco","Penamacor": "Distrito de Castelo Branco","Proença-a-Nova": "Distrito de Castelo Branco",
    "Sertã": "Distrito de Castelo Branco","Vila de Rei": "Distrito de Castelo Branco","Vila Velha de Ródão": "Distrito de Castelo Branco",

    # Distrito de Coimbra
    "Arganil": "Distrito de Coimbra","Cantanhede": "Distrito de Coimbra","Coimbra": "Distrito de Coimbra",
    "Condeixa-a-Nova": "Distrito de Coimbra","Figueira da Foz": "Distrito de Coimbra","Góis": "Distrito de Coimbra",
    "Lousã": "Distrito de Coimbra","Mira": "Distrito de Coimbra","Miranda do Corvo": "Distrito de Coimbra",
    "Montemor-o-Velho": "Distrito de Coimbra","Oliveira do Hospital": "Distrito de Coimbra","Pampilhosa da Serra": "Distrito de Coimbra",
    "Penacova": "Distrito de Coimbra","Penela": "Distrito de Coimbra","Soure": "Distrito de Coimbra",
    "Tábua": "Distrito de Coimbra","Vila Nova de Poiares": "Distrito de Coimbra",

    # Distrito de Évora
    "Alandroal": "Distrito de Évora","Arraiolos": "Distrito de Évora","Borba": "Distrito de Évora",
    "Estremoz": "Distrito de Évora","Évora": "Distrito de Évora","Montemor-o-Novo": "Distrito de Évora",
    "Mora": "Distrito de Évora","Mourão": "Distrito de Évora","Portel": "Distrito de Évora",
    "Redondo": "Distrito de Évora","Reguengos de Monsaraz": "Distrito de Évora","Vendas Novas": "Distrito de Évora",
    "Viana do Alentejo": "Distrito de Évora","Vila Viçosa": "Distrito de Évora",

    # Distrito de Faro
    "Albufeira": "Distrito de Faro","Alcoutim": "Distrito de Faro","Aljezur": "Distrito de Faro",
    "Castro Marim": "Distrito de Faro","Faro": "Distrito de Faro","Lagoa": "Distrito de Faro",
    "Lagos": "Distrito de Faro","Loulé": "Distrito de Faro","Monchique": "Distrito de Faro",
    "Olhão": "Distrito de Faro","Portimão": "Distrito de Faro","São Brás de Alportel": "Distrito de Faro",
    "Silves": "Distrito de Faro","Tavira": "Distrito de Faro","Vila do Bispo": "Distrito de Faro",
    "Vila Real de Santo António": "Distrito de Faro",

    # Distrito da Guarda
    "Aguiar da Beira": "Distrito da Guarda","Almeida": "Distrito da Guarda","Celorico da Beira": "Distrito da Guarda",
    "Figueira de Castelo Rodrigo": "Distrito da Guarda","Fornos de Algodres": "Distrito da Guarda","Gouveia": "Distrito da Guarda",
    "Guarda": "Distrito da Guarda","Manteigas": "Distrito da Guarda","Mêda": "Distrito da Guarda",
    "Pinhel": "Distrito da Guarda","Sabugal": "Distrito da Guarda","Seia": "Distrito da Guarda",
    "Trancoso": "Distrito da Guarda","Vila Nova de Foz Côa": "Distrito da Guarda",

    # Distrito de Leiria
    "Alcobaça": "Distrito de Leiria","Alvaiázere": "Distrito de Leiria","Ansião": "Distrito de Leiria",
    "Batalha": "Distrito de Leiria","Bombarral": "Distrito de Leiria","Caldas da Rainha": "Distrito de Leiria",
    "Castanheira de Pêra": "Distrito de Leiria","Figueiró dos Vinhos": "Distrito de Leiria","Leiria": "Distrito de Leiria",
    "Marinha Grande": "Distrito de Leiria","Nazaré": "Distrito de Leiria","Óbidos": "Distrito de Leiria",
    "Pedrógão Grande": "Distrito de Leiria","Peniche": "Distrito de Leiria","Pombal": "Distrito de Leiria",
    "Porto de Mós": "Distrito de Leiria",

    # Distrito de Lisboa
    "Alenquer": "Distrito de Lisboa","Amadora": "Distrito de Lisboa","Arruda dos Vinhos": "Distrito de Lisboa",
    "Azambuja": "Distrito de Lisboa","Cadaval": "Distrito de Lisboa","Cascais": "Distrito de Lisboa",
    "Lisboa": "Distrito de Lisboa","Loures": "Distrito de Lisboa","Lourinhã": "Distrito de Lisboa",
    "Mafra": "Distrito de Lisboa","Odivelas": "Distrito de Lisboa","Oeiras": "Distrito de Lisboa",
    "Sintra": "Distrito de Lisboa","Sobral de Monte Agraço": "Distrito de Lisboa","Torres Vedras": "Distrito de Lisboa",
    "Vila Franca de Xira": "Distrito de Lisboa",

    # Distrito de Portalegre
    "Alter do Chão": "Distrito de Portalegre","Arronches": "Distrito de Portalegre","Avis": "Distrito de Portalegre",
    "Campo Maior": "Distrito de Portalegre","Castelo de Vide": "Distrito de Portalegre","Crato": "Distrito de Portalegre",
    "Elvas": "Distrito de Portalegre","Fronteira": "Distrito de Portalegre","Gavião": "Distrito de Portalegre",
    "Marvão": "Distrito de Portalegre","Monforte": "Distrito de Portalegre","Nisa": "Distrito de Portalegre",
    "Ponte de Sor": "Distrito de Portalegre","Portalegre": "Distrito de Portalegre","Sousel": "Distrito de Portalegre",

    # Distrito do Porto
    "Amarante": "Distrito do Porto","Baião": "Distrito do Porto","Felgueiras": "Distrito do Porto",
    "Gondomar": "Distrito do Porto","Lousada": "Distrito do Porto","Maia": "Distrito do Porto",
    "Marco de Canaveses": "Distrito do Porto","Matosinhos": "Distrito do Porto","Paços de Ferreira": "Distrito do Porto",
    "Paredes": "Distrito do Porto","Penafiel": "Distrito do Porto","Porto": "Distrito do Porto",
    "Póvoa de Varzim": "Distrito do Porto","Santo Tirso": "Distrito do Porto","Trofa": "Distrito do Porto",
    "Valongo": "Distrito do Porto","Vila do Conde": "Distrito do Porto","Vila Nova de Gaia": "Distrito do Porto",

    # Distrito de Santarém
    "Abrantes": "Distrito de Santarém","Alcanena": "Distrito de Santarém","Almeirim": "Distrito de Santarém",
    "Alpiarça": "Distrito de Santarém","Benavente": "Distrito de Santarém","Cartaxo": "Distrito de Santarém",
    "Chamusca": "Distrito de Santarém","Constância": "Distrito de Santarém","Coruche": "Distrito de Santarém",
    "Entroncamento": "Distrito de Santarém","Ferreira do Zêzere": "Distrito de Santarém","Golegã": "Distrito de Santarém",
    "Mação": "Distrito de Santarém","Ourém": "Distrito de Santarém","Rio Maior": "Distrito de Santarém",
    "Salvaterra de Magos": "Distrito de Santarém","Santarém": "Distrito de Santarém","Sardoal": "Distrito de Santarém",
    "Tomar": "Distrito de Santarém","Torres Novas": "Distrito de Santarém","Vila Nova da Barquinha": "Distrito de Santarém",

    # Distrito de Setúbal
    "Alcácer do Sal": "Distrito de Setúbal","Alcochete": "Distrito de Setúbal","Almada": "Distrito de Setúbal",
    "Barreiro": "Distrito de Setúbal","Grândola": "Distrito de Setúbal","Moita": "Distrito de Setúbal",
    "Montijo": "Distrito de Setúbal","Palmela": "Distrito de Setúbal","Santiago do Cacém": "Distrito de Setúbal",
    "Seixal": "Distrito de Setúbal","Sesimbra": "Distrito de Setúbal","Setúbal": "Distrito de Setúbal",
    "Sines": "Distrito de Setúbal",

    # Distrito de Viana do Castelo
    "Arcos de Valdevez": "Distrito de Viana do Castelo","Caminha": "Distrito de Viana do Castelo","Melgaço": "Distrito de Viana do Castelo",
    "Monção": "Distrito de Viana do Castelo","Paredes de Coura": "Distrito de Viana do Castelo","Ponte da Barca": "Distrito de Viana do Castelo",
    "Ponte de Lima": "Distrito de Viana do Castelo","Valença": "Distrito de Viana do Castelo","Viana do Castelo": "Distrito de Viana do Castelo",
    "Vila Nova de Cerveira": "Distrito de Viana do Castelo",

    # Distrito de Vila Real
    "Alijó": "Distrito de Vila Real","Boticas": "Distrito de Vila Real","Chaves": "Distrito de Vila Real",
    "Mesão Frio": "Distrito de Vila Real","Mondim de Basto": "Distrito de Vila Real","Montalegre": "Distrito de Vila Real",
    "Murça": "Distrito de Vila Real","Peso da Régua": "Distrito de Vila Real","Ribeira de Pena": "Distrito de Vila Real",
    "Sabrosa": "Distrito de Vila Real","Santa Marta de Penaguião": "Distrito de Vila Real","Valpaços": "Distrito de Vila Real",
    "Vila Pouca de Aguiar": "Distrito de Vila Real","Vila Real": "Distrito de Vila Real",

    # Distrito de Viseu
    "Armamar": "Distrito de Viseu","Carregal do Sal": "Distrito de Viseu","Castro Daire": "Distrito de Viseu",
    "Cinfães": "Distrito de Viseu","Lamego": "Distrito de Viseu","Mangualde": "Distrito de Viseu",
    "Moimenta da Beira": "Distrito de Viseu","Mortágua": "Distrito de Viseu","Nelas": "Distrito de Viseu",
    "Oliveira de Frades": "Distrito de Viseu","Penalva do Castelo": "Distrito de Viseu","Penedono": "Distrito de Viseu",
    "Resende": "Distrito de Viseu","Santa Comba Dão": "Distrito de Viseu","São João da Pesqueira": "Distrito de Viseu",
    "São Pedro do Sul": "Distrito de Viseu","Sátão": "Distrito de Viseu","Sernancelhe": "Distrito de Viseu",
    "Tabuaço": "Distrito de Viseu","Tarouca": "Distrito de Viseu","Tondela": "Distrito de Viseu",
    "Vila Nova de Paiva": "Distrito de Viseu","Viseu": "Distrito de Viseu","Vouzela": "Distrito de Viseu",

    # Região Autónoma da Madeira
    "Calheta [R.A.M.]": "Região Autónoma da Madeira","Câmara de Lobos": "Região Autónoma da Madeira","Funchal": "Região Autónoma da Madeira",
    "Machico": "Região Autónoma da Madeira","Ponta do Sol": "Região Autónoma da Madeira","Porto Moniz": "Região Autónoma da Madeira",
    "Porto Santo": "Região Autónoma da Madeira","Ribeira Brava": "Região Autónoma da Madeira","Santa Cruz": "Região Autónoma da Madeira",
    "Santana": "Região Autónoma da Madeira","São Vicente": "Região Autónoma da Madeira",

    # Região Autónoma dos Açores
    "Lagoa [R.A.A.]": "Região Autónoma dos Açores","Nordeste": "Região Autónoma dos Açores","Ponta Delgada": "Região Autónoma dos Açores",
    "Povoação": "Região Autónoma dos Açores","Ribeira Grande": "Região Autónoma dos Açores","Vila Franca do Campo": "Região Autónoma dos Açores",
    "Angra do Heroísmo": "Região Autónoma dos Açores","Praia da Vitória": "Região Autónoma dos Açores","Santa Cruz da Graciosa": "Região Autónoma dos Açores",
    "Calheta [R.A.A.]": "Região Autónoma dos Açores","Velas": "Região Autónoma dos Açores","Lajes do Pico": "Região Autónoma dos Açores",
    "Madalena": "Região Autónoma dos Açores","São Roque do Pico": "Região Autónoma dos Açores","Horta": "Região Autónoma dos Açores",
    "Lajes das Flores": "Região Autónoma dos Açores","Santa Cruz das Flores": "Região Autónoma dos Açores","Corvo": "Região Autónoma dos Açores",
    "Vila do Porto": "Região Autónoma dos Açores","Vila da Praia da Vitória": "Região Autónoma dos Açores",
}


def agregar_por_distrito(
    df: pd.DataFrame,
    coluna_territorio: str = "Territórios",
    agregacao: str = "sum",
) -> pd.DataFrame:
    """
    Recebe um DataFrame com uma coluna de municípios e colunas numéricas,
    substitui os municípios pelo distrito correspondente e agrega os valores.

    Municípios não reconhecidos pelo dicionário são ignorados (removidos do resultado)
    e listados no terminal como aviso.

    Parâmetros:
        df                — DataFrame de entrada
        coluna_territorio — nome da coluna que contém os municípios (default: "Territórios")
        agregacao         — função de agregação: "sum" (default) ou "mean"

    Retorna:
        DataFrame com uma linha por distrito e os valores agregados.
    """
    if agregacao not in ("sum", "mean"):
        raise ValueError(f"agregacao deve ser 'sum' ou 'mean', recebeu: {agregacao!r}")

    df = df.copy()

    # Mapeia cada município para o seu distrito
    df["Distrito"] = df[coluna_territorio].map(DICIONARIO_DISTRITOS)

    # Avisa sobre municípios não reconhecidos
    nao_reconhecidos = df[df["Distrito"].isna()][coluna_territorio].tolist()
    if nao_reconhecidos:
        print(f"⚠  Municípios não reconhecidos e ignorados: {nao_reconhecidos}")

    # Remove linhas sem distrito e agrupa
    df = df.dropna(subset=["Distrito"])
    colunas_numericas = [c for c in df.columns if c not in (coluna_territorio, "Distrito")]

    resultado = (
        df.groupby("Distrito")[colunas_numericas]
        .agg(agregacao)
        .reset_index()
        .rename(columns={"Distrito": coluna_territorio})
    )

    return resultado
