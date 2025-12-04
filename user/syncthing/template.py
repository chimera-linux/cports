pkgname = "syncthing"
pkgver = "2.0.12"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/syncthing/syncthing/lib/build.Version=v{pkgver}",
    "./cmd/stdiscosrv",
    "./cmd/strelaysrv",
    "./cmd/syncthing",
]
make_check_args = [
    "./lib/...",
    "./cmd/stdiscosrv",
    "./cmd/strelaysrv",
    "./cmd/syncthing",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
go_build_tags = ["noupgrade"]
pkgdesc = "Continuous file synchronization program"
license = "MPL-2.0"
url = "https://syncthing.net"
source = f"https://github.com/syncthing/syncthing/archive/v{pkgver}.tar.gz"
sha256 = "30144685dea371075234fd3d9865d4f5ee25b5bed4bdfa8fd2f7481188e3fb09"


if self.profile().wordsize == 32:
    # 32-bit targets OOM in tests, maintainer recommends using -short to skip
    # those kinds of tests: https://github.com/syncthing/syncthing/issues/6209#issuecomment-561272903
    make_check_args += ["-short"]


def pre_build(self):
    self.do("go", "generate", "github.com/syncthing/syncthing/lib/api/auto")


def post_install(self):
    self.install_license("cmd/strelaysrv/LICENSE", pkgname="syncthing-relaysrv")
    self.install_file(
        "etc/firewall-ufw/syncthing", "usr/lib/ufw/applications.d"
    )
    self.install_file(
        "cmd/stdiscosrv/etc/firewall-ufw/stdiscosrv",
        "usr/lib/ufw/applications.d",
    )
    self.install_file(
        "cmd/strelaysrv/etc/firewall-ufw/strelaysrv",
        "usr/lib/ufw/applications.d",
    )
    self.install_file(
        "etc/linux-desktop/*.desktop", "usr/share/applications", glob=True
    )
    self.install_file("etc/linux-sysctl/30-syncthing.conf", "usr/lib/sysctl.d")

    self.install_man("man/*.[157]", glob=True)

    for f in [32, 64, 128, 256, 512]:
        self.install_file(
            f"assets/logo-{f}.png",
            f"usr/share/icons/hicolor/{f}x{f}/apps",
            name="syncthing.png",
        )
    self.install_file(
        "assets/logo-only.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="syncthing.svg",
    )

    self.install_service("^/syncthing.user")


@subpackage("syncthing-relaysrv")
def _(self):
    self.subdesc = "relay server"
    self.license = "MIT"

    return [
        "cmd:strelaysrv",
        "usr/lib/ufw/applications.d/strelaysrv",
        "usr/share/licenses/syncthing-relaysrv",
    ]


@subpackage("syncthing-discosrv")
def _(self):
    self.subdesc = "discovery server"

    return ["cmd:stdiscosrv", "usr/lib/ufw/applications.d/stdiscosrv"]
