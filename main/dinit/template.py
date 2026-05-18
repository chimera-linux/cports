pkgname = "dinit"
pkgver = "0.21.0"
pkgrel = 0
# has some fixes on top of 0.21.0 and feature i want to try
_gitrev = "3aa6f0392034f3e28773b7e90013defd94cb5cfd"
build_style = "configure"
configure_args = [
    "--disable-strip",
    "--enable-shutdown",
    "--sbindir=/usr/bin",
    "--syscontrolsocket=/run/dinitctl",
    "LDFLAGS_EXTRA=-lcap",
    "TEST_LDFLAGS_EXTRA=-lcap",
]
make_check_args = ["check-igr"]  # additional target
makedepends = ["libcap-devel"]
pkgdesc = "Service manager and init system"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/{_gitrev}.tar.gz"
sha256 = "aea2535d1198bb51990d26a75175390a0961ab6759b0359accba577ffd3c00c8"
# hand-rolled configure scripts/makefiles lol
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")
