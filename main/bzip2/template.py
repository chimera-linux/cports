pkgname = "bzip2"
version = "1.0.8"
revision = 0
short_desc = "Freely available, patent free, high-quality data compressor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "bzip2-1.0.6"
homepage = "https://sourceware.org/bzip2"
distfiles = [f"https://sourceware.org/pub/bzip2/bzip2-{version}.tar.gz"]
checksum = ["ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269"]

options = ["bootstrap"]

CFLAGS = ["-fPIC"]

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build([
        "-f", "Makefile-libbz2_so",
        "CFLAGS=" + self.get_cflags(shell = True),
        "LDFLAGS=" + self.get_ldflags(shell = True)
    ])
    self.make.invoke(["bzip2recover", "libbz2.a"], [
        "CFLAGS=" + self.get_cflags(shell = True),
        "LDFLAGS=" + self.get_ldflags(shell = True)
    ])

def do_check(self):
    self.make.invoke("check")

def do_install(self):
    self.cp("bzip2-shared", "bzip2")

    self.install_bin("bzip2")
    self.install_bin("bzip2recover")

    self.install_link("bzip2", "usr/bin/bunzip2")
    self.install_link("bzip2", "usr/bin/bzcat")

    self.install_bin("bzmore")

    self.install_lib("libbz2.so." + version)
    self.install_link("libbz2.so." + version, "usr/lib/libbz2.so")
    self.install_link("libbz2.so." + version, "usr/lib/libbz2.so.1")
    self.install_link("libbz2.so." + version, "usr/lib/libbz2.so.1.0")

    self.install_file("libbz2.a", "usr/lib")
    self.install_file("bzlib.h", "usr/include")

    self.install_man("bzip2.1")
    self.install_link("bzip2.1", "usr/share/man/man1/bunzip2.1")
    self.install_link("bzip2.1", "usr/share/man/man1/bzcat.1")
    self.install_link("bzip2.1", "usr/share/man/man1/bzip2recover.1")

@subpackage("bzip2-devel")
def _devel(self):
    self.depends = [f"{pkgname}={version}-r{revision}"]
    self.short_desc = short_desc + " - development files"

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
    ]
