pkgname = "console-setup"
pkgver = "1.218"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "build-linux"
make_install_target = "install-linux"
hostmakedepends = [
    "gmake",
    "perl",
    "bdfresize",
    "perl-xml-parser",
    "font-unifont-bdf",
]
depends = ["kbd"]
pkgdesc = "Console font and keymap setup program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND custom:console-setup"
url = "https://salsa.debian.org/installer-team/console-setup"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "06056b8a9d163e42b53b8b43f8685bad28f7ae6ab6a2e6cb4cce67135fd4d18d"
# no tests
options = ["bootstrap", "!check"]


def pre_build(self):
    self.make.invoke("maintainer-clean")


def do_install(self):
    self.install_dir("usr/bin")
    self.install_link("usr/bin", "bin")
    self.make.install(
        [
            "prefix=" + str(self.chroot_destdir / "usr"),
            "etcdir=" + str(self.chroot_destdir / "etc"),
        ]
    )
    self.rm(self.destdir / "bin")


def post_install(self):
    self.install_license("debian/copyright")


@subpackage("console-setup-xkb")
def _xkb(self):
    self.pkgdesc = f"{pkgdesc} (optional XKB keymap support)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "xkeyboard-config", "perl"]
    self.install_if = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "xkeyboard-config",
        "perl",
    ]
    return ["usr/bin/ckbcomp"]
