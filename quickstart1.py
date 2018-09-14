import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy


insta_username = 'saimah._'
insta_password = 'emraan12'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-0.6,
				  delimit_by_numbers=True,
				   max_followers=9000,
				    max_following=4000,
				     min_followers=100,
				      min_following=50)
    
    # actions

    session.follow_user_followers(['classypeepsofpakistan','classy__people','saeeinsta','shoutout.official.pk', 'islamabad_styleicon', 'isb_elite_class','elitepakistanis19','pakistan_style.icons','hearthrob_pakistanis','pakistanis_beauty'], amount=600, randomize=True, sleep_delay=120)


except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
