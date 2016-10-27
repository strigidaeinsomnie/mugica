import dropbox
import glob
import os

#----------------------------------

access_token = 'k2Al7W0a9SAAAAAAAAAALKqbdiL0Vr73rPreN4Pl760unofPADYeX2-lj2A5ei5S'

tardir_drop = '/mugicaData'
tardir_lake = 'mugicaData'

#----------------------------------

def drop_authorize(access_token) :
    client = dropbox.client.DropboxClient(access_token)
    return client

def drop_list(tardir_drop) :
    client = drop_authorize(access_token)
    folder_metadata = client.metadata(tardir_drop)

    drop_files = []
    for content in folder_metadata['contents']  :
        drop_path = content['path']
        drop_name = drop_path[drop_path.rfind('/') + 1 :]
        drop_files.append(drop_name)

    return drop_files


def lake_list(tardir_lake) :
    lake_files = glob.glob('{0}/*'.format(tardir_lake))
    return lake_files


def drop_down(tarfile) :
    client = drop_authorize(access_token)
    f, metadata = client.get_file_and_metadata(tarfile)

    lake_name = tarfile.replace('/', '', 1)
    out = open(lake_name, 'wb')
    out.write(f.read())
    out.close()


def drop_is_lake(tardir_drop, tardir_lake) :
    drop_files = drop_list(tardir_drop)
    lake_files = lake_list(tardir_lake)

    set_drop_files = set(drop_files)
    set_lake_files = set(lake_files)

    for lake in set_lake_files :
        if lake not in set_drop_files :
            os.system('rm {0}'.format(lake))

    for drop in set_drop_files :
        if drop not in set_lake_files :
            drop_down('{0}/{1}'.format(tardir_drop, drop))


def lake_play(tardir_lake) :
    lake_list_play = lake_list(tardir_lake)

    for lake_play in lake_list_play :
        os.system('mpg123  {0}'.format(lake_play))

#-----------------------------------



web = os.system('ping -c 5 google.com')

if web is 0 :
    drop_authorize(access_token)
    drop_is_lake(tardir_drop, tardir_lake)

lake_play(tardir_lake)
