pkgname = "f3-utils"
pkgver = "9.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["all", "extra"]
make_install_args = ["install-extra"]
make_use_env = True
makedepends = ["argp-standalone", "parted-devel", "linux-headers", "udev-devel"]
pkgdesc = "Flash devices tester"
license = "GPL-3.0-only"
url = "https://github.com/AltraMayor/f3"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "569ec069dc3ec1c74d90d6704aa8b7f45240f5998a9dc6f14f1736c917506ecb"
tool_flags = {
    "LDFLAGS": ["-largp"],
}
# no check target
options = ["!check"]
