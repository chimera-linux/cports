pkgname = "bc-gh"
pkgver = "6.7.5"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
make_use_env = True
replaces = ["chimerautils-extra<=14.0.1-r0"]
pkgdesc = "Implementation of POSIX bc with GNU extensions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://git.yzena.com/gavin/bc"
source = f"https://github.com/gavinhoward/bc/releases/download/{pkgver}/bc-{pkgver}.tar.xz"
sha256 = "c3e02c948d51f3ca9cdb23e011050d2d3a48226c581e0749ed7cbac413ce5461"
hardening = ["vis", "cfi"]


def do_configure(self):
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
def _man(self):
    self.replaces = ["chimerautils-extra-man<=14.0.1-r0"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "base-man"]

    return ["usr/share/man"]
