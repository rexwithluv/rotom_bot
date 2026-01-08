import httpx
from bs4 import BeautifulSoup, Tag


def get_nombre_medico(inputs: list[Tag]) -> str:
    for i in inputs:
        if i.get("name") == "nomemedico":
            return i.get("value")

    return "NOMBRE NO ENCONTRADO"


def get_estado_cupo(inputs: list[Tag]) -> str:
    for i in inputs:
        if i.get("name") == "telfurx" and "text-align:left" in i.get("style"):
            return i.get("value")

    return "NO SE HA PODIDO OBTENER EL ESTADO DEL CUPO"


async def check_cupo_medico_sergas() -> str:
    url: str = "https://tsinternet.sergas.es/TSInternet/ConsultaHorariosMedicos.servlet?CUPO=36502514"

    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)

        soup: BeautifulSoup = BeautifulSoup(r.text, "lxml")

        inputs: list[Tag] = soup.find_all("input")

        nombre: str = get_nombre_medico(inputs)
        cupo: str = get_estado_cupo(inputs)

        return f"Estado del cupo de {nombre}: {cupo}"
    except Exception as e:
        return f"Error tratando de obtener el cupo: {e}"
