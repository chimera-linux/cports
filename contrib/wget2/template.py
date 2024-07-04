pkgname = "wget2"
pkgver = "2.1.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-lzma",
    "--with-bzip2",
]
hostmakedepends = [
    "autoconf",
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "brotli-devel",
    "bzip2-devel",
    "gnutls-devel",
    "libidn2-devel",
    "libpsl-devel",
    "nghttp2-devel",
    "pcre2-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
provides = [f"wget={pkgver}-r{pkgrel}"]
pkgdesc = "GNU downloader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/gnuwget/wget2"
source = f"$(GNU_SITE)/wget/{pkgname}-{pkgver}.tar.gz"
sha256 = "a05dc5191c6bad9313fd6db2777a78f5527ba4774f665d5d69f5a7461b49e2e7"


def post_install(self):
    # testing-only
    self.uninstall("usr/bin/wget2_noinstall")
    # we don't have wget1
    self.install_link("usr/bin/wget", "wget2")
    # this is only installed with pandoc detected
    self.install_man("docs/man/man1/wget2.1")
    self.install_link("usr/share/man/man1/wget.1", "wget2.1")


@subpackage("libwget")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime libraries)"
    return self.default_libs()


@subpackage("libwget-devel")
def _devel(self):
    return self.default_devel()
