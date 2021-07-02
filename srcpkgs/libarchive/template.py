pkgname = "libarchive"
version = "3.5.1"
revision = 2
bootstrap = True
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

if not current.bootstrapping:
    configure_args.append("--with-zstd")
    makedepends.append("libzstd-devel")
else:
    configure_args.append("--without-zstd")

def do_check(self):
    pass

def post_install(self):
    self.install_license("COPYING")
    import os
    os.rename(self.destdir / "usr/bin/bsdtar", self.destdir / "usr/bin/tar")
    os.rename(self.destdir / "usr/bin/bsdcpio", self.destdir / "usr/bin/cpio")

@subpackage("bsdtar")
def _bsdtar(self):
    self.short_desc = "BSD utilities using libarchive"

    def install():
        self.take("usr/bin")
        self.take("usr/share/man/man1")
        self.take("usr/share/man/man5")
        import os
        os.rename(
            self.destdir / "usr/share/man/man5/mtree.5",
            self.destdir / "usr/share/man/man5/libarchive-mtree.5"
        )

    return install

@subpackage("libarchive-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = makedepends + [f"{pkgname}={version}-r{revision}"]

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")
        self.take("usr/share")

    return install
