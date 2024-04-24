pkgname = "tumbler"
pkgver = "4.18.2"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
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
    "libgsf-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libpoppler-devel",
    "libxfce4util-devel",
    # TODO: libopenraw, libgepub, cover-thumbnailer
]
pkgdesc = "Xfce implementation of the thumbnail management D-Bus spec"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/tumbler/start"
source = f"$(XFCE_SITE)/xfce/tumbler/{pkgver[:-2]}/tumbler-{pkgver}.tar.bz2"
sha256 = "b530eec635eac7f898c0d8d3a3ff79d76a145d3bed3e786d54b1ec058132be7a"
