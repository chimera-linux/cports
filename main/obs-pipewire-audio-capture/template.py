pkgname = "obs-pipewire-audio-capture"
pkgver = "1.2.1"
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
license = "GPL-2.0-or-later"
url = "https://obsproject.com/forum/resources/pipewire-audio-capture.1458"
source = f"https://github.com/dimtpap/obs-pipewire-audio-capture/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "70107cafd2020437fc0b663fdf6a94598b474942a0582b24719a0e76a9f73a50"
hardening = ["vis", "!cfi"]
