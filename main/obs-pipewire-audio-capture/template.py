pkgname = "obs-pipewire-audio-capture"
pkgver = "1.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "obs-studio-devel",
    "pipewire-devel",
]
pkgdesc = "OBS plugin for capturing device and application audio using pipewire"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "GPL-2.0-or-later"
url = "https://obsproject.com/forum/resources/pipewire-audio-capture.1458"
source = f"https://github.com/dimtpap/obs-pipewire-audio-capture/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ce5973187d637edaf5089ac443f364e5ade27b9612082c30c422ab5d8211d88a"
hardening = ["vis", "!cfi"]
