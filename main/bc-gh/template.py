pkgname = "bc-gh"
pkgver = "6.7.6"
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
sha256 = "828f390c2a552cadbc8c8ad5fde6eeaee398dc8d59d706559158330f3629ce35"
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
