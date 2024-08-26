pkgname = "nvidia-xconfig"
pkgver = "560.35.03"
pkgrel = 0
archs = ["x86_64"]
build_style = "makefile"
make_build_args = ["MANPAGE_GZIP=0", "STRIP_CMD=true"]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["libpciaccess-devel"]
pkgdesc = "NVIDIA xorg.conf configurator"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "GPL-2.0-only"
url = f"https://github.com/NVIDIA/{pkgname}"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "44ca36160418d86f3ae2842d7198d229193c6e4980c555a8d090cacf6d95698c"
# no tests
options = ["!check"]
