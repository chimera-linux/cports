pkgname = "dinit"
pkgver = "0.16.999"
_commit = "3f70f79e36a6e2a5edf70738eea953497e25aae4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--syscontrolsocket=/run/dinitctl"]
make_cmd = "gmake"
make_dir = "."
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
#source = f"https://github.com/davmac314/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "65b02ba823584843d2545febb2e121cd9e5184cce59882315293c648d299f4b2"
hardening = ["vis", "cfi"]

tool_flags = {
    "CXXFLAGS": ["-fno-rtti"]
}
