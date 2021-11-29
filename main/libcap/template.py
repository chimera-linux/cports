pkgname = "libcap"
pkgver = "2.61"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["GOLANG=no", "OBJCOPY=llvm-objcopy", "RANLIB=llvm-ranlib"]
make_install_args = [
    "PKGCONFIGDIR=/usr/lib/pkgconfig",
    "SBINDIR=/usr/bin",
    "LIBDIR=/usr/lib",
    "exec_prefix=/usr",
    "RAISE_SETFCAP=no",
]
make_check_target = "test"
make_use_env = True
hostmakedepends = ["pkgconf", "gmake", "perl", "bash"]
makedepends = ["attr-devel", "linux-headers"]
pkgdesc = "POSIX.1e capabilities suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://sites.google.com/site/fullycapable"
source = f"$(KERNEL_SITE)/libs/security/linux-privs/libcap2/{pkgname}-{pkgver}.tar.xz"
sha256 = "c1e29680f8bcc51b172e9a8eb9a7a4d7255a00a14301a7c2cf96d1febf7449a5"

def init_configure(self):
    eargs = [
        "CC=" + self.get_tool("CC"),
        "BUILD_CC=" + self.get_tool("CC", target = "host"),
    ]
    self.make_build_args += eargs
    self.make_check_args += eargs

@subpackage("libcap-static")
def _static(self):
    return self.default_static()

@subpackage("libcap-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel(man = True)

@subpackage("libcap-progs")
def _progs(self):
    return self.default_progs(extra = ["usr/share"])
