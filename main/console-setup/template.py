pkgname = "console-setup"
pkgver = "1.210"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "build-linux"
make_install_target = "install-linux"
hostmakedepends = ["gmake", "perl", "bdfresize", "perl-xml-parser"]
depends = ["perl", "kbd", "xkeyboard-config"]
pkgdesc = "Console font and keymap setup program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND custom:console-setup"
url = "https://salsa.debian.org/installer-team/console-setup"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6df6c5727efbeb2ba77682236d75210361d7184044aa71609b0698f178686bbb"
# no tests
options = ["bootstrap", "!check"]

def pre_build(self):
    self.make.invoke("maintainer-clean")

def do_install(self):
    self.install_dir("usr/bin")
    self.install_link("usr/bin", "bin")
    self.make.install([
        "prefix=" + str(self.chroot_destdir / "usr"),
        "etcdir=" + str(self.chroot_destdir / "etc")
    ])
    self.rm(self.destdir / "bin")

def post_install(self):
    self.install_license("debian/copyright")
