pkgname = "xfce4-screenshooter"
pkgver = "1.10.5"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "help2man",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "exo-devel",
    "glib-devel",
    "gtk+3-devel",
    "libsoup-devel",
    "libx11-devel",
    "libxext-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfixes-devel",
    "libxi-devel",
    "libxml2-devel",
    "pango-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce screenshot app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-screenshooter/start"
source = f"$(XFCE_SITE)/apps/xfce4-screenshooter/{'.'.join(pkgver.split('.')[:-1])}/xfce4-screenshooter-{pkgver}.tar.bz2"
sha256 = "fa711f2a6a5517f575f2e129fe48c2678e836bd4ede5433075f3076d7670621c"
# TODO
options = ["!check"]


@subpackage("xfce4-screenshooter-imgur")
def _imgur(self):
    self.pkgdesc = f"{pkgdesc} (Imgur upload support)"
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "curl",
        "jq",
        "xclip",
        "zenity",
    ]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/libexec/xfce4/screenshooter/scripts/imgur-upload.sh"]
