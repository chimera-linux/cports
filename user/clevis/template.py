pkgname = "clevis"
pkgver = "21"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Duser=_clevis",
    "-Dgroup=_clevis",
]
hostmakedepends = [
    "asciidoc",
    "cryptsetup",
    "initramfs-tools",
    "meson",
    "pkgconf",
    "tpm2-tools",
]
makedepends = [
    "bash-completion",
    "jansson-devel",
    "jose-devel",
    "luksmeta-devel",
]
depends = [
    "bash",
    "jq",
    "luksmeta",
]
checkdepends = [
    "curl",
    "keyutils",
    "lsof",
    "socat",
    "tang",
]
pkgdesc = "Pluggable framework for automated decryption"
maintainer = "natthias <natthias@proton.me>"
license = "GPL-3.0-or-later WITH custom:openssl-exception"
url = "https://github.com/latchset/clevis"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0ba38f0438337a799e98e1ab41ca30670cc8c13eb5f1f628b4680d46e2ef0013"
# cfi causes some tests to fail
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING.openssl")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
