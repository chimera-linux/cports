pkgname = "dinit"
pkgver = "0.19.1"
# temporary so we get our features
_gitrev = "29c189ac8a12aa1c78e4bfd37b6c5984a9f033da"
pkgrel = 3
build_style = "configure"
configure_args = ["--sbindir=/usr/bin", "--syscontrolsocket=/run/dinitctl"]
make_check_args = ["check-igr"]  # additional target
makedepends = ["libcap-devel"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/archive/{_gitrev}.tar.gz"
sha256 = "2d9901722643282827625d4a9ef77af025116c8c4ba17621a3ac3a98c9ed0b8a"
# hand-rolled configure scripts/makefiles lol
# drop the -lcap later when fixed upstream
tool_flags = {"CXXFLAGS": ["-fno-rtti"], "LDFLAGS": ["-lcap"]}
hardening = ["vis", "cfi"]


def post_install(self):
    with self.pushd("contrib/shell-completion"):
        self.install_completion("bash/dinitctl", "bash", "dinitctl")
        self.install_completion("fish/dinitctl.fish", "fish", "dinitctl")
        self.install_completion("zsh/_dinit", "zsh", "dinitctl")
