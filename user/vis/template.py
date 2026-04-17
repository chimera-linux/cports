pkgname = "vis"
pkgver = "0.9_git20260301"
_commit = "75cd95b08f379a32519ae4bbd977fea09ec6c847"
_libtermkeyver = "0.22"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = [
    "acl-devel",
    "lua5.5-devel",
    "lua5.5-lpeg",
    "ncurses-devel",
]
checkdepends = ["vim"]
depends = ["lua5.5-lpeg"]
pkgdesc = "Modern, legacy-free, simple yet efficient vim-like text editor"
license = "ISC"
url = "https://github.com/martanne/vis"
source = [
    f"https://github.com/martanne/vis/archive/{_commit}.tar.gz",
    f"https://www.leonerd.org.uk/code/libtermkey-{_libtermkeyver}.tar.gz",
]
source_paths = ["", "./libtermkey"]
sha256 = [
    "18b5597863d55bd70fbc43e2921bfdd7bc5a346f99afc38b9de5f84aa3fc1f3e",
    "6945bd3c4aaa83da83d80a045c5563da4edd7d0374c62c0d35aec09eb3014600",
]
hardening = ["vis", "cfi"]


def prepare(self):
    self.mv("libtermkey/termkey.h", ".")
    self.mv("libtermkey/termkey-internal.h", ".")
    self.mv("libtermkey/termkey.c", ".")
    self.mv("libtermkey/driver-csi.c", ".")
    self.mv("libtermkey/driver-ti.c", ".")


def post_install(self):
    self.install_license("LICENSE")
    self.mv(self.destdir / "usr/bin/vis", self.destdir / "usr/bin/vis-editor")
    self.mv(
        self.destdir / "usr/share/man/man1/vis.1",
        self.destdir / "usr/share/man/man1/vis-editor.1",
    )
