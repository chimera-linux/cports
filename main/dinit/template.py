pkgname = "dinit"
pkgver = "0.17.0"
pkgrel = 1
build_style = "gnu_configure"
# temporary
_commit = "2b8df1e1d1c1371af1d58086635796a3b0781db3"
configure_args = ["--syscontrolsocket=/run/dinitctl"]
configure_gen = []
make_cmd = "gmake"
make_dir = "."
make_check_args = ["check-igr"]  # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
# source = f"https://github.com/davmac314/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "39c6b91fd7a1de419a18d7ed7c61b208660ea47e8cb5bb46f7080bf42425f580"
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]
