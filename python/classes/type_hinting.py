#!/usr/bin/env python3 
from pathlib import Path
import hashlib
import os 
"""
EXAMPLES:
    Class vars and class sate (usercount is shared between all users and the class)
    Usage of __str__
    Usage of .format
    Looping through a list of cusotm objects
    Type hinting :) 
"""

class User:
    """This is just some example of using typehinting along with class vars here."""
    usercount: int = 0
    password: str = ''
    _userids: list = []
    userlist: list = []
    homedir: Path = Path('/home/users/')

    def __init__(self, username: str, uid: int, password: str = None) -> None:
        self.uid = uid
        self.username = username 
        self.home = Path(self.homedir / self.username)
        if isinstance(password, str): 
            salt = os.urandom(32)
            pw = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
            hashed_password = {'salt':salt,  'pw': pw}
            self.password = hashed_password
        if self.uid in User._userids: 
            raise ValueError("UID {} already exists!".format(self.uid))
        elif self.uid < 500 and self.username != 'root': 
            raise ValueError("UIDs below 500 are system reserved!".format(self.uid))
        else:
            User._userids.append(uid) 
        User.usercount += 1 
        User.userlist.append(self)

    def __str__(self) -> str:
        return "{}:{}:{}:{}:{}".format(self.username, self.uid, self.password, self.home, self.usercount)



admin = User('root', 0, 'toor')
p_halpert = User('p.halpert', 1000, 'mmmjim')
j_halpert = User('j.halpert', 1001, 'philly')
d_schrute = User('d.schrute', 1040, 'beets')

for user in User.userlist:
    print(user)

print(User.usercount)
