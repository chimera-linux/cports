pkgname = "lshw"
pkgver = "02.20"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "all",
    "gui",
    f"VERSION={pkgver}",
    "NO_VERSION_CHECK=1",
    "ZLIB=1",
]
make_install_args = [
    "install",
    "install-gui",
    f"VERSION={pkgver}",
    "NO_VERSION_CHECK=1",
    "ZLIB=1",
]
make_use_env = True
hostmakedepends = ["gettext", "pkgconf"]
makedepends = [
    "gtk+3-devel",
    "linux-headers",
    "zlib-ng-compat-devel",
]
pkgdesc = "Hardware lister"
license = "GPL-2.0-only"
url = "https://ezix.org/project/wiki/HardwareLiSter"
source = f"https://www.ezix.org/software/files/lshw-B.{pkgver}.tar.gz"
sha256 = "06d9cf122422220e5dc94e8ea5b01816a69bb6b59368f63d7f21fff31fc6922a"
# no tests available
options = ["!check"]


@subpackage("lshw-gtk")
def _(self):
    self.subdesc = "GTK UI"
    self.depends = [
        self.parent,
    ]
    return [
        "cmd:gtk-lshw",
        "usr/share/lshw/artwork",
        "usr/share/lshw/ui",
        "usr/share/applications",
        "usr/share/metainfo",
        "usr/share/doc/lshw",
        "usr/lib/pam.d",
    ]
