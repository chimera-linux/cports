pkgname = "whois"
pkgver = "5.5.22"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "CONFIG_FILE=/etc/whois.conf",
    "HAVE_ICONV=1",
]
make_install_target = "install-whois"
make_install_args = ["install-mkpasswd"]
hostmakedepends = [
    "gettext",
    "gmake",
    "perl",
    "pkgconf",
]
makedepends = [
    "libidn2-devel",
]
pkgdesc = "Intelligent WHOIS Client"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/rfc1036/whois"
source = f"https://github.com/rfc1036/whois/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b7de4288700951b141420e2b4408f0906eaf4e97409cf5043aee80ef4d31e2b4"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-DHAVE_GETOPT_LONG", "-DHAVE_GETADDRINFO", "-DHAVE_SHA_CRYPT"]
}


def init_install(self):
    self.make_install_args.append(f"INSTALL_ROOT={self.chroot_destdir}")
