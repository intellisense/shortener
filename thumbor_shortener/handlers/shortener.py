# -*- coding: utf-8 -*-

from thumbor.handlers.imaging import ImagingHandler
from thumbor.url import Url

from thumbor_shortener.shortener import Shortener
from thumbor_shortener.context import CommunityContext


class UrlShortenerHandler(ImagingHandler):

    @class_method
    def regex():
        pass

    def get(self):

        context = CommunityContext(self.context)

        shortener = Shortener(context)

        # Get the url from the shortener and parse the values.
        url = shortener.get(self.request.path)

        if not url:
            # TODO Throw a 404
            pass

        options = Url.parse_decrypted(url)

        # Call the original ImageHandler.get method to serve the image.
        return super(UrlShortenerHandler, self).get(**options)
