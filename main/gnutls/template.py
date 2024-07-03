pkgname = "gnutls"
pkgver = "3.8.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath",
    "--disable-static",
    "--disable-valgrind-tests",
    "--enable-afalg",
    "--enable-ktls",
    "--with-brotli",
    "--with-default-trust-store-file=/etc/ssl/certs/ca-certificates.crt",
    "--with-tpm2",
    "--with-zlib",
    "--with-zstd",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
    "trousers-devel",
]
makedepends = [
    "brotli-devel",
    "gmp-devel",
    "libidn2-devel",
    "libkcapi-devel",
    "libtasn1-devel",
    "libunistring-devel",
    "linux-headers",
    "nettle-devel",
    "p11-kit-devel",
    "tpm2-tss-devel",
    "trousers-devel",
    "unbound-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
# dlopened
depends = ["libtspi"]
pkgdesc = "GNU Transport Layer Security library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gnutls.org"
source = f"https://www.gnupg.org/ftp/gcrypt/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2e1588aae53cb32d43937f1f4eca28febd9c0c7aa1734fc5dd61a7e81e0ebcdd"


def post_install(self):
    self.install_file(self.files_path / "config", "etc/gnutls")


@subpackage("gnutls-devel")
def _devel(self):
    self.depends += ["trousers-devel"]

    return self.default_devel(extra=["usr/share/info"])


@subpackage("gnutls-progs")
def _progs(self):
    return self.default_progs()
