from sorl.thumbnail.base import ThumbnailBackend, EXTENSIONS
from sorl.thumbnail.conf import settings
from sorl.thumbnail.helpers import tokey, serialize


class MyThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        """
        Computes the destination filename.
        """
        key = tokey(source.key, geometry_string, serialize(options))
        path = '%s/%s/%s' % (key[:2], key[2:4], key)
        print(path)
        return '%s%s.%s' % (settings.THUMBNAIL_PREFIX, path, EXTENSIONS[options['format']])