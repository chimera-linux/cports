pkgname = "wireguard-tools"
pkgver = "1.0.20250521"
pkgrel = 0
build_style = "makefile"
make_dir = "src"
make_install_args = [
    "WITH_BASHCOMPLETION=yes",
    "WITH_WGQUICK=yes",
    "WITH_SYSTEMDUNITS=no",
]
hostmakedepends = ["pkgconf", "bash"]
makedepends = ["dinit-chimera", "linux-headers"]
checkdepends = ["clang-analyzer", "perl"]
pkgdesc = "Next generation secure network tunnel - tools for configuration"
license = "GPL-2.0-only"
url = "https://www.wireguard.com"
source = f"https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-{pkgver}.tar.xz"
sha256 = "b6f2628b85b1b23cc06517ec9c74f82d52c4cdbd020f3dd2f00c972a1782950e"
tool_flags = {
    "CFLAGS": ['-DRUNSTATEDIR="/run"'],
}
hardening = ["vis", "cfi"]
# the tests are just scan-build
options = ["!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        self.files_path / "wg-quick-all.sh",
        "usr/libexec",
        mode=0o755,
        name="wg-quick-all",
    )
    self.install_service(self.files_path / "wg-quick-all")


@subpackage("wireguard-tools-wg-quick")
def _(self):
    self.depends = [
        self.parent,
        "bash",
        "iproute2",
        "openresolv",
    ]
    self.subdesc = "wg-quick script"

    return [
        "usr/lib/dinit.d/wg-quick-all",
        "usr/bin/wg-quick",
        "usr/libexec/wg-quick-all",
        "usr/share/bash-completion/**/wg-quick",
        "usr/share/man/man?/wg-quick.?",
    ]


@subpackage("wireguard-tools-wg-quick-nftables")
def _(self):
    self.depends = ["nftables"]
    self.subdesc = "wg-quick nftables recommends package"
    self.options = ["empty"]
    self.install_if = [self.with_pkgver("wireguard-tools-wg-quick")]

    return []
