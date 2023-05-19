pkgname = "wget2"
pkgver = "2.0.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-lzma", "--with-bzip2",
]
hostmakedepends = ["pkgconf", "texinfo"]
makedepends = [
    "gnutls-devel", "libpsl-devel", "libidn2-devel", "zlib-devel",
    "libzstd-devel", "liblzma-devel", "libbz2-devel", "brotli-devel",
    "nghttp2-devel", "pcre2-devel",
]
provides = [f"wget={pkgver}-r{pkgrel}"]
pkgdesc = "GNU downloader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/gnuwget/wget2"
source = f"$(GNU_SITE)/wget/{pkgname}-{pkgver}.tar.gz"
sha256 = "0bb7fa03697bb5b8d05e1b5e15b863440826eb845874c4ffb5e32330f9845db1"

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

configure_gen = []
