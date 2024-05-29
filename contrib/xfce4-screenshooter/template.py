pkgname = "xfce4-screenshooter"
pkgver = "1.10.6"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
# check target fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gmake",
    "help2man",
    "libtool",
    "pkgconf",
    "wayland-progs",
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
    "wayland-devel",
]
pkgdesc = "Xfce screenshot app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-screenshooter/start"
source = f"$(XFCE_SITE)/apps/xfce4-screenshooter/{'.'.join(pkgver.split('.')[:-1])}/xfce4-screenshooter-{pkgver}.tar.bz2"
sha256 = "992066cfecfb44a68681340bfd55d524d40410aac3da6ef25c6c6cb2150a5965"
# Tries to run built executable to generate manpage
options = ["!cross"]


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
