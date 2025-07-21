pkgname = "mlt"
pkgver = "7.32.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # needs an ancient abandoned ruby kwalify
    "-DBUILD_TESTING=OFF",
    "-DBUILD_TESTS_WITH_QT6=OFF",
    "-DCLANG_FORMAT=OFF",
    "-DMOD_GLAXNIMATE_QT6=ON",
    "-DMOD_OPENCV=ON",
    "-DMOD_QT6=ON",
    "-DMOD_QT=OFF",
    "-DSWIG_PYTHON=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "swig",
]
makedepends = [
    "ffmpeg-devel",
    "fftw-devel",
    "fontconfig-devel",
    "frei0r-devel",
    "gdk-pixbuf-devel",
    "ladspa-sdk",
    "libarchive-devel",
    "libebur128-devel",
    "libexif-devel",
    "libpulse-devel",
    "libsamplerate-devel",
    "libvidstab-devel",
    "libvorbis-devel",
    "libxml2-devel",
    "mesa-devel",
    "opencv-devel",
    "pipewire-jack-devel",
    "python-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "rubberband-devel",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Multimedia framework for video editors"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later"
url = "https://www.mltframework.org"
source = f"https://github.com/mltframework/mlt/releases/download/v{pkgver}/mlt-{pkgver}.tar.gz"
sha256 = "1ca5aadfe27995c879b9253b3a48d1dcc3b1247ea0b5620b087d58f5521be028"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# suboverflow in find_first_pts for certain files
hardening = ["!int"]
options = ["linkundefver"]


@subpackage("mlt-devel")
def _(self):
    return self.default_devel()


@subpackage("mlt-python")
def _(self):
    self.subdesc = "python module"
    self.depends += ["python"]
    self.renames = ["python-mlt"]

    return ["usr/lib/python*"]
