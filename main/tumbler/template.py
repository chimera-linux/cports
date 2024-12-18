pkgname = "tumbler"
pkgver = "4.18.2"
pkgrel = 4
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "freetype-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gst-plugins-base-devel",
    "curl-devel",
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/tumbler/start"
source = f"$(XFCE_SITE)/xfce/tumbler/{pkgver[:-2]}/tumbler-{pkgver}.tar.bz2"
sha256 = "b530eec635eac7f898c0d8d3a3ff79d76a145d3bed3e786d54b1ec058132be7a"


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("tumbler-devel")
def _(self):
    return self.default_devel()
