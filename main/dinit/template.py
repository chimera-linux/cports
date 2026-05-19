pkgname = "dinit"
pkgver = "0.22.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--disable-strip",
    "--enable-shutdown",
    "--platform=Linux",
    "--sbindir=/usr/bin",
    "--syscontrolsocket=/run/dinitctl",
]
make_check_args = ["check-igr"]  # additional target
makedepends = ["libcap-devel"]
pkgdesc = "Service manager and init system"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/v{pkgver}.tar.gz"
sha256 = "926d431e1c596a214612a1fc31c66fc0356630c5759edc313fe7153eaf462ffc"
# hand-rolled configure scripts/makefiles lol
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")
