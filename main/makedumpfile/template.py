pkgname = "makedumpfile"
pkgver = "1.7.7"
pkgrel = 0
build_style = "makefile"
make_build_args = ["LINKTYPE=dynamic", "USELZO=on", "USEZSTD=on"]
make_use_env = True
makedepends = [
    "bzip2-devel",
    "elfutils-devel",
    "linux-headers",
    "lzo-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Make Linux crash dump small by filtering and compressing pages"
license = "GPL-2.0-or-later"
url = "https://github.com/makedumpfile/makedumpfile"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "69b4d24ace3024cf2a41f343e162838b62b1b37d6edc7bbad4260fa36217efee"
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
