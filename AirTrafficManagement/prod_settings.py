import dj_database_url
from AirTrafficManagement.settings import *

DEBUG=False
TEMPLATE_DEBUG=False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY='+7)7=@*14(jz#4fyf$f!29d()%=&m_t@16-yz&6xxum=lol216'

ALLOWED_HOSTS=['projecthamet.herokuapp.com']