from urllib import request
from urllib.error import HTTPError # Http Code Errors
from http.cookiejar import CookieJar, Cookie

class SpiderRouter():

    """ Obtener Tabla ARP, metodo POST, creacion previa de Cookie """

    you_know = { 
        'AA:AA:AA:AA:AA:AA': 'PC',
        'BB:BB:BB:BB:BB:BB': 'Phone',
    }
    response_data = None
    
    def __init__(self, url, url_extra, cookie_name, cookie_value, port, path):
        self.url = url
        self.url_extra = url_extra
        self.url_full = url + url_extra
        self.host = url.split('/')[2]
        self.cookie_name = cookie_name
        self.cookie_value = cookie_value
        self.port = port
        self.path = path

    def connect(self, body_request, method):
        try:
            headers = {'User-agent': 'Mozilla/5.0', 'Content-Type': 'text/plain',
                   'Referer': self.url}
            handle_cookie = request.HTTPCookieProcessor(self.create_cookie())
            handle_opener = request.build_opener(handle_cookie)
            request_data = request.Request(self.url_full, body_request, headers, method=method)
            self.response_data = handle_opener.open(request_data)
            return True
        except HTTPError as error:
            print(error)
            return False
        
    def create_cookie(self):
        """ Cookie de autorizacion de logueo """
        cookie_jar = CookieJar()
        cookie = Cookie(0, self.cookie_name, self.cookie_value, self.port, None,
                        self.host, None, None, self.path, None, False, None,
                        None, '', '', None, True)
        cookie_jar.set_cookie(cookie)
        return cookie_jar

    def format_data(self):
        """ Dar formato a la lista ARP obtenida """
        array_data = self.response_data.read().decode('utf-8').split('\n')
        index = 0
        columnxrow = 3 
        row = []
        resp = []
        for item in array_data:
            if index == 2:
                row.append(self.number_to_ip(item))
            elif index == 3:
                row.append(item)
                row.append(self.mac_discovered(item))

            if len(row) >= 2:
                resp.append(row)
                row = []
                index = 0
            else:
                index += 1
            
        return resp

    def number_to_ip(self, number):
        """ Conversion numero a IP """
        get_number = int(number.split('=')[1])
        part1 = get_number >> 24   # 0xFF = 255 
        part2 = get_number >> 16 & 0xFF
        part3 = get_number >> 8 & 0xFF
        part4 = get_number & 0xFF
        return 'ip={}.{}.{}.{}'.format(part1, part2, part3, part4)

    def mac_discovered(self, mac):
        """ Encontrar MAC """
        get_mac = mac.split('=')[1]
        try:
            return self.you_know[get_mac]
        except:
            return '----------¿Quien te conoce?'

        
spider = SpiderRouter('http://192.168.1.1/', 'cgi?5', 'Authorization',
                      'Basic YWRtaW46YWRtaW4=', '80', '/')
response = spider.connect(b'[ARP_ENTRY#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n', 'POST')

if response is True:
    [print(x) for x in spider.format_data()]
