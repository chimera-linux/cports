pkgname = "tumbler"
pkgver = "4.20.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "curl-devel",
    "freetype-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gst-plugins-base-devel",
    "libgsf-devel",
    "libjpeg-turbo-devel",
    "libopenraw-devel",
    "libpng-devel",
    "libxfce4util-devel",
    "poppler-devel",
    # TODO: libgepub, if/when it moves off libsoup2
]
depends = ["cover-thumbnailer"]
pkgdesc = "Xfce implementation of the thumbnail management D-Bus spec"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/tumbler/start"
source = f"$(XFCE_SITE)/xfce/tumbler/{pkgver[:-2]}/tumbler-{pkgver}.tar.bz2"
sha256 = "87b90df8f30144a292d70889e710c8619d8b8803f0e1db3280a4293367a42eae"


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("tumbler-devel")
def _(self):
    return self.default_devel()
