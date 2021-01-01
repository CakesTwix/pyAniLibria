import aiohttp
import requests

from pyAniLibria.TitleModel import Title


class AnilibriaApiV2:
    """
    Class for getTitle based API from AniLibria.tv
    """
    url = 'https://api.anilibria.tv/v2/'

    def __init__(self, proxies=None):
        self.__proxy = proxies
        self.__s = requests.Session()
        self.__s.proxies = proxies

    def getTitle(self, id: int):
        answer = self.__s.get(self.url + 'getTitle', params=dict({'id': id})).json()
        if 'error' in answer:
            raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')
        return Title(**answer)

    def getTitles(self, **param):
        if 'id_list' in param:
            param['id_list'] = ', '.join(param['id_list'])
        answer = self.__s.get(self.url + 'getTitles', params=param).json()
        if 'error' in answer:
            raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')
        return [Title(**line) for line in answer]

    def getUpdates(self, **param):
        answer = self.__s.get(self.url + 'getUpdates', params=param).json()
        if 'error' in answer:
            raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')
        return [Title(**line) for line in answer]

    def getChanges(self, **param):
        answer = self.__s.get(self.url + 'getChanges', params=param).json()
        if 'error' in answer:
            raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')
        return [Title(**line) for line in answer]

    def getRandomTitle(self, **param):
        answer = self.__s.get(self.url + 'getRandomTitle', params=param).json()
        if 'error' in answer:
            raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')
        return Title(**answer)

    def searchTitles(self, **param):
        answer = self.__s.get(self.url + 'searchTitles', params=param).json()
        if 'error' in answer:
            raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')
        return [Title(**line) for line in answer]

    async def getTitleAsync(self, id: int) -> Title:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + 'getTitle', params=dict({'id': id}), proxy=self.__proxy) as get:
                answer = await get.json()
                await session.close()
                if 'error' in answer:
                    raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')

                return Title(**answer)

    async def getRandomTitleAsync(self, **param) -> Title:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + 'getRandomTitle', params=param, proxy=self.__proxy) as get:
                answer = await get.json()
                await session.close()
                if 'error' in answer:
                    raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')

                return Title(**answer)