from objetos.SpiderRouter import SpiderRouter


class SpiderRouterArpList:

    @staticmethod
    def main():
        ip = 'http://192.168.1.1/'
        action = 'cgi?5'
        cookie_type = 'Authorization'
        cookie_body = 'Basic YWRtaW46YWRtaW4='
        port = '80'
        arp_entry = b'[ARP_ENTRY#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n'
        spider = SpiderRouter(ip, action, cookie_type, cookie_body, port, '/')
        response = spider.connect(arp_entry, 'POST')

        if response is True:
            [print(x) for x in spider.format_data()]


if __name__ == '__main__':
    SpiderRouterArpList.main()
