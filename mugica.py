import dropbox

app_key = 'a7a2uzsk54m2rvw'
app_secret = 'hx2zhh7gweo1qlv'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print('1. Go to: ' + authorize_url)
print('2. Click "Allow" (you might have to log in first)')
print('3. Copy the authorization code.')
code = input("Enter the authorization code here: ").strip()

access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)

folder_metadata = client.metadata('/mugica')

remotefiles = []
for content in folder_metadata['contents']  :
    remotefiles.append(content['path'])

for tarfile in remotefiles :
    f, metadata = client.get_file_and_metadata(tarfile)
    out = open(tarfile, 'wb')
    out.write(f.read())
    out.close()
