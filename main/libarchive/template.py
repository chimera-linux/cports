pkgname = "libarchive"
pkgver = "3.7.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-acl",
    "--enable-xattr",
    "--without-expat",
    "--with-lz4",
    "--without-xml2",
    "--without-nettle",
    "--disable-rpath",
]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "acl-devel",
    "bzip2-devel",
    "lz4-devel",
    "xz-devel",
    "musl-bsd-headers",
    "zlib-devel",
]
pkgdesc = "Library to read/write several different streaming archive formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://www.libarchive.org"
source = f"https://github.com/libarchive/libarchive/releases/download/v{pkgver}/libarchive-{pkgver}.tar.gz"
sha256 = "df404eb7222cf30b4f8f93828677890a2986b66ff8bf39dac32a804e96ddf104"
# encoding failures on musl; harmless
options = ["bootstrap", "!check"]

if self.stage > 0:
    configure_args += ["--with-openssl", "--with-zstd"]
    makedepends += ["openssl-devel", "zstd-devel"]
else:
    configure_args += ["--without-openssl", "--without-zstd"]


def post_install(self):
    self.install_license("COPYING")
    with self.pushd(self.destdir):
        self.mv("usr/bin/bsdtar", "usr/bin/tar")
        self.mv("usr/bin/bsdcpio", "usr/bin/cpio")
        with self.pushd("usr/share/man/man1"):
            self.mv("bsdcpio.1", "cpio.1")
            self.mv("bsdtar.1", "tar.1")
        with self.pushd("usr/share/man/man5"):
            self.mv("mtree.5", "libarchive-mtree.5")


@subpackage("bsdtar")
def _bsdtar(self):
    self.pkgdesc = "BSD utilities using libarchive"

    return self.default_progs(man="15")


@subpackage("libarchive-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()
