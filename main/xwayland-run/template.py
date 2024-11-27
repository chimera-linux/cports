pkgname = "xwayland-run"
pkgver = "0.0.4"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dcompositor=weston"]
hostmakedepends = ["meson"]
depends = [
    "python",
    "weston",
    "xauth",
    "xwayland",
]
pkgdesc = "Utilities around xwayland for running headless applications"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.freedesktop.org/ofourdan/xwayland-run"
source = f"{url}/-/archive/{pkgver}/xwayland-run-{pkgver}.tar.gz"
sha256 = "409eaf44938b120e8abe4e7c4a384d71d6ee1c72239f36e585fa0a2815d0fd8f"
