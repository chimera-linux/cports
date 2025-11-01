pkgname = "whois"
pkgver = "5.6.5"
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
url = "https://salsa.debian.org/md/whois"
source = f"{url}/-/archive/v{pkgver}/whois-v{pkgver}.tar.gz"
sha256 = "bbd7b3ef7bbaaa0acfb2281d78939c6afe1111ab0316b4de507a6e5c1d126b58"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-DHAVE_GETOPT_LONG", "-DHAVE_GETADDRINFO", "-DHAVE_SHA_CRYPT"]
}


def init_install(self):
    self.make_install_args.append(f"INSTALL_ROOT={self.chroot_destdir}")
