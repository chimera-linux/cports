pkgname = "gopass"
pkgver = "1.17.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "dinit-dbus"]
checkdepends = ["git", "gnupg"]
pkgdesc = "Pass-compatible password manager with more features"
license = "MIT"
url = "https://www.gopass.pw"
source = (
    f"https://github.com/gopasspw/gopass/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "abf3f67e6e2ffa09b802203d1dce324859edbcbaf3f1d95fea6f41118c11d1a0"
# needs initialising git config
options = ["!check"]


def post_install(self):
    self.install_man("gopass.1")
    self.install_license("LICENSE")
    self.install_completion("bash.completion", "bash")
    self.install_completion("zsh.completion", "zsh")
    self.install_completion("fish.completion", "fish")
    self.install_file(
        "contrib/secret-service/org.freedesktop.secrets.service",
        "usr/share/dbus-1/services",
    )
