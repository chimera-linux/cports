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
    "curl",
    "tpm2-tools",
]
checkdepends = [
    "curl",
    "keyutils",
    "lsof",
    "socat",
    "tang",
]
pkgdesc = "Pluggable framework for automated decryption"
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


@subpackage("clevis-luks")
def _(self):
    self.depends = [self.parent, "luksmeta", "jq"]
    self.subdesc = "luks integration"
    return [
        "usr/bin/clevis-luks-bind",
        "usr/bin/clevis-luks-common-functions",
        "usr/bin/clevis-luks-edit",
        "usr/bin/clevis-luks-list",
        "usr/bin/clevis-luks-pass",
        "usr/bin/clevis-luks-regen",
        "usr/bin/clevis-luks-report",
        "usr/bin/clevis-luks-unbind",
        "usr/bin/clevis-luks-unlock",
        "usr/share/man/man1/clevis-luks-bind.1",
        "usr/share/man/man1/clevis-luks-edit.1",
        "usr/share/man/man1/clevis-luks-list.1",
        "usr/share/man/man1/clevis-luks-pass.1",
        "usr/share/man/man1/clevis-luks-regen.1",
        "usr/share/man/man1/clevis-luks-report.1",
        "usr/share/man/man1/clevis-luks-unbind.1",
        "usr/share/man/man1/clevis-luks-unlock.1",
        "usr/share/man/man1/clevis.1",
        "usr/share/man/man7/clevis-luks-unlockers.7",
        "usr/share/initramfs-tools/hooks/clevis",
        "usr/share/initramfs-tools/scripts/local-bottom/clevis",
        "usr/share/initramfs-tools/scripts/local-top/clevis",
    ]
