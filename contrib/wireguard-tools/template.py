pkgname = "wireguard-tools"
pkgver = "1.0.20210914"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_dir = "src"
make_install_args = [
    "WITH_BASHCOMPLETION=yes",
    "WITH_WGQUICK=yes",
    "WITH_SYSTEMDUNITS=no",
]
hostmakedepends = ["gmake", "pkgconf", "bash"]
makedepends = ["linux-headers"]
checkdepends = ["clang-analyzer", "perl"]
pkgdesc = "Next generation secure network tunnel - tools for configuration"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://www.wireguard.com"
source = f"https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-{pkgver}.tar.xz"
sha256 = "97ff31489217bb265b7ae850d3d0f335ab07d2652ba1feec88b734bc96bd05ac"
tool_flags = {
    "CFLAGS": ['-DRUNSTATEDIR="/run"'],
}
hardening = ["vis", "cfi"]
# the tests are just scan-build
options = ["!check"]


def post_install(self):
    self.install_dir("etc/wireguard", mode=0o700, empty=True)
    self.install_file(
        self.files_path / "wg-quick-all.sh",
        "usr/libexec",
        mode=0o755,
        name="wg-quick-all",
    )
    self.install_service(self.files_path / "wg-quick-all")


@subpackage("wireguard-tools-wg-quick")
def _wgquick(self):
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "bash",
        "iproute2",
        "openresolv",
    ]
    self.pkgdesc = f"{pkgdesc} (wg-quick script)"

    return [
        "etc/dinit.d/wg-quick-all",
        "usr/bin/wg-quick",
        "usr/libexec/wg-quick-all",
        "usr/share/bash-completion/**/wg-quick",
        "usr/share/man/man?/wg-quick.?",
    ]
