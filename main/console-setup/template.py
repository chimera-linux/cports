pkgname = "console-setup"
pkgver = "1.232"
pkgrel = 1
build_style = "makefile"
make_build_target = "build-linux"
make_install_target = "install-linux"
hostmakedepends = [
    "bdfresize",
    "font-unifont-bdf",
    "fonts-dejavu-otf",
    "mandoc",
    "otf2bdf",
    "perl",
    "perl-xml-parser",
]
depends = ["kbd"]
pkgdesc = "Console font and keymap setup program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND custom:console-setup"
url = "https://salsa.debian.org/installer-team/console-setup"
source = f"{url}/-/archive/{pkgver}/console-setup-{pkgver}.tar.gz"
sha256 = "3b5b8a672853489d2706cc8be4ed74a28ff722743191c1e9587e1e57975fd5b8"
# no tests
options = ["bootstrap", "!check"]


def pre_build(self):
    self.make.invoke("maintainer-clean")


def install(self):
    self.install_dir("usr/bin")
    self.install_link("bin", "usr/bin")
    self.make.install(
        [
            "prefix=" + str(self.chroot_destdir / "usr"),
            "etcdir=" + str(self.chroot_destdir / "etc"),
        ]
    )
    self.uninstall("bin")


def post_install(self):
    self.install_license("debian/copyright")
    self.install_file(self.files_path / "dinit-console", "usr/lib", mode=0o755)


@subpackage("console-setup-xkb")
def _(self):
    self.subdesc = "optional XKB keymap support"
    self.depends = [self.parent, "xkeyboard-config", "perl"]
    self.install_if = [
        self.parent,
        "xkeyboard-config",
        "perl",
    ]
    return ["usr/bin/ckbcomp"]
