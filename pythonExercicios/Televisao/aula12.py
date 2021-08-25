import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))
    print(f'{response.status_code}')
    print(f'{response.json()}')
    dados_cep = response.json()
    print(f'{dados_cep["logradouro"]}')
    print(f'{dados_cep["complemento"]}')
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/' .format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return  response.text

if __name__ == '__main__':

    response = retorna_response('http://www.uol.com.br')
    print(f'{response}')
    #retorna_dados_cep('22041001')
    #dados_pokemon = retorna_dados_pokemon('charmander')
    #print(f'{dados_pokemon["sprites"]["front_shiny"]}')
