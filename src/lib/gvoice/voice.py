from util import *
import settings
import os

class Voice(object):
    """
    Main voice instance for interacting with the Google Voice service
    Handles login/logout and most of the baser HTTP methods
    """
    def __init__(self):
        install_opener(build_opener(HTTPCookieProcessor(CookieJar())))

        for name in settings.FEEDS:
            setattr(self, name, self.__get_xml_page(name))

    ######################
    # Some handy methods
    ######################
    def special(self):
        """
        Returns special identifier for your session (if logged in)
        """
        if hasattr(self, '_special') and getattr(self, '_special'):
            return self._special
        try:
            try:
                regex = bytes("('_rnr_se':) '(.+)'", 'utf8')
            except TypeError:
                regex = bytes("('_rnr_se':) '(.+)'")
        except NameError:
            regex = r"('_rnr_se':) '(.+)'"
        try:
            sp = re.search(regex, urlopen(settings.INBOX).read()).group(2)
        except AttributeError:
            sp = None
        self._special = sp
        return sp
    special = property(special)

    def login(self, email, passwd):
        """
        Login to the service using your Google Voice account
        Credentials will be propmpted for if not given as args or in the ``~/.gvoice`` config file
        """
        if hasattr(self, '_special') and getattr(self, '_special'):
            return self

        content = self.__do_page('login').read()
        # holy hackjob
        galx = re.search(r"name=\"GALX\"\s+value=\"(.+)\"", content).group(1)
        self.__do_page('login', {'Email': email, 'Passwd': passwd, 'GALX': galx})

        del email, passwd

        try:
            assert self.special
        except (AssertionError, AttributeError):
            raise LoginError

        return self

    def logout(self):
        """
        Logs out an instance and makes sure it does not still have a session
        """
        self.__do_page('logout')
        del self._special
        assert self.special == None
        return self

    def send_sms(self, phoneNumber, text):
        """
        Send an SMS message to a given ``phoneNumber`` with the given ``text`` message
        """
        self.__validate_special_page('sms', {'phoneNumber': phoneNumber, 'text': text})

    def search(self, query):
        """
        Search your Google Voice Account history for calls, voicemails, and sms
        Returns ``Folder`` instance containting matching messages
        """
        return self.__get_xml_page('search', data='?q=%s' % quote(query))()

    ######################
    # Helper methods
    ######################

    def __do_page(self, page, data=None, headers={}):
        """
        Loads a page out of the settings and pass it on to urllib Request
        """
        page = page.upper()
        if isinstance(data, dict) or isinstance(data, tuple):
            data = urlencode(data)
        headers.update({'User-Agent': 'PyGoogleVoice/0.5'})
        if page in ('DOWNLOAD','XML_SEARCH'):
            return urlopen(Request(getattr(settings, page) + data, None, headers))
        if data:
            headers.update({'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'})
        return urlopen(Request(getattr(settings, page), data, headers))

    def __validate_special_page(self, page, data={}, **kwargs):
        """
        Validates a given special page for an 'ok' response
        """
        data.update(kwargs)
        load_and_validate(self.__do_special_page(page, data))

    _Phone__validate_special_page = __validate_special_page

    def __do_special_page(self, page, data=None, headers={}):
        """
        Add self.special to request data
        """
        assert self.special, 'You must login before using this page'
        if isinstance(data, tuple):
            data += ('_rnr_se', self.special)
        elif isinstance(data, dict):
            data.update({'_rnr_se': self.special})
        return self.__do_page(page, data, headers)

    _Phone__do_special_page = __do_special_page

    def __get_xml_page(self, page, data=None, headers={}):
        """
        Return XMLParser instance generated from given page
        """
        return XMLParser(self, page, lambda: self.__do_special_page('XML_%s' % page.upper(), data, headers).read())

    def __messages_post(self, page, *msgs, **kwargs):
        """
        Performs message operations, eg deleting,staring,moving
        """
        data = kwargs.items()
        for msg in msgs:
            if isinstance(msg, Message):
                msg = msg.id
            assert is_sha1(msg), 'Message id not a SHA1 hash'
            data += (('messages',msg),)
        return self.__do_special_page(page, dict(data))

    _Message__messages_post = __messages_post