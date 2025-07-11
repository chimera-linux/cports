pkgname = "vis"
pkgver = "0.9"
_testver = "0.5"
_libtermkeyver = "0.22"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr", "--enable-lua", "--enable-acl"]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = [
    "acl-devel",
    "ncurses-devel",
    "lua5.4-devel",
]
checkdepends = ["lua5.4-lpeg", "vim"]
depends = ["lua5.4-lpeg"]
pkgdesc = "Modern, legacy-free, simple yet efficient vim-like text editor"
license = "ISC"
url = "https://github.com/martanne/vis"
source = [
    f"https://github.com/martanne/vis/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/martanne/vis-test/archive/v{_testver}.tar.gz>test.tar.gz",
    f"https://www.leonerd.org.uk/code/libtermkey-{_libtermkeyver}.tar.gz",
]
source_paths = ["", "./test", "./libtermkey"]
sha256 = [
    "bd37ffba5535e665c1e883c25ba5f4e3307569b6d392c60f3c7d5dedd2efcfca",
    "0098ad933ec1f87bba4b2da9fa84e00cab5612ec3623622c1e5003a245aec7d1",
    "6945bd3c4aaa83da83d80a045c5563da4edd7d0374c62c0d35aec09eb3014600",
]
hardening = ["vis", "cfi"]
# for check
exec_wrappers = [("/usr/bin/clang-cpp", "cpp")]


def prepare(self):
    self.mv("libtermkey/termkey.h", ".")
    self.mv("libtermkey/termkey-internal.h", ".")
    self.mv("libtermkey/termkey.c", ".")
    self.mv("libtermkey/driver-csi.c", ".")
    self.mv("libtermkey/driver-ti.c", ".")


def post_install(self):
    self.install_license("LICENSE")
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vis-editor")
    self.mv(self.destdir / "usr/share/man/man1/vis.1", self.destdir / "usr/share/man/man1/vis-editor.1")

