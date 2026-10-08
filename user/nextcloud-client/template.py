pkgname = "nextcloud-client"
pkgver = "34.0.5"
pkgrel = 0
build_style = "cmake"
configure_args = []
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "inkscape",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kdsingleapplication-devel",
    "kguiaddons-devel",
    "kio-devel",
    "libp11-devel",
    "openssl3-devel",
    "qt6-qt5compat-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebsockets-devel",
    "qtkeychain-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
checkdepends = [
    "cmocka-devel",
]
pkgdesc = "Desktop sync client for Nextcloud"
license = "GPL-2.0-or-later"
url = "https://github.com/nextcloud/desktop"
source = f"{url}/archive/refs/tags/v{pkgver.replace('_', '-')}.tar.gz"
sha256 = "cd520a7b5299c3ee6a5226e662530c38f064427fadab7c8f439e9595ff66f58f"
tool_flags = {
    "CXXFLAGS": ["-Wno-c++20-extensions", "-Wno-deprecated-declarations"]
}
options = ["etcfiles"]


if self.profile.arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
else:
    configure_args += ["-DBUILD_WITH_WEBENGINE=OFF"]
