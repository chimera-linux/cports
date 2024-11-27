pkgname = "wxwidgets"
pkgver = "3.2.6"
pkgrel = 1
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
    "-DOPENGL_opengl_LIBRARY=/usr/lib/libGL.so",
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
    "zlib-ng-compat-devel",
]
pkgdesc = "WXwidgets GUI toolkit"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "custom:wxWidgets"
url = "https://www.wxwidgets.org"
source = f"https://github.com/wxWidgets/wxWidgets/releases/download/v{pkgver}/wxWidgets-{pkgver}.tar.bz2"
sha256 = "939e5b77ddc5b6092d1d7d29491fe67010a2433cf9b9c0d841ee4d04acb9dce7"
# fixme: int
hardening = ["!int"]
# fixme
options = ["!check", "linkundefver"]


def post_install(self):
    self.install_license("docs/licence.txt")
    self.install_file("wxwin.m4", "usr/share/aclocal")


@subpackage("wxwidgets-devel")
def _(self):
    return self.default_devel()


@subpackage("wxwidgets-gtk3")
def _(self):
    self.subdesc = "GTK3 components"
    return ["usr/lib/libwx_gtk3u*.so.*"]
