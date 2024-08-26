pkgname = "nvidia-modprobe"
pkgver = "560.35.03"
pkgrel = 0
archs = ["x86_64"]
build_style = "makefile"
make_build_args = ["MANPAGE_GZIP=0", "STRIP_CMD=true"]
make_use_env = True
makedepends = ["linux-headers"]
pkgdesc = "Load the NVIDIA kernel module and create character device files"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "GPL-2.0-only"
url = f"https://github.com/NVIDIA/{pkgname}"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c89f7f834a1a27c2f9174f4d14026811bf9683edaad9e9e44f0b2869fce91f95"
# no tests
options = ["!check"]
