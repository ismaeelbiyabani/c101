import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'kJ9zNEA-yK4AAAAAAAAAAYmYWrsqbKqrw08GUHn2IcN6lZ_55X1slaxvYPTaS-LG'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")
main()