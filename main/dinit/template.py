pkgname = "dinit"
pkgver = "0.19.1"
# temporary so we get our features
_gitrev = "f883bcb2eabe6c2646bc74647a3aeaece09a9875"
pkgrel = 1
build_style = "configure"
configure_args = ["--sbindir=/usr/bin", "--syscontrolsocket=/run/dinitctl"]
make_check_args = ["check-igr"]  # additional target
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/{_gitrev}.tar.gz"
sha256 = "1dd190e8fb906dfa80316365f0f6fac03113a134763b794fa625183ab8b74878"
tool_flags = {"CXXFLAGS": ["-fno-rtti"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")
