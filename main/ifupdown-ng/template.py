pkgname = "ifupdown-ng"
pkgver = "0.12.1"
pkgrel = 1
build_style = "makefile"
make_build_target = "all"
make_build_args = ["docs"]
make_install_args = ["install_docs"]
hostmakedepends = ["scdoc"]
makedepends = ["dinit-chimera"]
checkdepends = ["atf", "kyua"]
pkgdesc = "Network configuration manager"
license = "ISC"
url = "https://github.com/ifupdown-ng/ifupdown-ng"
source = f"{url}/archive/refs/tags/ifupdown-ng-{pkgver}.tar.gz"
sha256 = "d42c8c18222efbce0087b92a14ea206de4e865d5c9dde6c0864dcbb2b45f2d85"
# a bunch of tests fail
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
    # service stuff
    self.install_file(
        self.files_path / "ifupdown-ng-dinit", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "ifupdown-ng")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("ifupdown-ng-batman")
def _(self):
    self.subdesc = "batman integration"
    # self.depends = ["batctl"]
    # self.install_if = [self.parent, "batctl"]

    return [
        "usr/libexec/ifupdown-ng/batman",
    ]


@subpackage("ifupdown-ng-ethtool")
def _(self):
    self.subdesc = "ethtool integration"
    self.depends = ["ethtool"]
    self.install_if = [self.parent, "ethtool"]

    return [
        "usr/libexec/ifupdown-ng/ethtool",
    ]


@subpackage("ifupdown-ng-iproute2")
def _(self):
    self.subdesc = "iproute2 integration"
    self.depends = ["iproute2"]
    self.install_if = [self.parent, "iproute2"]

    return [
        "usr/libexec/ifupdown-ng/gre",
        "usr/libexec/ifupdown-ng/mpls",
        "usr/libexec/ifupdown-ng/vrf",
        "usr/libexec/ifupdown-ng/vxlan",
    ]


@subpackage("ifupdown-ng-ppp")
def _(self):
    self.subdesc = "ppp integration"
    self.depends = ["ppp"]
    self.install_if = [self.parent, "ppp"]

    return [
        "usr/libexec/ifupdown-ng/ppp",
    ]


@subpackage("ifupdown-ng-wifi")
def _(self):
    self.subdesc = "wifi integration"
    self.depends = ["wpa_supplicant"]
    self.install_if = [self.parent, "wpa_supplicant"]

    return [
        "usr/libexec/ifupdown-ng/wifi",
    ]


@subpackage("ifupdown-ng-wireguard")
def _(self):
    self.subdesc = "wireguard integration"
    self.depends = ["wireguard-tools"]
    self.install_if = [self.parent, "wireguard-tools"]

    return [
        "usr/libexec/ifupdown-ng/wireguard",
    ]


@subpackage("ifupdown-ng-wireguard-quick")
def _(self):
    self.subdesc = "wg-quick integration"
    self.depends = ["wireguard-tools-wg-quick"]
    self.install_if = [self.parent, "wireguard-tools-wg-quick"]

    return [
        "usr/libexec/ifupdown-ng/wireguard-quick",
    ]
