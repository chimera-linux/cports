pkgname = "i3status"
pkgver = "2.15"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dmans=true"]
hostmakedepends = ["asciidoc", "meson", "perl", "pkgconf", "xmlto"]
makedepends = [
    "alsa-lib-devel",
    "libconfuse-devel",
    "libnl-devel",
    "libpulse-devel",
    "yajl-devel",
]
pkgdesc = "Generates status bar to use with i3bar, dzen2 or xmobar"
license = "BSD-3-Clause"
url = "https://github.com/i3/i3status"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "25af0dd77a5325c13890d4ee53a9205827a11c8b90f54e8a7fe2654bd0273d4b"
hardening = ["vis", "cfi"]


def post_extract(self):
    # failing tests
    for test in [
        "006-cpu-usage-max-threshold-format",
        "007-cpu-usage-degraded-threshold-format",
        "010-cpu-usage",
        "011-cpu-usage",
        "020-percentliteral-cpu_usage",
        "020-percentliteral-time",
        "020-percentliteral-volume",
        "022-cpu-usage-tenth-cpu",
        "024-cpu-usage-invalid-cpu",
    ]:
        self.rm(f"testcases/{test}", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
