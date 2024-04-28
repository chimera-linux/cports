pkgname = "parole"
pkgver = "4.18.1"
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
    "dbus-devel",
    "dbus-glib-devel",
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "taglib-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce media player"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/parole/start"
source = f"$(XFCE_SITE)/apps/parole/{pkgver[:-2]}/parole-{pkgver}.tar.bz2"
sha256 = "0c7364a484812f69cf2b20a2323864203334cc854fd8103d1d1131814ac55a66"
# TODO
options = ["!check"]

# TODO: kinda broken on wayland


@subpackage("parole-devel")
def _devel(self):
    return self.default_devel()
