pkgname = "wget2"
pkgver = "2.2.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-lzma",
    "--with-bzip2",
]
hostmakedepends = [
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
provides = [self.with_pkgver("wget")]
pkgdesc = "GNU downloader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/gnuwget/wget2"
source = f"$(GNU_SITE)/wget/wget2-{pkgver}.tar.gz"
sha256 = "2b3b9c85b7fb26d33ca5f41f1f8daca71838d869a19b406063aa5c655294d357"


def post_install(self):
    # testing-only
    self.uninstall("usr/bin/wget2_noinstall")
    # we don't have wget1
    self.install_link("usr/bin/wget", "wget2")
    # this is only installed with pandoc detected
    self.install_man("docs/man/man1/wget2.1")
    self.install_link("usr/share/man/man1/wget.1", "wget2.1")


@subpackage("wget2-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libwget")]

    return self.default_libs()


@subpackage("wget2-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libwget-devel")]

    return self.default_devel()
