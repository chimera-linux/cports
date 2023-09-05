pkgname = "wget2"
pkgver = "2.1.0"
pkgrel = 0
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
    "gnutls-devel",
    "libpsl-devel",
    "libidn2-devel",
    "zlib-devel",
    "zstd-devel",
    "xz-devel",
    "bzip2-devel",
    "brotli-devel",
    "nghttp2-devel",
    "pcre2-devel",
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
    self.rm(self.destdir / "usr/bin/wget2_noinstall")
    # we don't have wget1
    self.install_link("wget2", "usr/bin/wget")


@subpackage("libwget")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime libraries)"
    return self.default_libs()


@subpackage("libwget-devel")
def _dev(self):
    return self.default_devel()
