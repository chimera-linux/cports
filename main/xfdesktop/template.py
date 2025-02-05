pkgname = "xfdesktop"
pkgver = "4.20.0"
pkgrel = 1
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfdesktop/start"
source = f"$(XFCE_SITE)/xfce/xfdesktop/{pkgver[:-2]}/xfdesktop-{pkgver}.tar.bz2"
sha256 = "227041ba80c7f3eb9c99dec817f1132b35d8aec7a4335703f61ba1735cd65632"


@subpackage("xfdesktop-backgrounds")
def _(self):
    self.pkgdesc = "Backgrounds for the Xfce desktop"
    self.install_if = [self.parent]
    self.license = "CC-BY-SA-4.0"
    # transitional
    self.provides = [self.with_pkgver("xfce4-backgrounds")]

    return ["usr/share/backgrounds"]
