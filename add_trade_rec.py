import re
import sqlite3
import sys

from ab_util import log, get_spotify_conn, create_connection
from datetime import datetime
from pprint import pprint

TRADELISTS = ['5X8lN5fZSrLnXzFtDEUwb9', '34fjygZUlRVjTOlK36VxAn']
CURATORLISTS = ['1Bfsx8NYN4psWxBdXHVW91', '2hyorCyLFfk5I9hwqEFnpj']
TODAY = datetime.now().strftime("%Y-%m-%d 00:00:00.000000")


def add_rec(spotify_uri, db_conn, type='trade'):
    insert_stmt = 'INSERT INTO albums (spotify_uri, add_date, json_text)' \
                  + ' VALUES(?,?,?)'
    update_stmt = 'UPDATE albums SET {}_rec = 1 where spotify_uri = "{}"'
    match_string = re.compile('(spotify:album:.*)')
    if match_string.match(spotify_uri) is None:
        message = 'Malformed Spotify URI: {}'.format(spotify_uri)
        log(message)
        raise Exception(message)
    try:
        db_conn.execute(insert_stmt, (spotify_uri, TODAY, ''))
    except sqlite3.IntegrityError:
        log('Good news, it is already in the database!')
        pass

    try:
        db_conn.execute(update_stmt.format(type, spotify_uri))
    except sqlite3.IntegrityError:
        # Ignore duplicates
        pass

    db_conn.commit()
    pass


def add_playlist_recs(playlist_id, sp_conn, db_conn, type='trade'):
    plylst_json = sp_conn.user_playlist(playlist_id)
    for track in plylst_json[u'tracks'][u'items']:
        add_rec(track[u'track'][u'album'][u'uri'], db_conn, type)


if __name__ == '__main__':
    db_conn = create_connection()
    sp_conn = get_spotify_conn()
    if len(sys.argv) > 1:
        for rec in sys.argv[1:]:
            add_rec(rec, db_conn)
    else:
        for playlist in PLAYLISTS:
            add_playlist_recs(playlist, sp_conn, db_conn)
    db_conn.close()
