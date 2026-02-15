pkgname = "darkman"
pkgver = "2.3.1"
pkgrel = 2
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.Version=v{pkgver}",
    "./cmd/darkman",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "turnstile"]
pkgdesc = "Control dark-mode and light-mode transitions"
license = "ISC"
url = "https://gitlab.com/WhyNotHugo/darkman"
source = f"{url}/-/archive/v{pkgver}/darkman-v{pkgver}.tar.gz"
sha256 = "0d54660b1ac07d648d8caef68fbcbe96337fadbb58dafcf49bba9f2b3114ca3f"
# builds completions with generated binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"darkman.{shell}", "w") as comp_file:
            self.do(
                "build/darkman",
                "completion",
                shell,
                stdout=comp_file,
            )


def post_install(self):
    self.install_license("LICENCE")
    self.install_files(
        "contrib/dbus/nl.whynothugo.darkman.service",
        "usr/share/dbus-1/services",
    )
    self.install_files(
        "contrib/dbus/org.freedesktop.impl.portal.desktop.darkman.service",
        "usr/share/dbus-1/services",
    )
    self.install_files(
        "contrib/portal/darkman.portal",
        "usr/share/xdg-desktop-portal/portals",
    )
    self.install_files(
        "darkman.desktop",
        "usr/share/applications",
    )

    self.install_service("^/darkman.user")

    self.install_man("darkman.1")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"darkman.{shell}", shell)
