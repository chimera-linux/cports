pkgname = "wxwidgets"
pkgver = "3.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DwxBUILD_PRECOMP=OFF",
    "-DwxBUILD_TESTS=OFF",
    "-DwxBUILD_TOOLKIT=gtk3",
    "-DwxUSE_EXPAT=sys",
    "-DwxUSE_GLCANVAS_EGL=ON",
    "-DwxUSE_GTKPRINT=ON",
    "-DwxUSE_LIBJPEG=sys",
    "-DwxUSE_LIBLZMA=sys",
    "-DwxUSE_LIBPNG=sys",
    "-DwxUSE_LIBTIFF=sys",
    "-DwxUSE_OPENGL=ON",
    "-DwxUSE_PRIVATE_FONTS=ON",
    "-DwxUSE_REGEX=sys",
    "-DwxUSE_ZLIB=sys",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glu-devel",
    "gspell-devel",
    "gst-plugins-base-devel",
    "gtk+3-devel",
    "libcurl-devel",
    "libexpat-devel",
    "libjpeg-turbo-devel",
    "xz-devel",
    "libnotify-devel",
    "libsecret-devel",
    "libsm-devel",
    "libtiff-devel",
    "mesa-devel",
    "pcre2-devel",
    "sdl-devel",
    "zlib-devel",
]
pkgdesc = "WXwidgets GUI toolkit"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:wxWidgets"
url = "https://www.wxwidgets.org"
source = f"https://github.com/wxWidgets/wxWidgets/releases/download/v{pkgver}/wxWidgets-{pkgver}.tar.bz2"
sha256 = "0640e1ab716db5af2ecb7389dbef6138d7679261fbff730d23845ba838ca133e"
# fixme: int
hardening = ["!int"]
# fixme
options = ["!check", "linkundefver"]


def post_install(self):
    self.install_license("docs/licence.txt")


@subpackage("wxwidgets-devel")
def _devel(self):
    return self.default_devel()


@subpackage("wxwidgets-gtk3")
def _gtk3(self):
    self.pkgdesc = f"{pkgdesc} (GTK3 components)"
    return ["usr/lib/libwx_gtk3u*.so.*"]
