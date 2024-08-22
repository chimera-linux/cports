pkgname = "xfdesktop"
pkgver = "4.18.1"
pkgrel = 0
build_style = "gnu_configure"
# check target fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "cairo-devel",
    "exo-devel",
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "libnotify-devel",
    "libwnck-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "thunar-devel",
    "xfconf-devel",
]
# We patch the default wallpaper to Chimera's, see
# patches/default-to-chimera-wallpaper.patch
depends = ["chimera-artwork"]
pkgdesc = "Xfce desktop manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfdesktop/start"
source = f"$(XFCE_SITE)/xfce/xfdesktop/{pkgver[:-2]}/xfdesktop-{pkgver}.tar.bz2"
sha256 = "ef9268190c25877e22a9ff5aa31cc8ede120239cb0dfca080c174e7eed4ff756"


@subpackage("xfce4-backgrounds")
def _(self):
    self.pkgdesc = "Backgrounds for the Xfce desktop"
    self.install_if = [self.parent]
    # TODO: https://gitlab.xfce.org/xfce/xfdesktop/-/issues/298
    self.license = "CC-BY-SA-4.0"

    return ["usr/share/backgrounds"]
