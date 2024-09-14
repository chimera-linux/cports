pkgname = "xfce4-screenshooter"
pkgver = "1.11.1"
pkgrel = 0
build_style = "gnu_configure"
# check target fails without this
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "help2man",
    "libtool",
    "pkgconf",
    "wayland-progs",
    "xfce4-dev-tools",
]
makedepends = [
    "exo-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxext-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfixes-devel",
    "libxi-devel",
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
sha256 = "d94c4a37ac9b26f6d73214bdc254624a4ede4e111bee8d34e689f8f04c37d34d"
# Tries to run built executable to generate manpage
options = ["!cross"]


@subpackage("xfce4-screenshooter-imgur")
def _(self):
    self.subdesc = "Imgur upload support"
    self.depends = [
        self.parent,
        "curl",
        "jq",
        "xclip",
        "zenity",
    ]
    self.install_if = [self.parent]

    return ["usr/libexec/xfce4/screenshooter/scripts/imgur-upload.sh"]
