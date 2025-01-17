pkgname = "dinit"
pkgver = "0.19.3"
# temporary so we get our features
_gitrev = "712e1faa6e2faeb4e56d925334266976904096e9"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--sbindir=/usr/bin",
    "--syscontrolsocket=/run/dinitctl",
    "LDFLAGS_EXTRA=-lcap",
    "TEST_LDFLAGS_EXTRA=-lcap",
]
make_check_args = ["check-igr"]  # additional target
makedepends = ["libcap-devel"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/{_gitrev}.tar.gz"
sha256 = "a1595c201ccaaa1af509221eefd20f8abd3f4a00c50e2184851e2fba606b53fb"
# hand-rolled configure scripts/makefiles lol
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")
