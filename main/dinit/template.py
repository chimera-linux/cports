pkgname = "dinit"
pkgver = "0.16.999"
_commit = "122599a461f3dc90a78f51d9f2c55facc70ee000"
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
sha256 = "b60f73b5c217c1e7ae22bfad972e25583ad3e5ff1da8c1dd5815d8b95f52df91"
hardening = ["vis", "cfi"]

tool_flags = {
    "CXXFLAGS": ["-fno-rtti"]
}

configure_gen = []
