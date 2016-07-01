'''
facebook urlresolver plugin
Copyright (C) 2013 icharania

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import re
import urllib
from t0mm0.common.net import Net
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin

class FacebookResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "facebook"
    domains = [ "facebook.com" ]
    pattern = '(?://|\.)(facebook\.com)/.+?video_id=([0-9a-zA-Z]+)'

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        link = self.net.http_GET(web_url).content

        if link.find('Video Unavailable') >= 0:
            err_message = 'The requested video was not found.'
            raise UrlResolver.ResolverError(err_message)

        params = re.compile('"params","([\w\%\-\.\\\]+)').findall(link)[0]
        html = urllib.unquote(params.replace('\u0025', '%')).decode('utf-8')
        html = html.replace('\\', '')

        videoUrl = re.compile('(?:hd_src|sd_src)\":\"([\w\-\.\_\/\&\=\:\?]+)').findall(html)

        vUrl = ''
        vUrlsCount = len(videoUrl)
        if vUrlsCount > 0:
            q = self.get_setting('quality')
            if q == '0':
                # Highest Quality
                vUrl = videoUrl[0]
            else:
                # Standard Quality
                vUrl = videoUrl[vUrlsCount - 1]

            return vUrl

        else:
            raise UrlResolver.ResolverError('No playable video found.')

    def get_url(self, host, media_id):
        return 'https://www.facebook.com/video/embed?video_id=%s' % media_id

    def get_host_and_id(self, url):
        r = re.search(self.pattern, url)
        if r:
            return r.groups()
        else:
            return False
    
    def valid_url(self, url, host):
        return re.search(self.pattern, url) or self.name in host

    def get_settings_xml(self):
        xml = PluginSettings.get_settings_xml(self)
        xml += '<setting label="Video Quality" id="%s_quality" ' % self.__class__.__name__
        xml += 'type="enum" values="High|Standard" default="0" />\n'
        return xml