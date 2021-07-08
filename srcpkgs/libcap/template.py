pkgname = "libcap"
version = "2.49"
revision = 0
bootstrap = True
build_style = "gnu_makefile"
make_cmd = "gmake"
make_build_args = ["CC=clang", "BUILD_CC=clang", "GOLANG=no"]
make_install_args = [
    "PKGCONFIGDIR=/usr/lib/pkgconfig",
    "SBINDIR=/usr/bin",
    "LIBDIR=/usr/lib",
    "exec_prefix=/usr",
    "RAISE_SETFCAP=no",
]
make_use_env = True
makedepends = ["attr-devel"]
short_desc = "POSIX.1e capabilities suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
homepage = "http://sites.google.com/site/fullycapable/"
changelog = "https://sites.google.com/site/fullycapable/release-notes-for-libcap"

from cbuild import sites

distfiles = [f"{sites.kernel}/libs/security/linux-privs/libcap2/{pkgname}-{version}.tar.xz"]
checksum = ["e98bc4d93645082ec787730b0fd1a712b38882465c505777de17c338831ee181"]

if not current.bootstrapping:
    hostmakedepends = ["gmake", "perl"]

def pre_build(self):
    if not self.cross_build:
        return

    self.make_build_args.append(f"CROSS_COMPILE={self.cross_triplet}-")

@subpackage("libcap-devel")
def _devel(self):
    self.depends = [f"{pkgname}={version}-r{revision}"]
    self.short_desc = short_desc + " - development files"

    def install():
        self.take("usr/include")
        self.take("usr/lib/libcap.a")
        self.take("usr/lib/libpsx.a")
        self.take("usr/lib/libcap.so")
        self.take("usr/lib/libpsx.so")
        self.take("usr/lib/pkgconfig")
        self.take("usr/share/man/man3")

    return install

@subpackage("libcap-progs")
def _progs(self):
    self.short_desc = short_desc + " - utilities"

    def install():
        self.take("usr/bin")
        self.take("usr/share")

    return install
