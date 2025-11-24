pkgname = "dinit"
pkgver = "0.20.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--sbindir=/usr/bin",
    "--syscontrolsocket=/run/dinitctl",
    "--platform=Linux",
]
make_check_args = ["check-igr"]  # additional target
makedepends = ["libcap-devel"]
pkgdesc = "Service manager and init system"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/v{pkgver}.tar.gz"
sha256 = "cd75b572a2eab4a9bd0610a2bb8cc154da7e80074e61cb1059a996dfd977baae"
# hand-rolled configure scripts/makefiles lol
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")
