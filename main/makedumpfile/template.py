pkgname = "makedumpfile"
pkgver = "1.7.6"
pkgrel = 0
build_style = "makefile"
make_build_args = ["LINKTYPE=dynamic", "USELZO=on", "USEZSTD=on"]
make_use_env = True
makedepends = [
    "elfutils-devel",
    "bzip2-devel",
    "linux-headers",
    "lzo-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Make Linux crash dump small by filtering and compressing pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/makedumpfile/makedumpfile"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c949a5b2ad95e5f83a6d1b4faac0972510e4286b0e3257020762e45357816a61"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

match self.profile().arch:
    case "aarch64" | "riscv64" | "x86_64":
        make_build_args += [f"TARGET={self.profile().arch}"]
    case "armhf" | "armv7":
        make_build_args += ["TARGET=arm"]
    case "ppc64" | "ppc64le":
        make_build_args += ["TARGET=powerpc64"]
    case "ppc":
        make_build_args += ["TARGET=powerpc32"]
    case _:
        broken = f"Unknown architecture {self.profile().arch}"


def install(self):
    self.install_bin("makedumpfile")
    self.install_bin("makedumpfile-R.pl")
    self.install_man("makedumpfile.8")
    self.install_man("makedumpfile.conf.5")
    self.install_file("makedumpfile.conf", "usr/share/examples/makedumpfile")


@subpackage("makedumpfile-perl")
def _(self):
    self.depends = [self.parent, "perl"]
    self.install_if = [self.parent, "perl"]
    self.subdesc = "Perl scripts"

    return ["usr/bin/makedumpfile-R.pl"]
