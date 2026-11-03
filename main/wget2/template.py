pkgname = "wget2"
pkgver = "2.3.0"
pkgrel = 0
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
license = "GPL-3.0-or-later"
url = "https://gitlab.com/gnuwget/wget2"
source = f"$(GNU_SITE)/wget/wget2-{pkgver}.tar.gz"
sha256 = "4f1915b2a55a789a15f2f9ada7cc44bca81418e648f76fd88a7f4dd028b2149f"


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
