pkgname = "rnnoise"
pkgver = "0_git20210122"
pkgrel = 0
_gitrev = "1cbdbcf1283499bbb2230a6b0f126eb9b236defd"
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Neural network based noise reduction library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://jmvalin.ca/demo/rnnoise"
source = f"https://github.com/xiph/rnnoise/archive/{_gitrev}.tar.gz"
sha256 = "68c7ab4e408426088603e19955e746bb2a412d84bb121b6f39834c60fc8068b7"
hardening = ["vis", "cfi"]


def post_extract(self):
    with open(self.cwd / "package_version", "w") as f:
        f.write(f'PACKAGE_VERSION="{pkgver}"\n')


def post_install(self):
    self.install_license("COPYING")


@subpackage("rnnoise-devel")
def _devel(self):
    return self.default_devel()
