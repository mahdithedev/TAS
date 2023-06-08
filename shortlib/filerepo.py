from shortlib.repository import Repository

# Implmentation of Repository with for the file-system

class FileRepo(Repository):

    def __init__(self , address) -> None:
        super().__init__(address)
        self.file = open(address , "a+")

    def save(self , url, value):
        self.file.write(f"{url} === {value}\n")

    def get(self , iurl):
        file_content = ""
        BUFFER_SIZE = 4056
        while True:
            new = self.file.read(BUFFER_SIZE)
            if new == None:
                break
            file_content += new
        urls = map(lambda url_entry: url_entry.split(" === ") , file_content.split("\n"))

        for url in urls:
            if url == iurl:
                return (url[0] , url[1] , -1) 

    def delete(self, url):
        return super().delete(url)
    
    def click(self):
        return super().click()

    def __del__(self):
        self.file.close()

    