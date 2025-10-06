pkgname = "bc-gh"
pkgver = "7.1.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
make_use_env = True
replaces = ["chimerautils-extra<=14.0.1-r0"]
pkgdesc = "Implementation of POSIX bc with GNU extensions"
license = "BSD-2-Clause"
url = "https://git.yzena.com/gavin/bc"
source = f"https://github.com/gavinhoward/bc/releases/download/{pkgver}/bc-{pkgver}.tar.xz"
sha256 = "1f13663ba0f2435b684321714a4d0b9fff32bb951fc78dc7424cd69bba5c0d3a"
hardening = ["vis", "cfi"]


def post_extract(self):
    # same as gdk-pixbuf pixbuf-fail; with mimalloc this never gets an alloc
    # failure with linux overcommit and eats memory until it gets oom killed
    self.rm("tests/bc/errors/33.txt")


def configure(self):
    self.do(
        self.chroot_cwd / "configure.sh",
        "-GM",
        "-sbc.banner",
        "-sdc.tty_mode",
        env={
            "PREFIX": "/usr",
            "DESTDIR": self.chroot_destdir,
            "HOSTCC": "clang",
            "HOSTCFLAGS": self.get_cflags(shell=True, target="host"),
        },
    )


def post_install(self):
    self.install_license("LICENSE.md")

    self.install_man("manuals/bc.1")
    self.install_man("manuals/dc.1")


@subpackage("bc-gh-man")
def _(self):
    self.replaces = ["chimerautils-extra-man<=14.0.1-r0"]
    self.install_if = [self.parent, "base-man"]

    return ["usr/share/man"]
