pkgname = "whois"
pkgver = "5.6.2"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "CONFIG_FILE=/etc/whois.conf",
    "HAVE_ICONV=1",
]
make_install_target = "install-whois"
make_install_args = ["install-mkpasswd"]
hostmakedepends = [
    "gettext",
    "perl",
    "pkgconf",
]
makedepends = [
    "libidn2-devel",
]
pkgdesc = "Intelligent WHOIS Client"
license = "GPL-2.0-or-later"
url = "https://github.com/rfc1036/whois"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0773cf51fc9a980af3954fb3859c7673f8bb7901c5be4041a12c926609edeb89"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-DHAVE_GETOPT_LONG", "-DHAVE_GETADDRINFO", "-DHAVE_SHA_CRYPT"]
}


def init_install(self):
    self.make_install_args.append(f"INSTALL_ROOT={self.chroot_destdir}")
