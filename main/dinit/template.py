pkgname = "dinit"
pkgver = "0.18.0"
pkgrel = 0
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
source = f"https://github.com/davmac314/dinit/archive/v{pkgver}.tar.gz"
sha256 = "ec854903e93416b3f65e72009dcde4965869d8793e2314565484d94ede534e48"
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
