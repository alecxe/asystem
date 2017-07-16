from sorl.thumbnail.base import ThumbnailBackend


DIR_MAP = {
    '30x30': 'small',
    '100x100': 'medium'
}

class MyThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        """
        Computes the destination filename.
        """
        dir_name = DIR_MAP.get(geometry_string, '')
        path = dir_name + "/" + dir_name + "_" + source.name
        return path
