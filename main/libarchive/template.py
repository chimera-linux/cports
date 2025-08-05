pkgname = "libarchive"
pkgver = "3.8.1"
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
    "musl-bsd-headers",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library to read/write several different streaming archive formats"
license = "BSD-2-Clause"
url = "https://www.libarchive.org"
source = f"https://github.com/libarchive/libarchive/releases/download/v{pkgver}/libarchive-{pkgver}.tar.gz"
sha256 = "bde832a5e3344dc723cfe9cc37f8e54bde04565bfe6f136bc1bd31ab352e9fab"
# encoding failures on musl; harmless
options = ["bootstrap", "!check"]

if self.stage > 0:
    configure_args += ["--with-openssl", "--with-zstd"]
    makedepends += ["openssl3-devel", "zstd-devel"]
else:
    configure_args += ["--without-openssl", "--without-zstd"]


def post_install(self):
    self.install_license("COPYING")
    self.rename("usr/bin/bsdtar", "tar")
    # but symlink them back
    self.install_link("usr/bin/bsdtar", "tar")
    self.rename("usr/bin/bsdcpio", "cpio")
    self.install_link("usr/bin/bsdcpio", "cpio")
    self.rename("usr/share/man/man1/bsdcpio.1", "cpio.1")
    self.install_link("usr/share/man/man1/bsdcpio.1", "cpio.1")
    self.rename("usr/share/man/man1/bsdtar.1", "tar.1")
    self.install_link("usr/share/man/man1/bsdtar.1", "tar.1")
    self.rename("usr/share/man/man5/mtree.5", "libarchive-mtree.5")


@subpackage("libarchive-progs")
def _(self):
    self.renames = ["bsdtar"]

    return self.default_progs(man="15")


@subpackage("libarchive-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
