class Keys:

    def __init__(self, data, url):
        self.d = data
        self.url = url

    def title(self):
        try:
            title = self.d['contents'][0]['title']
        except KeyError:
            title = ' '
            print('Missing Title key for: ', self.url)
        return title

    def crid(self):
        try:
            crid = self.d['contents'][0]['alternativeIdentifiers']['crid']
        except KeyError:
            crid = ' '
            print('Missing CRID key for: ', self.url)
        return crid

    def parentId(self):
        try:
            parentId = self.d['contents'][0]['alternativeIdentifiers']['parentId']
        except KeyError:
            parentId = ' '
           # print('Missing parentId key for: ', self.url)
        return parentId

    def rootId(self):
        try:
            rootId = self.d['contents'][0]['alternativeIdentifiers']['rootId']
        except KeyError:
            rootId = ' '
            print('Missing rootId key for: ', self.url)
        return rootId

    def mediaGroupId(self):
        try:
            mediaGroupId = self.d['contents'][0]['alternativeIdentifiers']['mediaGroupId']
        except KeyError:
            mediaGroupId = ' '
            print('\n Missing mediaGroupId key for: ', self.url)
        return mediaGroupId

    def currentProductIds(self):
        try:
            cProductIds = self.d['contents'][0]['custom']['currentProductIds']
        except KeyError:
            cProductIds = ' '
            print('Missing currentProductIds key for: ', self.url)
        return cProductIds

    def availabilityEndDate(self):
        try:
            availabilityEndDate = self.d["contents"][0]["availabilityEndAt"]
        except KeyError:
            availabilityEndDate = ' '
            print('Missing availailityEndDAt key for: ', self.url)
        return availabilityEndDate

