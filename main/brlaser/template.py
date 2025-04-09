pkgname = "brlaser"
pkgver = "6.2.7"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["cups-devel"]
pkgdesc = "CUPS driver for monochrome Brother laser printers"
license = "GPL-2.0-or-later"
url = "https://github.com/Owl-Maintain/brlaser"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e67c5726fc1fe53574c2e8b5f72634f1359d0f53586a555eb2489fafd7c81640"
hardening = ["cfi", "vis"]
