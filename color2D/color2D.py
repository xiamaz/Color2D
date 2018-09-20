import re
import pkg_resources

import imageio


COLORMAPS = {
    "bremm": "data/bremm.png",
    "cubediagonal": "data/cubediagonal.png",
    "schumann": "data/schumann.png",
    "steiger": "data/steiger.png",
    "teulingfig2": "data/teulingfig2.png",
    "ziegler": "data/ziegler.png",
}


class Color2D:
    """Get color values for 2 dimensional coordinates.

    More info: http://dominikjaeckle.com/projects/color2d/
    """
    def __init__(self, map_name="bremm"):
        """
        Args:
            map_name: Name of colormap to be used.
        """
        self._data = imageio.imread(
            pkg_resources.resource_string(__name__, COLORMAPS[map_name]))

    @staticmethod
    def list_colormaps():
        """Get a list of all available colormap names."""
        return list(COLORMAPS.keys())

    def get_scaled(self, x, y):
        """Insert a number between 0 and 1."""
        assert 0 <= x <= 1 and 0 <= y <= 1, f"{x}, {y} have to be between 0 and 1"
        return self._data[int(x * self._data.shape[0] + 0.5), int(y * self._data.shape[1] + 0.5)]

    def __getitem__(self, key):
        assert isinstance(key, tuple), f"{key} has to be a tuple."
        return self.get_scaled(*key)


if __name__ == "__main__":
    c2d = Color2D("bremm")

    test = c2d[0.5, 0.4]
    print(test)
