pkgname = "xfdesktop"
pkgver = "4.20.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-default-backdrop-filename=/usr/share/backgrounds/chimera/bg-l.svg"
]
hostmakedepends = [
    "automake",
    "gettext",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "cairo-devel",
    "exo-devel",
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libnotify-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfce4windowing-devel",
    "libyaml-devel",
    "thunar-devel",
    "xfconf-devel",
]
depends = ["chimera-artwork"]
pkgdesc = "Xfce desktop manager"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfdesktop/start"
source = f"$(XFCE_SITE)/xfce/xfdesktop/{pkgver[:-2]}/xfdesktop-{pkgver}.tar.bz2"
sha256 = "acccde849265bbf4093925ba847977b7abf70bb2977e4f78216570e887c157b8"
# FIXME lintpixmaps
options = ["!lintpixmaps"]


@subpackage("xfdesktop-backgrounds")
def _(self):
    self.pkgdesc = "Backgrounds for the Xfce desktop"
    self.install_if = [self.parent]
    self.license = "CC-BY-SA-4.0"
    # transitional
    self.provides = [self.with_pkgver("xfce4-backgrounds")]

    return ["usr/share/backgrounds"]
