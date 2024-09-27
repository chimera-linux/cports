pkgname = "iproute2"
pkgver = "6.11.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--color", "auto"]
configure_env = {"CC": "clang"}
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = [
    "bison",
    "flex",
    "linux-headers",
    "perl",
    "pkgconf",
]
makedepends = [
    "libcap-devel",
    "libfl-devel-static",
    "libmnl-devel",
    "libxtables-devel",
    "linux-headers",
]
pkgdesc = "IP routing utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://wiki.linuxfoundation.org/networking/iproute2"
source = f"$(KERNEL_SITE)/utils/net/iproute2/iproute2-{pkgver}.tar.xz"
sha256 = "1f795398a04aeaacd06a8f6ace2cfd913c33fa5953ca99daae83bb5c534611c3"
# causes some part of the build to silently break which drops support for various features
hardening = ["!vis"]


def init_build(self):
    with self.profile("host"):
        self.make_build_args += [f"HOSTCC={self.get_tool('CC')}"]


def check(self):
    self.make.invoke(None, ["-C", "testsuite"])


def post_install(self):
    # nothing includes the one header here
    self.uninstall("usr/include")
    self.uninstall("usr/share/man/man3")
