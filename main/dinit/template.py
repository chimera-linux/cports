pkgname = "dinit"
pkgver = "0.17.1"
pkgrel = 2
_commit = "f28ab8c656afa9dcb5a61d5cd4b91f1b43760c3a"
build_style = "gnu_configure"
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
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "0da1bf4b4305d2132af73ea24336d4894b9eb544d6c5f6ae8893c78564fdbf7a"
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def init_configure(self):
    self.configure_env["CXX_FOR_BUILD"] = "clang++"
    self.configure_env["CXXFLAGS_FOR_BUILD"] = self.get_cxxflags(
        shell=True, target="host"
    )
    self.configure_env["LDFLAGS_FOR_BUILD"] = self.get_ldflags(
        shell=True, target="host"
    )
