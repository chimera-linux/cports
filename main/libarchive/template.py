pkgname = "libarchive"
version = "3.5.1"
revision = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-acl", "--enable-xattr", "--without-expat",
    "--with-lz4", "--with-openssl", "--without-xml2",
    "--without-nettle", "--disable-rpath"
]
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "bzip2-devel", "liblzma-devel",
    "acl-devel", "liblz4-devel", "openssl-devel"
]
short_desc = "Library to read/write several different streaming archive formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "http://www.libarchive.org/"
distfiles = [f"https://github.com/libarchive/libarchive/releases/download/{version}/libarchive-{version}.tar.gz"]
checksum = ["9015d109ec00bb9ae1a384b172bf2fc1dff41e2c66e5a9eeddf933af9db37f5a"]

options = ["bootstrap", "!check"]

if not current.bootstrapping:
    configure_args.append("--with-zstd")
    makedepends.append("libzstd-devel")
else:
    configure_args.append("--without-zstd")

def do_check(self):
    pass

def post_install(self):
    self.install_license("COPYING")
    with self.pushd(self.destdir):
        self.mv("usr/bin/bsdtar", "usr/bin/tar")
        self.mv("usr/bin/bsdcpio", "usr/bin/cpio")
        with self.pushd("usr/share/man/man5"):
            self.mv("mtree.5", "libarchive-mtree.5")

@subpackage("bsdtar")
def _bsdtar(self):
    self.short_desc = "BSD utilities using libarchive"

    return [
        "usr/bin",
        "usr/share/man/man1",
        "usr/share/man/man5",
    ]

@subpackage("libarchive-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = makedepends + [f"{pkgname}={version}-r{revision}"]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share",
    ]
