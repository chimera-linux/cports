pkgname = "iproute2"
pkgver = "6.8.0"
pkgrel = 0
build_style = "configure"
configure_env = {"CC": "clang"}
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = [
    "bison",
    "flex",
    "gmake",
    "linux-headers",
    "perl",
    "pkgconf",
]
makedepends = [
    "libfl-devel-static",
    "libmnl-devel",
    "libxtables-devel",
    "linux-headers",
]
pkgdesc = "IP routing utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://wiki.linuxfoundation.org/networking/iproute2"
source = f"$(KERNEL_SITE)/utils/net/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "03a6cca3d71a908d1f15f7b495be2b8fe851f941458dc4664900d7f45fcf68ce"
hardening = ["vis", "cfi"]


def init_build(self):
    with self.profile("host"):
        self.make_build_args += [f"HOSTCC={self.get_tool('CC')}"]


def do_check(self):
    self.make.invoke(None, ["-C", "testsuite"])


def post_install(self):
    self.rm(self.destdir / "usr/share/man/man3", recursive=True)
